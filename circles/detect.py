import numpy
import cv2
import settings

def detect(path):
    img = cv2.imread(path,0)

    rows = img.shape[0]

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,rows,
                               param1=settings.param1,
                               param2=settings.param2,minRadius=0,maxRadius=0)
    if circles is not None:
        circles = numpy.uint16(numpy.around(circles))
        x, y, count = 0, 0, 0
        for i in circles[0, :]:
            print(i)
            x += i[0]
            y += i[1]
            count += 1
        print(x/count, y/count)
        return x/count, y/count
    else:
        print('No circles in image??')
        return None

