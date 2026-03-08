import cv2

def preprocess_image(path):

    img = cv2.imread(path)

    img = cv2.resize(img,(256,256))

    blur = cv2.GaussianBlur(img,(5,5),0)

    gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray,100,200)

    return img, blur, gray, edges