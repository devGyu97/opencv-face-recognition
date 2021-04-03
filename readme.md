# 얼굴 인식 및 모자이크 처리

 OpenCV를 이용하여 이미지 속 인물의 얼굴은 인식한 후  좌표를 추출하여 저장한다. 이후 다시 이미지를 불러와 입력된 이미지 속 좌표에 맞춰 얼굴을 모자이크 처리한다.



### requirement

****

opencv-python(3.4.5.20) - [설치법](https://bobr2.tistory.com/entry/Python-whl-%ED%8C%8C%EC%9D%BC-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95)

python 3.7

****



### 얼굴 인식

 얼굴 인식을 이용하기 위해서는 location.py를 이용하면 된다.


	python location.py

<code>./img</code> 폴더에 저장되어 있는 이미지를 모두 읽은 뒤 각 이미지마다 인식된 인물들의 얼굴 좌표를  <code> ./location </code> 폴더에 저장 된 xml 파일로 저장한다.

 좌표는 인식된 얼굴을 사각형으로 분류하여 각 꼭지점의 좌표를 뜻한다.

  아래의 예시를 보자.

<a href='https://ifh.cc/v-kFxac1' target='_blank'><img src='https://ifh.cc/g/kFxac1.jpg' border='0'></a>

 인식된 인물들의 얼굴 좌표는 아래와 같다.

```
8 58 1161 58
2118 42 2053 42
636 53 35 53
2 55 3006 55
1 55 1683 55
...생략...
```

### 모자이크 처리
 모자이크 처리는 더욱 간단하다. <code> ./location </code>에 저장되어 있는 좌표를 읽은 뒤 <code> ./img </code>의 이미지에 좌표를 resize한 뒤 다시 원상 복귀 시켜 고의로 좌표에 해당하는 부분을 열화시키는 것이다. 처리 결과는 <code> ./result </code>에 저장된다.

 위의 이미지를 그대로 blur.py에 적용시킨 결과는 아래와 같다.

```
python blur.py
```

<a href='https://ifh.cc/v-PuXbCK' target='_blank'><img src='https://ifh.cc/g/PuXbCK.jpg' border='0'></a>