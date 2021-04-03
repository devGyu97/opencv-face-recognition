import cv2
import os

# 얼굴 인식 필터 추가
# 정면
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
# 측면
side_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')

img_list = os.listdir('img/')
img_list.sort()

for i in img_list:
    # 모자이크 해야할 사진 불러오기
    src = cv2.imread('img/'+str(i))
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(src_gray)
    side_faces = side_face_cascade.detectMultiScale(src_gray)

    f = open('location/'+'loc_'+i.rstrip('.jpg')+'.xml', 'w')
    for x, y, w, h in faces:
        f.write((str(y) + ' ' + str(h) + ' ' + str(x) + ' ' + str(w))+'\n')
    for x, y, w, h in side_faces:
        f.write((str(y) + ' ' + str(h) + ' ' + str(x) + ' ' + str(w))+'\n')
f.close()