import cv2

# Open the webcam
camera = cv2.VideoCapture(0)

while True:
    # Get the current frame
    _, frame = camera.read()

    # Do something with the frame (e.g. draw a funny face on it)
    # ...

    # Show the frame
    cv2.imshow('Webcam', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
camera.release()

# Close the window
cv2.destroyAllWindows()
