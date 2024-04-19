import cv2

import facial_landmarks as fl
import raycasting as rc

# parameters
WIN_WIDTH = 600 # 2560
WIN_HEIGHT = 300 # 1600

# initialize face mesh
face_mesh = fl.get_face_mesh()

# initialize raycasting
h_viewer = rc.Vec(-1, 0)
v_viewer = rc.Vec(-1, 0)
projection_surface = rc.ProjectionSurface(1, 16)

h_left_ray_anchor = rc.Vec(0, 0.2)
h_right_ray_anchor = rc.Vec(0, -0.2)
h_left_ray = rc.Ray(h_viewer, h_left_ray_anchor, projection_surface)
h_right_ray = rc.Ray(h_viewer, h_right_ray_anchor, projection_surface)

v_left_ray_anchor = rc.Vec(0, 0.4)
v_right_ray_anchor = rc.Vec(0, -0.4)
v_left_ray = rc.Ray(v_viewer, v_left_ray_anchor, projection_surface)
v_right_ray = rc.Ray(v_viewer, v_right_ray_anchor, projection_surface)

# initialize output
img = cv2.imread("test-input/panorama.jpg")
rows, cols, _ = img.shape

# initialize webcam
cap = cv2.VideoCapture(0)

# main loop
while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        break

    # convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # get eye position
    eye_position = fl.get_eye_position(face_mesh, image_rgb)
    if eye_position:
        h_viewer.y = -1 * (eye_position.x - 0.5)
        v_viewer.y = eye_position.y - 0.5
    h_left_ray.update()
    h_right_ray.update()
    v_left_ray.update()
    v_right_ray.update()

    x1 = int(h_right_ray.get_projection_angle() / 180 * cols)
    x2 = int(h_left_ray.get_projection_angle() / 180 * cols)
    y1 = int(v_right_ray.get_projection_angle() / 180 * rows)
    y2 = int(v_left_ray.get_projection_angle() / 180 * rows)
    cropped = img[y1:y2, x1:x2]
    resized = cv2.resize(cropped, (WIN_WIDTH, WIN_HEIGHT))

    cv2.imshow("Resized", resized)
    cv2.waitKey(10)

    # exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()