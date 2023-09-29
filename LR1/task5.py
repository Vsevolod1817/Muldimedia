import cv2

def task5():
    img = cv2.imread("D:/704.jpg")
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.namedWindow("1Display window", cv2.WINDOW_NORMAL)
    cv2.namedWindow("1Hsv window", cv2.WINDOW_NORMAL)
    cv2.imshow("1Display window", img)
    cv2.imshow("1Hsv window", hsv_image)
    cv2.waitKey(0)

task5()
