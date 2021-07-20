# Exploration 3
얼굴에 고양이 스티커 붙히기

[ 사용한 library 및 package ]
- cv2 (opencv python)
- matplotlib
- numpy
- os
- dlib
- cmake

[ 필수 설치 ]
- pip install opencv-python
- pip install cmake
- pip install dlib

[ 사진에 스티커 붙이는 과정 ]
1. 사진을 준비한다.
2. 준비한 사진으로부터 얼굴 영억의 face landmark를 찾아낸다. landmark를 찾기 위해선 얼굴의 bounding box를 먼저 찾아야한다.
3. 찾아낸 영억에 스티커를 붙여넣는다.


## 얼굴 인식 과정
![image](https://user-images.githubusercontent.com/25050210/126277281-6d37afae-c2b3-4480-84ac-593107e8ec59.png)

스티커를 붙이기 위해 세밀하고 자연스럽게 적용하기 위해서 눈, 코, 입, 귀와 같은 얼굴 각각의 위치를 아는 것이 중요하며, <br />
이 위치들을 찾아내는 기술을 **landmark(랜드마크)** 또는 **alignment(조정)** 이라 한다. <br />
큰 범주로는 **keypoint** **detection** 이라 부르고 있으며, 대부분의 face landmark 데이터셋은 눈, 코, 입, 턱을 포함한다.

## 얼굴 검출 (face detection)
dlib를 이용하여 얼굴을 검출한다.
- dlib 의 face detector는 HOG(Histogram of Oriented Gradient) feature를 사용해서 SVM(Support Vector Machine)의 sliding window로 얼굴을 찾습니다.   
[참고자료_얼굴인식- 한국어](https://medium.com/@jongdae.lim/%EA%B8%B0%EA%B3%84-%ED%95%99%EC%8A%B5-machine-learning-%EC%9D%80-%EC%A6%90%EA%B2%81%EB%8B%A4-part-4-63ed781eee3c)   
[참고자료_얼굴인식- 원문](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78)

- 이미지 피라미드에서 얼굴을 다시 검출하면 작게 촬영된 얼굴을 크게 볼 수 있기 때문에 더 정확한 검출이 가능합니다.   
[참고자료_이미지 피라미드](https://opencv-python.readthedocs.io/en/latest/doc/14.imagePyramid/imagePyramid.html)

- dlib detector 는 dlib.rectangles 타입의 객체를 반환.   
[참고자료_dlib_rectangles](http://dlib.net/python/index.html#dlib.rectangles)

## 얼굴 랜드마크 (face landmark)
이목구비의 위치를 추론하는 것을 face landmark localization 기술이라 하며,    
face landmark는 detection의 결과물인 bounding box로 잘라낸(crop) 얼굴 이미지를 이용한다.

### Object keypoint estimation 알고리즘
Face landmark와 같이 객체 내부의 점을 찾는 기술을 object keypoint estimation이라고 하며,    
keypoint를 찾는 알고리즘은 크게 2가지로 나누어 진다.
1) top-down : bounding box를 찾고 box 내부의 keypoint를 예측
2) bottom-up : 이미지 전체의 keypoint를 먼저 찾고 point 관계를 이용해 군집화 해서 box 생성

### Dlib landmark localization
![image](https://user-images.githubusercontent.com/25050210/126280234-8f906e8a-278f-4036-a515-3dfe5464f706.png)            
- [AFLW](https://www.tugraz.at/institute/icg/research/team-bischof/lrs/downloads/aflw/) 데이터셋은 21개를 사용한다.    
- 우리가 이번에 사용할 점은 ibug 300w으로 데이터셋은 68개를 사용한다.      
- Dlib은 ibug [300-W](https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/) 데이터셋으로 학습한 pretrained model 을 제공한다.   
해당 모델은 bzip2로 압축되어 있는 [http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)를 다운받으면 된다. bzip2명령어로 압축을 풀어주면 된다.

## 스티커 적용하기
스티커 위치를 선정할 시 고려해야 될 점은 2가지이다.
1. 스티커 위치
2. 스티커 크기
스티커를 붙힐 위치를 구현하는 방법은 여러가지가 있지만, 필자는 왼쪽눈의 40번을 기준으로 위치를 잡아줬다.


# 문제점
이 프로젝트는 단순히 얼굴을 인식하여 스티커를 적절한 위치에 붙힌다. 하지만 앱으로 출시되기에는 부족한 부분이 많다.
1. 얼굴을 돌릴 때, 스티커도 같이 돌아가야 한다.   
[참고자료](https://happy8earth.tistory.com/492)
3. 스티커를 돌릴 때, 구도와 돌릴때 생기는 빈 배경을 처리해야한다.
      - cv2.getRotationMatrix2D
      - cv2.warpAffine
4. 조명이 밝아지면 얼굴을 인식하는데 문제가 생긴다.

이 밖에 문제점이 굉장히 많지만, 여기까지 하도록 한다.     
구현된 코드를 보고 싶으면 `.ipynb` 확장자가 붙어있는 파일을 클릭하면 된다.
