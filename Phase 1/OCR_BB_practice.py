import cv2
import pytesseract
import os

img_pth =  r"C:\Users\91630\Desktop\Projects\OCR Application\Phase 1\82092117.png"

img = cv2.imread(img_pth)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3,3) , 0)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

data = pytesseract.image_to_data(binary, output_type=pytesseract.Output.DICT)

for i in range(len(data['text'])):
    if int(data['conf'[i]]) > 50:
        x,y,w,h = data['left'][i], data['top'][i],data['width'][i], data['height'][i]
        word = data['text']

        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img, word, (x,y-10), cv2.FONT_HERSHEY_COMPLEX, 0.5 ,(255,0,0),1)

cv2.imshow("OCR",img)
cv2.waitKey(0)
cv2.destroyAllWindows()