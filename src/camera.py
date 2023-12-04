import cv2

# Designed to work with raspberry pi, but should work with other devices too.
def take_photo():
    cam_port = 0    # Define the camera's port. 0 for the first camera.

    cam = cv2.VideoCapture(cam_port)    # Set up the camera
    result, image = cam.read()          # Take a photo

    # If the photo was taken successfully, write it to where it will be read by the image analysis code
    if result:
        cv2.imwrite("../images/default.png", image)
    # No image detected. Either no camera or some other error occured.
    else:
        print("No picture was taken.")
