# Simple Url Counter

## 환경
1. Python 3.11.x


pyenv 로 설정하는 것을 권장합니다.
파이썬 실행환경을 다른 방법으로 구성하실 수 있다면 아래의 pyenv 가이드는 생략하셔도 됩니다.

### pyenv

~~~shell
$ pyenv install 3.11.2
$ pyenv virtualenv 3.11.2 url_counter
$ pyenv local url_counter
~~~

### 설치

~~~shell
$ pip install -e .
~~~

### 실행

~~~shell
$ counter --help  # 도움말 출력

$ counter -d . -r -f  # 현재 폴더 하위의 모든 json 파일에서 url 을 카운팅하고 결과 파일 생성 (단 result_ 로 시작하는 json 파일은 포함되지 않음!)
~~~

#### 옵션 사용예 (도움말 출력 참고할 것!)

~~~shell
$ counter 000.json  # 000.json 에서 카운트 한 결과를 화면에 출력

$ counter 000.json -f  # 000.json 에서 카운트 한 결과를 화면에 출력 및 result_{날짜_시분초}.json 파일로 생성

$ counter 000.json 111.json 222.json ...  # 복수의 json 파일을 카운트 하여 화면에 출력

$ counter 000.json 111.json 222.json ...  -f  # 복수의 json 파일을 카운트 하여 화면에 출력 및 결과 파일 생성

$ counter -d ./0000  # 0000 폴더의 모든 json 파일을 카운트 하여 결과 출력 (하위 폴더는 처리 하지 않음)

$ counter -d ./0000  -f  # 0000 폴더의 모든 json 파일을 카운트 하여 결과 출력 및 파일 생성 (하위 폴더는 포함 하지 않음)

$ counter -d -r -f ./0000  # 0000 폴더의 모든 json 파일을 카운트 하여 결과 출력 및 파일 생성 (하위 폴더 포함)
~~~

### 테스트 (unittest with pytest)

~~~shell
$ pytest -svx -rsa tests
~~~

## 결과 파일 양식

양식: result_{날짜_시분초}.json
~~~json
{
  "targets": [ 카운팅한 파일 목록 ],
  "result": [
    {"카운팅 된 URL": 등장횟수 1위},
    {"카운팅 된 URL": 등장횟수 내림차순으로 정렬},
  ]
}
~~~
Sample: result_20230310_100501.json
~~~json
{
  "targets": [
    "000.json",
    "111.json",
    "222.json"
  ],
  "result": [
    {"https://aaa.com": 100},
    {"https://bbb.com": 50},
    {"https://ccc.com": 10},
    {"https://ddd.com": 1}
  ]
}
~~~
