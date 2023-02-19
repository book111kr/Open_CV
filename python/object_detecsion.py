import numpy as np
import cv2
# red 도형 색인식
Hue_R = 340.84
Saturation_R = 0.628
Value_R = 0.929
lowerRED = np.array([Hue_R / 2 - 10, Saturation_R * 255 - 30, Value_R * 255 - 30])
upperRED = np.array([Hue_R / 2 + 10, Saturation_R * 255 + 30, 255])
# yellow 도형 색인식
Hue_Y = 53.61
Saturation_Y = 0.48
Value_Y = 0.99
lowerYellow = np.array([Hue_Y / 2 - 10, Saturation_Y * 255 - 30, Value_Y * 255 - 30])
upperYellow = np.array([Hue_Y / 2 + 10, Saturation_Y * 255 + 30, 255])
# green 도형 색인식
Hue_G = 97.67
Saturation_G = 0.21
Value_G = 0.97
lowerGreen = np.array([Hue_G / 2 - 10, Saturation_G * 255 - 30, Value_G * 255 - 30])
upperGreen = np.array([Hue_G / 2 + 10, Saturation_G * 255 + 30, 255])
def showcam():
    try:
        print('open cam')
        cap = cv2.VideoCapture(-1)
    except:
        print('Not working')
        return
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    while True:
        ret, frame = cap.read()
        if not ret:
            print('error: faild')
            break
        frame = frame[83:310, 146:475]
        frame = cv2.resize(frame, None, fx=3, fy=3, interpolation=cv2.INTER_LINEAR)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        color_mask_red = cv2.inRange(hsv, lowerRED, upperRED)
        color_mask_yellow = cv2.inRange(hsv, lowerYellow, upperYellow)
        color_mask_green = cv2.inRange(hsv, lowerGreen, upperGreen)
        ret1, thr_red = cv2.threshold(color_mask_red, 127, 255, 0)
        ret2, thr_yellow = cv2.threshold(color_mask_yellow, 127, 255, 0)
        ret3, thr_green = cv2.threshold(color_mask_green, 127, 255, 0)
        contours_red, _ = cv2.findContours(thr_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_yellow, _ = cv2.findContours(thr_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_green, _ = cv2.findContours(thr_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours_red) > 0:
            for i in range(len(contours_red)):
                area = cv2.contourArea(contours_red[i])
                if 20000 < area < 22000:
                    rect = cv2.minAreaRect(contours_red[i])
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)
                    # red box 가운데 좌표값 추출
                    box = np.array(box)
                    box_R = np.mean(box, axis=0)
                    print(box_R)
        if len(contours_yellow) > 0:
            for i in range(len(contours_yellow)):
                area = cv2.contourArea(contours_yellow[i])
                if 14000 < area < 18000:
                    rect = cv2.minAreaRect(contours_yellow[i])
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    cv2.drawContours(frame, [box], 0, (0, 255, 255), 2)
                    # yellow box 가운데 좌표값 추출
                    box = np.array(box)
                    box_Y = np.mean(box, axis=0)
                    print(box_Y)
        if len(contours_green) > 0:
            for i in range(len(contours_green)):
                area = cv2.contourArea(contours_green[i])
                if 14000 < area < 25000:
                    rect = cv2.minAreaRect(contours_green[i])
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    cv2.drawContours(frame, [box], 0, (255, 255, 255), 2)
                    # green box 가운데 좌표값 추출
                    box = np.array(box)
                    box_G = np.mean(box, axis=0)
                    print(box_G)
        if not ret:
            print('error')
            break
        # cv2.imshow('color_bitwise',color_mask)
        cv2.imshow('cam_load',frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
showcam()
