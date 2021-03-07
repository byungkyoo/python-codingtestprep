# Data Types

## Numbers

### Integers
#### 정수형에는 (1) 양의정수, (2) 음의정수 (3) 0 이 있다. 
a = 100     # positive 
a = -7      # negative
a = 0       # 0

### Real Numbers
#### 실수형은 소수점 아래의 데이터를 포함하는 수
positive = 157.93 # 양의 실수
negative = -1823.234 # 음의 실수

real_num = 5.    # .만 적어두고 뒤의 0을 생략해도 5.0으로 저장이됨
real_num = .4   # .만 적어두고 앞의 0을 생략해도 0.4로 저장이됨

expo = 1e9      # 10의 9제곱 == 10^9
expo = 71.23e1  # 71.23 * 10^1 = 712.3
expo = 3594e-3  # 3594 * 10^-3 = 3.594

#### Special case (rounding issue)
add = 0.3 + 0.6   # 0.9로 저장되기를 예상
print (add)       # 하지만 실상은 0.89999999999 로 저장됨

if add == 0.9:
    print(True)
else:
    print(False)    #결과적으로 false뜸

#### Special case (fixed)
add = 0.3 + 0.6
add = round(add, 1) # 이렇게 수정하게 되면, 소수점 1의 자리로 반올림 하게 됨
print(add)

if add == 0.9:
    print(True)
else:
    print(False)

### Computing numbers
#### + , - , * , / , %, //, **
#### 나누기 연산자 (/)는 나눠진 결과를 기본적으로 실수형으로 처리. 소수점이 남음
print(7/3) # 2.3333333333333

#### 나머지 연산자 (%)는 홀짝 여부를 알아볼때 유용함. 나머지가 1이면 홀, 0이면 짝
#### 몫 연산자 (//) 는 나눈 결과에서 몫만 알려준다
#### 제곱 연산자 (**)는 제곱을 구하기 위해서 사용됨




## List (리스트) 자료형

#### 리스트는 여러개의 데이터를 연속적으로 담아 처리하기 위해 사용
#### C와 자바같은 배열 (array) 기능을 포함하고 있으며, 
#### 내부적으로 연결리스트 자료구조를 채택하고 있어서 append(), remove() 등의 메서드를 지원
#### list는 array (배열) 혹은 table(테이블)이라고도 불림

### 리스트 만들기
#### list() 혹은 [] (대괄호) 를 이요해서 선언 
a = [1,2,3,4,5,6,7,8,9]
print(a)
print(a[4])
a = []      ### 빈 리스트 선언 1
a = list()  ### 빈 리스트 선언 2

### 1차원 리스트 초기화
#### 크기가 n인 1차원 리스트; 크기가 n이고, 모든값이 0 인 1차원 리스트를 초기화하는 코드
n = 10 
a = [0] * n 
print(a)

### 리스트의 인덱싱과 슬라이싱
#### Indexing (인덱싱): 인덱스 값을 입력하여 리스트의 특정 원소에 접근하는 것
#### 원소값변경 -> a[3] = 특정값을 해당 인덱스에 저장함
#### [a, b] ==> a번부터 b-1번까지. 마지막 숫자-1을 항상 명심

a = [1,2,3,4,5,6,7,8,9]
print(a[1:4]) # 1번부터 3번까지 혹은 2부터 4까지

### 리스트 컴프리헨션
#### 리스트를 초기화하는 방법; 대괄호[] 안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화 할 수 있다

#### 0부터 19까지의 수 중에서 홀수만 포함하는 리스트 1
a = [i for i in range(20) if i % 2 == 1]
print(a)

#### 0부터 19까지의 수 중에서 홀수만 포함하는 리스트 2
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)

#range() ==> 0 을 시작점으로 1을 increment로 특정 숫자까지 올라감
#range(a,b,c) ==> a를 시작점으로 b까지 c의 increment

#### 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i  for i in range(1,10)]
print(array)

### 2차원 리스트 초기화
#### N * M 크기의 리스트

n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)



summary = 0
for _ in range (1,10):
    summary += _
print(summary)

summary = 0
for i in range (1,10):
    summary += i
print(summary)