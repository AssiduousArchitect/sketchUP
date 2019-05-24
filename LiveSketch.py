import cv2
import numpy as np
import os


def sketchUP(image, detail):
    # Convert image to gray-scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Smoothen out the image using Gaussian Blur. This also removes any noise present in the image.
    blur_gray = cv2.GaussianBlur(gray, (5,5), 0)
    
    # Extract edges
    canny_edges = cv2.Canny(blur_gray, detail, 70)
    
    # Do an invert binarize the image 
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask
	
def save_image(image, path, file_num):
	
	if not os.path.exists(path):
		os.mkdir(path)
		
	cv2.imwrite(path + str(file_num)+ '.jpg', image)
	print ("::: Image has been saved.")
	


if __name__ == '__main__':
	
	DETAIL = 50
	PATH = "./Captures/"
	cap = cv2.VideoCapture(0)
	count = 0
	
	print('::: sketchUP :::')
	print('Press Q to exit.')
	print('Press S to Capture the sketch.')

	while True:
		ret, frame = cap.read()
		sketch = sketchUP(frame, DETAIL)
		cv2.imshow('SketchUP - Press Q to Quit.', sketch)
		if cv2.waitKey(0) == ord('q'): 
			break
		elif cv2.waitKey(0) == ord('s'):
			count += 1
			save_image(sketch, PATH, count)
        
	cap.release()
	cv2.destroyAllWindows()      