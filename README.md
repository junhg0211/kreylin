# Kreylin
> Good Timer™

## 실행 방법

1. `Kreylin.exe`를 실행합니다.

### 개발 시 실행 방법

1. [Python](https://python.org)을 다운로드 합니다.
1. [Pygame](https://pypi.org/project/pygame/)과 [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)를 설치합니다.
1. `.`(`./__main__.py`)을 실행합니다.

## 사용법

### 시계
1. (`-`를 입력하여) 실행합니다.

### 타이머
1. <code><시간>`</code>를 입력하여 실행합니다.
   * 시간 포맷은 다음과 같습니다.
     * `N` 분
     * `Ns` 초
     * `Nh` 시간
     * `Nd` 일
     * `Ny` 년
1. 시간이 종료되면 시계 모드로 돌아갑니다.

* 예) <code>30s`</code>

### 스톱워치
1. `/`를 입력하여 실행합니다.

### 알람
1. `<시간>.`을 입력하여 실행합니다.
   * 시간 포맷은 다음과 같습니다.
     * `HHMM` HH시 MM분
     * `HHMMSS` HH시 MM분 SS초
     * `YYYYOODDHHMM` YYYY년 OO월 DD일 HH시 MM분
     * `YYYYOODDHHMMSS` YYYY년 OO월 DD일 HH시 MM분 SS초
1. 시간이 종료되면 시계 모드로 돌아갑니다.

* 예) `2100c`

### 일시정지

1. 백슬래쉬(<code>\\</code>)를 입력하여 화면을 멈춥니다.

### 색상

* 테마를 사용하는 경우
  1. `c`를 입력하여 테마 리스트를 확인합니다.
  1. `<테마>c`를 입력하여 테마를 적용합니다.
     * 예) `gc`
* 색상코드를 사용하는 경우
  1. `<배경색><슬라이더색><글자색>c`를 입력하여 테마를 적용합니다.
     * 예) `ffffff000000000000c`
* 자동 배경색 변경을 사용하려는 경우
  1. c를 2번 누른다.