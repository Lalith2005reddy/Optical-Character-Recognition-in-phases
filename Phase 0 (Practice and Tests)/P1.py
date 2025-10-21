import cv2

img = cv2.imread("Testimg.jpg")
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# resized = cv2.resize(gray,(500,400))


# img = cv2.imread("test_image.png", cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img, 100, 200)  # thresholds
edges = cv2.resize(edges,(600,700))

cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imshow("Original img", img)
# cv2.imshow("Gray Scale",resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()