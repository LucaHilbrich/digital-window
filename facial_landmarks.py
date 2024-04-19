import cv2
import mediapipe as mp


def get_face_mesh():
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(
    min_detection_confidence=0.2,
    min_tracking_confidence=0.2
    )
    return face_mesh

def get_eye_position(face_mesh, image_rgb):
    results = face_mesh.process(image_rgb)
    if results.multi_face_landmarks:
        return results.multi_face_landmarks[0].landmark[8]