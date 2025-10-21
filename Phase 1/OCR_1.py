import cv2
import pytesseract

img = cv2.imread(r"C:\Users\91630\Desktop\Projects\OCR Application\Phase 1\82092117.png")

# Convert from color (BGR) to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to remove small noise
gray = cv2.GaussianBlur(gray, (3,3), 0)

# Apply thresholding (binary + Otsu)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Show result
cv2.imshow("Preprocessed", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()


config = "--oem 1 --psm 6"   # LSTM engine, assume block of text
text = pytesseract.image_to_string(binary, config=config)
print("Detected text:\n", text)


print("Cleaned Text")
import re
text = text.strip()
text = re.sub(r'[^A-Za-z0-9\s.,:-]', '', text)
print(text)
