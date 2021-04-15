import cv2

im = cv2.imread("C:/Users/jyoth/Desktop/home_hk_screen.png")

roi = cv2.selectROI(im)

print(roi)

im_cropped = im[int(roi[1]):int(roi[1]+roi[3]),
			int(roi[0]):int(roi[0]+roi[2])]

#for finding the center of the interested region
center=[((roi[3]+roi[2])/2),((roi[1]+roi[0])/2)]
print(center)

cv2.imshow("Cropped Image", im_cropped)
cv2.waitKey(0)
