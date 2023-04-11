# Machine Learning Mid-Project

<h3>주제 : 수도권 지하철 이용자 및 만 65세 이상 이용자에 의한 운임 수입 및 운임 손실 예측</h3>

<hr>

* **배경**
  * 노령 인구의 증가 및 청, 장년층 인구 감소에 따라 만 65세 이상 노령 인구에 대해 지하철 무임승차에 의한 적자를 방지하기 위한 대책 마련
<br><br>
* **사용된 기술**
  * Scikit-Learn을 이용한 **Linear Regression**, **Polynomial Regression**
  * Python 3.10
  * **Anaconda**, Pandas, Numpy, etc.
<br><br>
* **동작구조**
  * _Input Data_ : 2018년부터 2021년까지 1달 단위의 서울교통공사에 속하는 노선별(1호선 ~ 9호선) 전체 이용객 수와 만 65세 이상의 우대권 이용자 수
    * 데이터 개수 : 4(년) * 12(달) * 9(노선 개수) = 432(개)
  * _Target Data_ : 2018년부터 2021년까지 매년 운송 수입 및 총 적자에 대한 데이터
    * Target Data의 경우 통계 기준이 1년 단위로, 월별 전체 이용객수에 비례하도록 운임 수입과 운임 손실을 나눔
    * 데이터 개수 : 4(년) * 12(달) * 9(노선 개수) = 432(개)
  * **전체 이용자**와 **우대권 이용자**를 각각 **운임 수입**과 **운임 손실**에 Mapping
    * 이때 사용된 ML 기술은 Polynomial Regression
    * 전체 이용객과 우대권 이용개의 2가지 특성을 각각 수입과 손실에 Mapping
<br><br>
* **한계점**
  * _Coivd - 19_
    * 2020년 총 적자 약 1조 1000억, 2021년 약 9600억
    * 데이터상으로 확인하면, 2019년 대비 2020년 적자 약 2배수 이상 증가(2019년 약 5800억)
    * 정확도 감소 및 예측 정확도가 낮음(아래 학습 및 예측 결과 Screenshot 첨부)  
      ![IMG_5311](https://user-images.githubusercontent.com/89850286/231095650-c825d0f0-e4ec-4646-a049-bcbcd27fa6d3.jpg)
      * 위에서부터 Train Score, Test Score, 예측 적자액, 실제 적자액
<br><br>
* **해결 방안**
  * _데이터 삭제_
    * Covid - 19에 영향이 있었던 2020년과 2021년 **데이터 삭제 후 재학습**
<br><br>
* **파일 설명**
  * [`Data`](https://github.com/IIIBreakeRIII/ML-SubwayPredict/tree/main/Data) 폴더는 현재 사용되는 Excel File
    * `All_Population.xlsx` 는 사용되지 않음
  * [`Dividing_Function_Revenue(Loss).py`](https://github.com/IIIBreakeRIII/ML-SubwayPredict/blob/main/Dividing_Function_Revenue.py) 는 운임 수입 및 적자액을 월별, 호선별 전체 이용자수에 비례해 나눈 후 2차원 List로 생성해주는 파일
    * 뒤에 [`Covid`](https://github.com/IIIBreakeRIII/ML-SubwayPredict/blob/main/Dividing_Function_Loss_Covid.py) 는 코로나 이전 데이터만 불러올 경우에 대한 파일
  * [`Subway_Poly_Loss_Final.py`](https://github.com/IIIBreakeRIII/ML-SubwayPredict/blob/main/Subway_Poly_Revenue_Final.py) 는 Linear Regression과 Polynomial Regression을 이용하여 학습시키는 파일
    * 뒤에 [`Covid`](https://github.com/IIIBreakeRIII/ML-SubwayPredict/blob/main/Subway_Poly_Loss_Covid.py) 는 위와 마찬가지로 코로나 이전 데이터를 이용해서만 학습
  * [`FinalProgram.py`](https://github.com/IIIBreakeRIII/ML-SubwayPredict/blob/main/FinalProgram.py) 는 최종 결과를 보여주기 위한 파일
  <br><br>
<hr>
<br>

* **결론**
  * Screenshot 첨부
  ![IMG_5310](https://user-images.githubusercontent.com/89850286/231096750-4f418347-32c7-42db-ba4f-a429459fcf69.jpg)
    * 운임 수입액은 약 6000만원 ~ 7000만원 정도의 오차
    * 운임 적자액은 약 8000만원 정도의 오차
<br><br>
<hr>
<br><br>

* _**Contributors**_
  * **[_Beom_](https://github.com/BeomKung)**
  * **[_Soyun_](https://github.com/nuyos)**
  * **[_jin-altf4_](https://github.com/jin-altf4)**
