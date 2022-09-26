import numpy as np
import cv2
import sys
from matplotlib.patches import Circle
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
if len(sys.argv)!=3:
    print("input format is not correct.Please enter image file name and coordinate")
    exit()
#sys.argv[1]



img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
coordinate=sys.argv[2]
print(coordinate)
coordinate=coordinate.replace("(","")
coordinate=coordinate.replace(")","")
seperate=coordinate.split(",")
print(seperate)
x_point=int(seperate[0])
y_point=int(seperate[1])
print(x_point,y_point)



#cv2.imshow("image", img)
#output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        #cv2.circle(img, (x, y), r, (0, 255, 0), 4)
        #cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 128), -1)
        #print(x,y,r)
        circ = Circle((x,y), radius = r)
        print(circ.contains_point([x_point,y_point]))







    # show the output image
    cv2.imshow("output",img)
    cv2.waitKey(0)