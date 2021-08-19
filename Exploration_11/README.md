# Exploration 11
## 미스터 폐렴, 거기 스탑!

데이터는 [캐글](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)에서 가져왔다.

**의료 영상을 분석하는 것은 일반적인 이미지 처리와는 다른 독특한 특징이 있다.**
- 의료 영상 이미지는 개인 정보 보호 등의 이슈로 인해 데이터를 구하는 것이 쉽지 않다.
- 라벨링 작업 자체가 전문적 지식을 요하므로 데이터셋 구축 비용이 비싸다.
- 희귀질병을 다루는 경우 데이터를 입수하는 것 자체가 드문 일이다.
- 음성/양성 데이터 간 imbalance가 심하므로, 학습에 주의가 필요하다.
- 이미지만으로 진단이 쉽지 않아 다른 데이터와 결합해서 해석해야 할 수도 있다.

[의료 영상 종류]
- X-RAY : 전자를 물체에 충돌시킬 때 발생하는 투과력이 강한 복사선(전자기파)을 말한다. \
X-RAY는 방사선의 일종으로 지방, 근육, 천, 종이같이 밀도가 낮은 것은 수월하게 통과하지만, 밀도가 높은 뼈, 금속 같은 물질은 잘 통과하지 못한다.   
  - 뼈 : 하얀색
  - 근육 및 지방 : 연한 회색
  - 공기 : 검은색

![image](https://user-images.githubusercontent.com/25050210/130027661-61a12484-671a-438e-b0b9-2b4b2f5d4224.png)    
출처 : https://www.highlandradio.com/2018/01/29/works-still-ongoing-on-community-x-ray-units-in-donegal-town-dungloe/

  

- CT : Computed Tomography의 줄임말로, 환자를 중심으로 X-RAY를 빠르게 회전하여 3D 이미지를 만들어내는 영상이다. \
환자의 3 차원 이미지를 형성하여 기본 구조는 물론 가능한 종양 또는 이상을 쉽게 식별하고 위치를 파악할 수 있다. \
신체의 단면 이미지를 "Slice"라고 하며, 이러한 Slice는 단층 촬영 이미지라고도 하며 기존의 X-RAY보다 더 자세한 정보를 포함한다.
- MRI : Magnetic Resonance Imaging(자기 공명 영상)의 줄임말로 신체의 해부학적 과정과 생리적 과정을 보기 위해 사용하는 의료 영상 기술이다. \
MRI 스캐너는 강한 자기장를 사용하여 신체 기관의 이미지를 생성하며, MRI는 CT, X-RAY와 다르게 방사선을 사용하지 않아서 방사선의 위험성에서는 보다 안전하다.

[의료영상 자세]   

![image](https://user-images.githubusercontent.com/25050210/130027278-529a2c36-8e76-4910-8a49-18a8181ee8d2.png)   
출처 : https://www.insilicogen.com/blog/358

- Sagittal plane : 시상면. 사람을 왼쪽과 오른쪽을 나누는 면.
- Coronal plane : 관상면. 인체를 앞뒤로 나누는 면.
- Transverse plane : 횡단면(수평면). 인체를 상하로 나누는 면.

이 프로젝트에선 **Coronal plane**을 사용할 것이다.


-------

[jupyter notebook Link](https://github.com/kalina007/AIFFEL_EXPLORATION/blob/main/Exploration_11/practice.ipynb)     
[Exploration 11 Link](https://github.com/kalina007/AIFFEL_EXPLORATION/blob/main/Exploration_11/Exploration_11.ipynb)
