import cv2
import mediapipe as mp


# initialize face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
   min_detection_confidence=0.2,
   min_tracking_confidence=0.2
)

# initialize webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        break

    # get image dimensions
    image_height, image_width, _ = image.shape

    # convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # detect landmarks
    results = face_mesh.process(image_rgb)

    # extract and draw landmarks
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for landmark in face_landmarks.landmark:
                x = int(landmark.x * image_width)
                y = int(landmark.y * image_height)
                cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
    
    # # draw eye position
    # x = int(results.multi_face_landmarks[0].landmark[8].x * image_width)
    # y = int(results.multi_face_landmarks[0].landmark[8].y * image_height)
    # cv2.circle(image, (x, y), 2, (0, 0, 255), -1)

    # display image
    cv2.imshow("Facial Landmarks", image)

    # exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()