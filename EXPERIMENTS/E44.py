import cv2
import numpy as np


def create_sample_image(width=256, height=256):
    img = np.full((height, width, 3), (40, 40, 40), dtype=np.uint8)
    cv2.rectangle(img, (40, 50), (120, 180), (0, 180, 255), -1)
    cv2.circle(img, (180, 130), 45, (255, 100, 50), -1)
    return img


def segment_image(image_path: str | None = None):
    if image_path:
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"Could not read image: {image_path}")
    else:
        img = create_sample_image()

    # Method 1: Grayscale + Otsu thresholding
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    otsu_thresh, otsu_mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Method 2: K-Means color segmentation (K=3)
    pixels = img.reshape(-1, 3).astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, labels, centers = cv2.kmeans(pixels, 3, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    segmented_color = centers[labels.flatten()].reshape(img.shape).astype(np.uint8)

    cv2.imwrite("E44_otsu_mask.png", otsu_mask)
    cv2.imwrite("E44_kmeans_segmented.png", segmented_color)

    print(f"Otsu optimal threshold: {otsu_thresh:.2f}")
    print("Saved 'E44_otsu_mask.png' and 'E44_kmeans_segmented.png'")


if __name__ == "__main__":
    segment_image()  # Pass an image path like segment_image("sample.jpg") if desired