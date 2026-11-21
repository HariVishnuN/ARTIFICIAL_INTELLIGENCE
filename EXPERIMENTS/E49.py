import cv2
import numpy as np


def get_face_detector():
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(cascade_path)
    if detector.empty():
        raise RuntimeError("Failed to load OpenCV Haar Cascade face detector.")
    return detector


def extract_embedding(face_gray: np.ndarray) -> np.ndarray:
    """Normalized 16x16 intensity feature vector as a lightweight fallback embedding."""
    resized = cv2.resize(face_gray, (16, 16), interpolation=cv2.INTER_AREA).astype(np.float32)
    vec = resized.flatten()
    norm = np.linalg.norm(vec)
    return vec / norm if norm > 0 else vec


def cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-8))


def create_synthetic_face(seed: int = 1):
    rng = np.random.default_rng(seed)
    img = np.full((200, 200, 3), 210, dtype=np.uint8)
    # Face oval
    cv2.ellipse(img, (100, 105), (48, 62), 0, 0, 360, (180, 200, 225), -1)
    # Eyes
    cv2.circle(img, (82, 90), 6, (30, 30, 30), -1)
    cv2.circle(img, (118, 90), 6, (30, 30, 30), -1)
    # Mouth
    cv2.ellipse(img, (100, 130), (18, 8), 0, 0, 180, (60, 40, 140), 2)
    noise = rng.integers(-5, 6, size=img.shape, dtype=np.int16)
    return np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)


def main():
    try:
        import face_recognition  # Optional dlib-based pre-trained face model

        known_img = face_recognition.load_image_file("known_person.jpg")
        unknown_img = face_recognition.load_image_file("test_person.jpg")
        known_enc = face_recognition.face_encodings(known_img)[0]
        unknown_encs = face_recognition.face_encodings(unknown_img)
        for idx, enc in enumerate(unknown_encs):
            match = face_recognition.compare_faces([known_enc], enc)[0]
            dist = face_recognition.face_distance([known_enc], enc)[0]
            print(f"Face #{idx + 1}: match={match}, distance={dist:.4f}")
        return
    except Exception:
        pass

    # Fallback demo using OpenCV face detection + embedding similarity
    detector = get_face_detector()
    ref_img = create_synthetic_face(seed=1)
    test_img = create_synthetic_face(seed=2)

    ref_gray = cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY)
    test_gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    ref_faces = detector.detectMultiScale(ref_gray, scaleFactor=1.1, minNeighbors=3)
    test_faces = detector.detectMultiScale(test_gray, scaleFactor=1.1, minNeighbors=3)

    print(f"Detected faces -> reference: {len(ref_faces)}, test: {len(test_faces)}")
    if len(ref_faces) > 0 and len(test_faces) > 0:
        x, y, w, h = ref_faces[0]
        tx, ty, tw, th = test_faces[0]
        emb_ref = extract_embedding(ref_gray[y : y + h, x : x + w])
        emb_test = extract_embedding(test_gray[ty : ty + th, tx : tx + tw])
        print(f"Cosine similarity between detected faces: {cosine_sim(emb_ref, emb_test):.4f}")
    else:
        print("Tip: Install 'face_recognition' or pass real face photos for full pre-trained recognition.")


if __name__ == "__main__":
    main()