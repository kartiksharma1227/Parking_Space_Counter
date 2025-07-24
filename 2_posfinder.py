# # # import cv2
# # # import pickle
# # # width = 107
# # # height = 48
# # # try:
# # #     with open('carparkpos', 'rb') as f:
# # #         posList = pickle.load(f)
# # # except:
# # #     posList = []

# # # def mouseClick(events, x,y, flags, params):
# # #     if events == cv2.EVENT_LBUTTONDOWN:
# # #         posList.append((x,y))
# # #     if events == cv2.EVENT_RBUTTONDOWN:
# # #         for i, pos in enumerate(posList):
# # #             x1, y1 = pos
# # #             if x1<x<x1+width and y1<y<y1+height:
# # #                 posList.pop(i)
# # #     with open('carparkpos', 'wb') as f:
# # #         pickle.dump(posList, f)


# # # while True:
# # #     image = cv2.imread("Image_Video/image.png")
# # #     for pos in posList:
# # #         cv2.rectangle(image, (pos[0], pos[1]), (pos[0] + width, pos[1] + height), (255, 100, 100),2)
# # #     cv2.imshow("Image", image)
# # #     cv2.setMouseCallback("Image", mouseClick)
# # #     if cv2.waitKey(1) & 0xFF == ord('1'):
# # #         break



import cv2
import pickle

drawing = False  # True if mouse is pressed
start_point = (-1, -1)
current_point = (-1, -1)
posList = []

try:
    with open('carparkposnew', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


def mouseClick(event, x, y, flags, params):
    global drawing, start_point, current_point, posList

    # Left Click - Start Drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    # Mouse Move - Update Current Rectangle
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            current_point = (x, y)

    # Left Click Release - Save Rectangle
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        posList.append((start_point, end_point))
        with open('carparkposnew', 'wb') as f:
            pickle.dump(posList, f)

    # Right Click - Delete Rectangle if clicked inside
    elif event == cv2.EVENT_RBUTTONDOWN:
        for i, rect in enumerate(posList):
            (x1, y1), (x2, y2) = rect
            # Handle cases where rectangle may be drawn in reverse direction
            x_min, x_max = min(x1, x2), max(x1, x2)
            y_min, y_max = min(y1, y2), max(y1, y2)

            if x_min < x < x_max and y_min < y < y_max:
                posList.pop(i)
                with open('carparkposnew', 'wb') as f:
                    pickle.dump(posList, f)
                break  # Only delete one at a time


while True:
    image = cv2.imread("Image_Video/image.png")

    # Draw saved rectangles
    for rect in posList:
        cv2.rectangle(image, rect[0], rect[1], (255, 100, 100), 2)

    # Draw current rectangle while dragging
    if drawing:
        cv2.rectangle(image, start_point, current_point, (0, 255, 0), 2)

    cv2.imshow("Image", image)
    cv2.setMouseCallback("Image", mouseClick)

    if cv2.waitKey(1) & 0xFF == ord('1'):
        break

