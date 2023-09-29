import cv2

"out arts with flags"

def task2(window, color, path):
    img = cv2.imread(path, color)
    cv2.namedWindow("Display window", window)
    cv2.imshow("Display window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

task2(cv2.WINDOW_NORMAL, cv2.IMREAD_GRAYSCALE, "D:/704.jpg")
task2(cv2.WINDOW_AUTOSIZE, cv2.COLOR_BGR5552GRAY, "D:/20500268.png")
task2(cv2.WINDOW_FULLSCREEN, cv2.COLOR_BGR2HSV, "D:/20500268.png")
