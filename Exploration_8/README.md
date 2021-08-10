# Exploration 8
## 인물사진을 만들어 보자

목표는 핸드폰 **인물사진 모드(portrait mode)** 이다.

[인물사진 모드에서 사용되는 용어]
- 얕은 피사계 심도(shallow depth of field), 셸로우 포커스(shallow focus) : 배경을 흐리게 하는 기술. 한국에선 아웃포커싱이라고 주로 얘기하며, "보케(bokeh)"라는 일본어도 많이 사용한다.

[목차]
- 사진을 준비
- 세그멘테이션으로 사람 분리하기
- 시맨틱 세그멘테이션 다뤄보기
- 세그멘테이션 결과를 원래 크기로 복원하기
- 배경 흐리게 하기 (blur)
- 흐린 배경과 원본 영상 합성
- 문제점 찾기
- 문제 해결 솔루션 제시


원래는 카메라 렌즈가 2개여야 하지만 우리들은 1개밖에 없기 때문에 1개의 렌즈로 shallow focus를 구현해보겠다.    
여기서 중요한 개념은 이미지 세그멘테이션(image segmentation) 기술이며, 하나의 이미지에서 배경과 사람을 분리한다.
![image](https://user-images.githubusercontent.com/25050210/128821598-23222aae-89de-4a8c-a744-b3e4d0d1cdff.png)
 
 
### 세그멘테이션(Segmentation)
이미지에서 픽셀 단위로 관심 객체를 추출하는 방법을 **이미지 세그멘테이션(image segmentation)** 라고 한다.   
이미지 세그멘테이션은 모든 픽셀에 라벨(label)을 할당하고 같은 라벨은 "공통적인 특징"을 가진다고 가정하며, 이때 공통 특징은 물리적 의미가 없을 수 있다.   

- 시멘틱 세그멘테이션(semantic segmentation)
세그멘테이션 중에서도 특히 우리가 인식하는 세계처럼 물리적 의미 단위로 인식하는 세그멘테이션을 **시맨틱 세그멘테이션** 이라 한다.    
이미지에서 픽셀을 사람, 자동차, 비행기 등의 물리적 단위로 분류(classification)하는 방법이다.   
![image](https://user-images.githubusercontent.com/25050210/128822990-d3bb6149-5804-498d-82d7-149dbd7ada5d.png)

- 인스턴스 세그멘테이션(Instance segmentation)
시맨틱 세그멘테이션은 '사람'이라는 추상적인 정보를 이미지에서 추출해내는 방법이며. 그래서 사람이 누구인지 관계없이 같은 라벨로 표현이 되지만,   
**인스턴스 세그멘테이션** 은 사람 개개인별로 다른 라벨을 가지게 한다. 여러 사람이 한 이미지에 등장할 때 각 객체를 분할해서 인식하자는 것이 목표이다.

[DeepLab]
세그멘테이션 문제에는 FCN, SegNet, U-Net 등 많은 모델이 사용되지만, 여기에선 DeepLab이라는 세그멘테이션 모델을 만들고 모델에 이미지를 입력할 것이다.   
Deep lab에 관한 자세한 설명은 밑에 링크를 통해 들어가면 된다.   
[DeepLab](https://blog.lunit.io/2018/07/02/deeplab-v3-encoder-decoder-with-atrous-separable-convolution-for-semantic-image-segmentation/), [DeepLab Demo](https://github.com/tensorflow/models/blob/master/research/deeplab/deeplab_demo.ipynb)

---
[jupyter notebook](https://github.com/kalina007/AIFFEL_EXPLORATION/blob/main/Exploration_8/Exploration_8.ipynb)
