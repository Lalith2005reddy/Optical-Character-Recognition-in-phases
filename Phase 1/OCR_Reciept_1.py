import cv2
import pytesseract
import json
import os

# Path setup
img_path = r"C:\Users\91630\Desktop\Projects\OCR Application\Phase 1\82092117.png"

# Read image
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3,3), 0)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# OCR with bounding boxes
data = pytesseract.image_to_data(binary, output_type=pytesseract.Output.DICT)

forms = []
for i in range(len(data['text'])):
    word = data['text'][i].strip()
    if word == "":
        continue
    x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
    box = [x, y, x+w, y+h]

    forms.append({
        "box": box,
        "text": word,
        "label": "other",  # default label
        "words": [{
            "box": box,
            "text": word
        }],
        "linking": [],
        "id": i
    })

output = {"form": forms}

# Save JSON
out_path = os.path.join(os.path.dirname(img_path), "ocr_output.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4)

print(f"OCR extraction complete! Saved JSON to:\n{out_path}")
