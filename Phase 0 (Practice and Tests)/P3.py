import cv2
import pytesseract

img  = cv2.imread("Testimg.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("processed",img)
cv2.waitKey(0)
cv2.destroyAllWindows()