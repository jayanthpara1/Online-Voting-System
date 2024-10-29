import cv2
import numpy as np
import time

# Function to create the invisible cloak effect
def invisible_cloak():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Allow the camera to warm up
    time.sleep(3)

    # Capture the background image
    ret, background = cap.read()

    while True:
        # Capture the current frame
        ret, frame = cap.read()

        if not ret:
            break

        # Convert the frame to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the lower and upper range for the color of the cloak (blue in this case)
        lower_blue = np.array([90, 120, 70])
        upper_blue = np.array([120, 255, 255])

        # Create a mask for the cloak color
        mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

        # Perform morphological operations to remove noise from the mask
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

        # Apply bitwise operations to create the final invisible effect
        invisible = cv2.bitwise_and(background, background, mask=mask)
        visible = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
        final_output = cv2.add(invisible, visible)

        # Display the final output
        cv2.imshow("Invisible Cloak", final_output)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to create the invisible cloak effect
invisible_cloak()
