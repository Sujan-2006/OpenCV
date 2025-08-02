import cv2 as cv
import os

output_folder = "faces"
os.makedirs(output_folder, exist_ok=True)

haarcascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv.VideoCapture(0)

face_id =1
max_faces =3

while face_id <= max_faces:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_rects = haarcascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)

    for (x, y, w, h) in face_rects:
        face = frame[y:y+h, x:x+w]
        face_filename = os.path.join(output_folder, f"face_{face_id}.jpg")
        cv.imwrite(face_filename, face)
        print(f"[INFO] Saved {face_filename}")
        face_id += 1
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if face_id > max_faces:
            break

    cv.imshow("Live Face Detection", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
