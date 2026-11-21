import cv2
import numpy as np
import torch
from torchvision.models.detection import (
    FasterRCNN_MobileNet_V3_Large_320_FPN_Weights,
    fasterrcnn_mobilenet_v3_large_320_fpn,
)


def main(image_path: str | None = None, score_threshold: float = 0.5):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    weights = FasterRCNN_MobileNet_V3_Large_320_FPN_Weights.DEFAULT
    model = fasterrcnn_mobilenet_v3_large_320_fpn(weights=weights).to(device)
    model.eval()

    if image_path:
        bgr = cv2.imread(image_path)
        if bgr is None:
            raise FileNotFoundError(f"Could not read image: {image_path}")
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    else:
        # Synthetic sample image when no file path is provided
        rgb = np.full((320, 320, 3), 220, dtype=np.uint8)
        cv2.rectangle(rgb, (60, 80), (220, 260), (50, 120, 200), -1)

    tensor = torch.from_numpy(rgb).permute(2, 0, 1).float() / 255.0
    tensor = tensor.to(device)

    with torch.no_grad():
        outputs = model([tensor])[0]

    categories = weights.meta["categories"]
    boxes = outputs["boxes"].cpu().numpy()
    labels = outputs["labels"].cpu().numpy()
    scores = outputs["scores"].cpu().numpy()

    print(f"Detections (score >= {score_threshold}):")
    found = False
    for box, lbl, score in zip(boxes, labels, scores):
        if score >= score_threshold:
            found = True
            name = categories[lbl]
            x1, y1, x2, y2 = [round(float(v), 1) for v in box]
            print(f"  - {name}: confidence={score:.3f}, box={[x1, y1, x2, y2]}")
    if not found:
        print("  No objects above threshold (expected on synthetic placeholder shapes; pass a real photo path).")


if __name__ == "__main__":
    main()  # Example: main("street.jpg", score_threshold=0.5)