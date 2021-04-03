import cv2
import os

# 얼굴 인식 필터 추가
# 정면
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

path = 'img/sfdgwr.jpg'

#img_list = os.listdir('img/')
#img_list.sort()

# 모자이크 농도 설정
ratio = 0.04

# 모자이크 해야할 사진 불러오기
#src = cv2.imread('img/'+str(i))
src = cv2.imread(path)

#cv2.imshow('BEFORE', src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(src_gray)

for x, y, w, h in faces:
    small = cv2.resize(src[136: 242, 160: 266], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    src[136: 242, 160: 266] = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
    '''
        small = cv2.resize(src[y: y + h, x: x + w], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        src[y: y + h, x: x + w] = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
    '''
    #print(y, y+h, x, x+h)


cv2.imwrite('result/result.jpg', src)
#cv2.imshow('AFTER', src)
#cv2.waitKey(0)