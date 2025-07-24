import cv2

image = cv2.imread("Image_Video/image.png")
while True:
    cv2.rectangle(image, (49, 145), (156, 193), (255, 100, 100), 2)
    cv2.imshow("Input Image", image)
    if cv2.waitKey(10) & 0xFF==ord('1'):
        break

"""
STEP 0:
Trying to draw a rectangle on an image using OpenCV.
This while loop will keep the image displayed until the user presses '1'.
The rectangle is drawn at coordinates (49, 145) to (156, 193)
and has a color of (255, 100, 100) with a thickness of 2 pixels.

We drew this manually, but in practice, you would use a mouse callback function
to draw rectangles interactively on the image.

In this step we need to locate the parking space locations in the image.

Basically before working on the video, we need to analyse the image which is the snapshot of the video only and then identify the required things using contour detection and other techniques and then marks them using rectangles.

Then we will use the same rectangle coordinates to mark the parking spaces in the video.



"""