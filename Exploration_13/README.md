# Exploration 13
## 인공지능으로 세상에 없던 새로운 패션 만들기

#### [학습 목표]
- 생성 모델링 개념을 이해하며 판별 모델링과의 차이 알기
- Pix2Pix, CycleGAN 등의 이미지 관련 다양한 생성 모델링의 응용을 접하며 흥미 가지기
- Fashion MNIST 데이터셋의 의미를 알기
- 생성적 적대 신경망(GAN)의 구조와 원리를 이해하기
 - 텐서플로우로 짠 DCGAN 학습 코드를 익히며 응용하기

#### [생성모델링]   
생성 모델링은 지금까지 접해 보았던 기본적인 딥러닝 모델들과는 다르다. \
인공지능과 가위바위보 하기 프로젝트에서는 우리가 직접 가위, 바위, 보에 해당하는 사진을 찍어 데이터셋을 만들고, 각 이미지를 알맞은 카테고리로 분류 할 수 있도록 학습시켰다. 이러한 모델을 우리는 **판별 모델링 (Discriminative Modeling)** 이라고 부르며, 말 그대로 입력받은 데이터를 어떤 기준에 대해 판별하는 것이 목표인 모델링이다.

반면, 이번에 배워 볼 생성 모델링은 말 그대로 없던 데이터를 생성해내는 것이 목표이며, \
가위바위보 프로젝트로 대입해 본다면 다양한 가위, 바위, 보가 담긴 데이터셋에서 각 이미지의 특징을 학습해 그와 비슷한 새로운 사진을 만들어내야 하는 것이 목표이다. 

물론 여기선 실제 사진과 거의 구별이 어려울 정도로 좋은 품질의 이미지를 만들어내는 것이 최종 목표이다.
- 판별 모델 : 입력된 데이터셋을 특정 기준에 따라 분류하거나, 특정 값을 맞추는 모델
- 생성 모델 : 학습한 데이터셋과 비슷하면서도 기존에는 없던 새로운 데이터셋을 생성하는 모델


#### [그림을 사진으로 변환해 보자: Pix2Pix]   
논문 : [https://arxiv.org/pdf/1611.07004.pdf](https://arxiv.org/pdf/1611.07004.pdf)   
Pix2Pix는 간단한 이미지를 입력할 경우 실제 사진처럼 보이도록 바꿔줄 때 많이 사용되는 모델이다. \
단순화된 이미지(Input Image) 와 실제 이미지(Ground Truth) 가 쌍을 이루는 데이터셋으로 학습을 진행한다. \
한 이미지를 다른 이미지로 픽셀 단위로 변환한다는 뜻의 Pixel to Pixel을 딴 `Pix2Pix`로 이름이 지어졌다.

#### [CycleGAN]
##### 모네의 그림을 사진으로, 사진을 다시 모네의 그림으로: CycleGAN
Pix2Pix 이후 발전된 모델로는 **CycleGAN** 이 있으며, 이 모델은 한 이미지와 다른 이미지를 번갈아 가며 Cyclic하게 변환시킬 수 있다.
![image](https://user-images.githubusercontent.com/25050210/131075805-9be87912-3cc3-496d-8189-dcd0388cbd25.png)

#### [Neural Style Transfer]
##### 사진에 내가 원하는 스타일을 입혀보자: Neural Style Transfer
Style Transfer 라는 이름에서 알 수 있듯, 이 기법은 이미지의 스타일을 변환시킨다. \
![image](https://user-images.githubusercontent.com/25050210/131076036-bc8d1665-4552-4718-9a64-24122f69d901.png) \
출처 : https://ml4a.github.io/ml4a/style_transfer/




-------

[jupyter notebook Link](https://github.com/kalina007/AIFFEL_EXPLORATION/blob/main/Exploration_13/practice.ipynb)     
[Exploration 13 Link](https://github.com/kalina007/AIFFEL_EXPLORATION/blob/main/Exploration_13/Exploration_13.ipynb)
