import cv2
import numpy as np

#Read an image

# img = cv2.imread("img/airplane.png")

# # cv2.rectangle(img, pt1=(100,100), pt2=(300, 300), color=(0, 255, 0), thickness=3)
# cv2.circle(img, center=(300, 300), radius=50, color=(255,0,0), thickness=2)

# cv2.imshow("window", img)

# cv2.waitKey(0)

# drawing = False
# ix = -1
# iy = -1

# def draw(event, x, y ,flags, params):

#     global drawing, ix, iy

#     if event==1:
#         drawing = True
#         ix = x
#         iy = y


#     elif event == 4:

#         fx = x
#         fy = y

#         drawing = False
#         cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(5,0,0), thickness=1)

#         cropped = img[iy:fy, ix:fx]
#         cv2.imshow("cropped", cropped)
#         cv2.waitKey(0)


# cv2.namedWindow(winname="window")
# cv2.setMouseCallback("window", draw)

# img = cv2.imread("img/airplane.png")

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 60.0, (640,480))

while True:

    ret, frame = cap.read()
    out.write(frame)
    
    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

out.release()
cv2.destroyAllWindows()
