# import cv2


# img = cv2.imread("Testimg.jpg")

# cv2.imshow("imges",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# import pytesseract
# from PIL import Image

# img = Image.open("Testimg.jpg")

# text = pytesseract.image_to_string(img, lang="eng")

# print(text)


import cv2
import pytesseract

# Load image using OpenCV
img = cv2.imread("testimg1.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding (optional, helps clean noisy images)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# OCR
text = pytesseract.image_to_string(thresh, lang="eng")

print("Extracted Text:")
print(text)

# Show image (optional, for debugging)
cv2.imshow("Processed", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
