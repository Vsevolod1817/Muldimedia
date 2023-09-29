import cv2

"out arts"

def task1(path):
    img = cv2.imread(path)
    cv2.imshow("out", img)
    cv2.waitKey(0)

task1("D:/704.jpg")
task1("D:/20500268.png")
