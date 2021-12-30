# 🍕 velog-hits
**velog-hits**는 자신의 velog 게시글 조회수 통계를 종합해서 한 눈에 보기 쉽도록 HTML 파일로 만들어주는 프로젝트입니다.

## 📍 Demo Image
![Demo Image](./demo.png)

## 📍 시작하기
### 1) 파이썬 버전
- Python >= 3.8

### 2) 설치
- git clone
  ```shell
  $ git clone https://github.com/insutance/velog-hits.git
  ```

- pip install
  ```shell
  $ pip install velog-hits
  ```

## 📍 사용방법
### 1) 도움말 명령어
```shell
$ velog-hits -h
```
```shell
usage: velog-hits [-h] -u USERNAME -at ACCESSTOKEN

Velog Hits

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Velog Username
  -at ACCESSTOKEN, --accesstoken ACCESSTOKEN
                        Your Velog Access Token
```

### 2) Velog Hits 실행

> ⚠️ Access Token을 모르신다면 해당 기능을 사용하실 수 없습니다.

Velog Hits를 사용하기 위해서는 자신의 **Velog Username(=ID)** 와 **Access Token**이 필요합니다.</br>
"조회수 통계"는 로그인 했을 때만 볼 수 있는 기능이기 때문에 Access Token이 필요합니다. Access Token을 통해 본인임을 인증할 수 있습니다.</br> 


```shell
$ velog-hits -u {username} -at {access_token}
```
```shell
'{username}'님의 조회수 데이터를 가져오고 있으니 잠시만 기다려주세요:)
'{username}'님의 조회수 데이터를 모두 가져왔습니다!!
HTML로 변환을 시작합니다...
Velog Hits Success!!
Velog Hits Result: {결과 index.html 파일 위치 경로}
```

(해당 기능을 실행한 후 `.../velog-hits/htmlhits` 경로에 `index.html` 파일이 생성되었을 것입니다.)

### 3) index.html 파일 위치 경로 복사 및 붙여넣기
결과로 나온 `{결과 index.html 파일 위치 경로}` 해당 부분을 복사한 후 **웹 브라우저를 열고 주소창에** 붙여넣기합니다.
