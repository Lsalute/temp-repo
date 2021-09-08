# Exploration 16
## 흐린 사진을 선명하게 super resolution

### [Super Resolution]  
인공지능이 활발하게 사용되는 기술 중 하나인 Super Resolution에 대해 살펴보고, 직접 활용해 보자.   
Super Resolution이란 저해상도 영상을 고해상도 영상으로 변환하는 작업 또는 그러한 과정을 말한다.   
[참고자료1](http://blog.lgdisplay.com/2014/03/%eb%aa%a8%eb%8b%88%ed%84%b0-%ed%95%b5%ec%8b%ac-%eb%94%94%ec%8a%a4%ed%94%8c%eb%a0%88%ec%9d%b4%ec%9d%98-%ec%8a%a4%ed%8e%99-%eb%94%b0%eb%9d%bc%ec%9e%a1%ea%b8%b0-%ed%95%b4%ec%83%81%eb%8f%84/)   
[참고자료2](https://blog.lgdisplay.com/2014/07/%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%89%BD%EA%B2%8C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-hd-%ED%95%B4%EC%83%81%EB%8F%84%EC%9D%98-%EC%B0%A8%EC%9D%B4/)   
[Deep Learning for Single Image Super-Resolution: A Brief Review](https://arxiv.org/pdf/1808.03344.pdf)

![image](https://user-images.githubusercontent.com/25050210/132469531-432c6c4e-5a9b-4227-878b-b8b687b0429a.png)  
해상도가 높다면 같은 화면이라도 더욱 선명하게 보인다.

### [Super Resolution의 활용 사례]  
- <하얀거탑>이라는 드라마의 리마스터링
- 감시 및 보안 시스템에서 흔히 사용되는 CCTV는 대상의 거리가 멀어짐에 따라 획득한 영상의 해상도가 저하되는 현상이 발생하는 것을 극복
- 의료 영상을 이용하면 구조 정보를 상세하게 관찰할 수 있으므로, 정량적인 이미지 분석 및 진단 등의 의사 결정에 많은 도움을 줌

### [Super Resolution을 어렵게 만드는 요인들]  
1. 하나의 저해상도 이미지에 대해 여러 개의 고해상도 이미지가 나올 수 있다는 것
2. Super Resolution 문제의 복잡도

### [Super Resolution 여러 기법]  
Super Resolution을 수행하는 가장 쉬운 방식은 Interpolation 을 이용하는 것이다.   
[참고 자료: Bilinear interpolation](http://blog.naver.com/dic1224/220882679460)  

### [Deep Learning을 이용한 Super Resolution (1) SRCNN]  
Super Resolution Convolutional Neural Networks의 앞글자를 따서 SRCNN이라고 불리며, 매우 간단한 모델 구조를 사용했음에도 기존 결과에 비해 큰 성능 향상을 이뤄냈다.  
![image](https://user-images.githubusercontent.com/25050210/132469479-482342c2-22da-4995-9785-84329ad553aa.png)  
출처 : https://deepai.org/publication/deep-learning-for-single-image-super-resolution-a-brief-review
[논문 리뷰 SRCNN](https://d-tail.tistory.com/6)

### [Deep Learning을 이용한 Super Resolution (2) SRCNN 이후 제안된 구조들]
#### VDSR (Very Deep Super Resolution)
![image](https://user-images.githubusercontent.com/25050210/132470252-a6d54408-fa23-45e4-9019-8e524e547445.png)   
출처: https://cv.snu.ac.kr/research/VDSR/VDSR_CVPR2016.pdf   
SRCNN과 동일하게 interpolation을 통해 저해상도 이미지의 크기를 늘려 입력으로 사용한다.

#### RDN (Residual Dense Network)
![image](https://user-images.githubusercontent.com/25050210/132470321-9e66b130-8da2-408c-b496-ad77a70494a4.png)  
출처: https://arxiv.org/pdf/1802.08797.pdf   
RDN은 저해상도 이미지가 입력되면, 여러 단계의 convolutional layer를 거치는데 각 layer에서 나오는 출력을 최대한 활용하도록 한다.

#### RCAN (Residual Channel Attention Networks)
![image](https://user-images.githubusercontent.com/25050210/132470960-fc026e51-a050-4d52-8059-cd3686a9f6eb.png)   
출처: https://arxiv.org/pdf/1807.02758.pdf

### Deep Learning을 이용한 Super Resolution (3) SRGAN
GAN(Generative Adversarial Networks) 을 활용한 Super Resolution 과정에 대해 다뤄보자.   
- [GAN - 스스로 학습하는 인공지능](https://www.samsungsds.com/global/ko/support/insights/Generative-adversarial-network-AI.html?moreCnt=19&backTypeId=undefined&category=undefined)   
- [GAN - GAN의 개념과 이해](https://www.samsungsds.com/global/ko/support/insights/Generative-adversarial-network-AI-2.html)

-------

[jupyter notebook Link](https://github.com/kalina007/AIFFEL_EXPLORATION/blob/main/Exploration_16/practice.ipynb)     
[Exploration 16 Link](https://github.com/kalina007/AIFFEL_EXPLORATION/blob/main/Exploration_16/Exploration_16.ipynb)
