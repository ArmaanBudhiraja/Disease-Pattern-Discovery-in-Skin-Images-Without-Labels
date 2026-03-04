from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import matplotlib.pyplot as plt


Tk().withdraw()

image_path = askopenfilename(
    title="Select Skin Image",
    filetypes=[("Image Files","*.jpg *.jpeg *.png")]
)

image = cv2.imread(image_path)
image = cv2.resize(image,(400,400))

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


blur = cv2.GaussianBlur(gray,(5,5),0)


_, thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


if np.mean(thresh) > 127:
    thresh = cv2.bitwise_not(thresh)

contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
c = max(contours,key=cv2.contourArea)


mask = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask,[c],-1,255,-1)


edges = cv2.Canny(mask,100,200)


area = cv2.contourArea(c)
perimeter = cv2.arcLength(c,True)

border_index = (perimeter**2)/(4*np.pi*area)


(x,y),radius = cv2.minEnclosingCircle(c)
diameter = radius*2


lesion_pixels = rgb[mask==255]
color_variance = np.var(lesion_pixels)


risk = 0

if border_index > 1.5:
    risk += 1

if color_variance > 500:
    risk += 1

if diameter > 50:
    risk += 1

if risk >= 2:
    prediction = "Possible Melanoma"
else:
    prediction = "Low Risk"

print("Border Irregularity:",border_index)
print("Color Variance:",color_variance)
print("Diameter:",diameter)
print("Prediction:",prediction)


plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.title("Original Image")
plt.imshow(rgb)
plt.axis("off")

plt.subplot(2,3,2)
plt.title("Grayscale")
plt.imshow(gray,cmap="gray")
plt.axis("off")

plt.subplot(2,3,3)
plt.title("Noise Removal")
plt.imshow(blur,cmap="gray")
plt.axis("off")

plt.subplot(2,3,4)
plt.title("Segmentation")
plt.imshow(thresh,cmap="gray")
plt.axis("off")

plt.subplot(2,3,5)
plt.title("Lesion Mask")
plt.imshow(mask,cmap="gray")
plt.axis("off")

plt.subplot(2,3,6)
plt.title("Edge Detection")
plt.imshow(edges,cmap="gray")
plt.axis("off")

plt.suptitle("ABCDE Melanoma Detection Pipeline")

plt.show()