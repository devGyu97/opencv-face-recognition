import cv2
import os

# 모자이크 농도 설정
ratio = 0.04

img_list = os.listdir('img/')
img_list.sort()

loc_list = os.listdir('location/')
loc_list.sort()

count = 0
for i in img_list:
    src = cv2.imread('img/'+str(i))
    list_file = open('location/loc_'+i.rstrip('.jpg')+'.xml', 'r').read().split('\n')

    cnt = 0
    while True:
        list_file[cnt] = list_file[cnt].split()
        cnt += 1
        if cnt == len(list_file): break

    for i in range(0, len(list_file)-1):
        y = int(list_file[i][0])
        h = int(list_file[i][1])
        x = int(list_file[i][2])
        w = int(list_file[i][3])

        small = cv2.resize(src[y: y + h, x: x + w], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        src[y: y + h, x: x + w] = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)

    cv2.imwrite('result/result_sample'+str(count)+'.jpg', src)
    count += 1

#cv2.imwrite('result/result.jpg', src)
#cv2.imshow('Result', src)
#cv2.waitKey(0)