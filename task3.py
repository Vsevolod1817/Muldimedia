import cv2

def task3(color, size):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Изменения цвета
        hsv_frame = cv2.cvtColor(frame, color)
        # Изменение размера окна
        resized_frame = cv2.resize(hsv_frame, size)
        cv2.imshow('Video', resized_frame)
        if cv2.waitKey(30) & 0xFF == 27:  # Нажмите Esc, чтобы выйти из цикла
            break

"""a = [cv2.COLOR_BGR2HLS, cv2.COLOR_BGR2HSV, cv2.COLOR_RGB2HLS]
b = [(640, 480), (500, 500), (430, 430)]
for i in a:
    for j in b:
        task3(i, j)
        """
task3(cv2.COLOR_BGR2HSV, (640, 480))