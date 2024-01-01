# 좋은 데이터의 기준&데이터 클리닝

### 완결성
데이터는 필수항목 + 선택항목으로 이뤄져있음
필수 항목은 비어있으면 분석할 수 없기 때문에
비어있는 값(결측값)의 여부를 확인해야 한다.
pandas에선 NaN(Not a Number)로 표현함

없는게 가장 좋고, 왜 생기는지 원인을 파악해야됨

```python
df.isnull().sum()    #비어있는 데이터 확인
df.dropna(inplace=True)    #비어있는 데이터가 있다면 해당 row 삭제
df.dropna(axis='columns')    #비어있는 데이터가 있다면 해당 column 삭제
df.fillna(0)    #비어있는 값 0으로 채움
df.fillna(df.mean(),inplace=True)
df.fillna(df.median(),inplace=True)
```


### 유일성
동일한 데이터가 불필요하게 중복되어 있으면 안됨

```python
df.index
df.index.value_counts()
df.drop_duplicates(inplace=True)    #중복된 두 로우 중 하나 삭제
df=df.T.drop_duplicates().T    #.T는 transpose의 약자로 col,row 뒤집기
```

### 통일성
데이터가 동일한 단위로 되어있어야함

### 정확성
데이터가 정확해야함
다른 데이터와 너무 동떨어진 데이터를 이상점(outlier)라고함
너무 비이상적인 데이터라면 제거해야함

# 이상점을 판단하는 기준
절대적인 기준은 없음

### IQR(Interquartile Range)
box_plot에서 25%(Q1)지점과 75%(Q3)지점 사이에 거리

Q1 지점과 Q3 지점에서 1.5 IQR을 넘어가는 데이터를
pandas에서는 이상점이라고 봄

### 이상점 대처
잘못된 데이터면 고치거나 제거
올바른 데이턴데 그래도 쓸모없으면 지우고
필요한 데이터면 사용 이건 분석하는 사람이 판단

```python
df.plot(kind='box',y='abv')
df['abv'].describe()
q1=df['abv'].quantile(0.25)    #q1에 해당하는 값
#quantile 분위수
#확률 분포를 동등한 확률 구간으로 나누는 구분 눈금들
q3=df['abv'].quantile(0.75)
iqr=q3-q1
condition=(df['abv']<q1-1.5*iqr)|(df['abv']>q3+1.5*iqr)
df.loc[2250,'abv']=0.055
df[condition].index
df.drop(df[condition].index,inplace=True)
df.plot(kind='box',y='abv') 
```


### 관계적 이상점(Relational Outlier)
두 변수의 관계를 고려했을 때 이상한 데이터

```python
df.plot(kind='scatter',x='reading score',y='writing score')
df.corr()
df[df['writing score']>100]
df.drop(51,inplace=True)
df.plot(kind='scatter',x='reading score',y='writing score')
df.corr()
condition=(df['writing score']>90)&(df['reading score']<40)
df[condition]
df.drop(373,inplace=True)
df.plot(kind='scatter',x='reading score',y='writing score')
df.corr()
```