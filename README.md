# AICI
![AICI_Web_Main](https://user-images.githubusercontent.com/106011096/278024338-6023f0e1-42f4-4ead-b7bf-4a664c2497a2.jpg)

## 프로젝트 내용
>**고객 TM 및 사외공사 신고 관리 자동화 프로세스**   
>**개발기간 : 2023 - 05 - 30 ~ 2023 - 07 - 11**

## 베포주소
>**http://52.63.184.150/**

<hr></hr>

## 프로젝트 소개
본 프로젝트는 KT의 사업부서의 과제로 효율적인 업무를 위한 자동화 시스템 AICI으로 사업 부서에서 제시한 2가지의 요구사항  
   
**1. 고객 TM확인 서비스**   
AICI 시스템으로 장애 영향 고객에 동시다발 고객 TM을 시행 후 결과를 수합하여 확인할 수 있는 서비스인 고객 TM확인 서비스를 개발      
   
**2. 사외공사 신고 서비스**   
AICI시스템으로 사외 공사를 신고하고, 관리 및 자동 응대를 시행할 수 있는 사외 공사 신고 서비스를 개발   

## Architecture
### Presentation  
<div class="badge-container">
<img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=HTML5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS3&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/></div>
   
### Application    
<div class="badge-container">
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=NGINX&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=Gunicorn&logoColor=white"/></div>  

### Database   
<div class="badge-container">
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/></div>   

<hr></hr>

## 화면구성
### 메인페이지
<img src="https://user-images.githubusercontent.com/106011096/278023038-7480518f-b76c-4332-a4ed-89fef88b7c5a.jpg" width="600px" height="300px"/></p>
                |고객TM                          |사외공사                         
|-------------------------------|-----------------------------|
|![고객TM](https://user-images.githubusercontent.com/106011096/278021804-e3e57366-58c6-45a3-9255-d4170ffed935.png) |![사외공사](https://user-images.githubusercontent.com/106011096/278022380-2d783c72-b8e3-4a75-aa3e-b2f6ef877dc6.png) |   

<hr></hr>

## 주요 기능
### 고객 TM확인 서비스
- 고객 TM확인 서비스의 경우 접수된 VOC 내역과 고객 TM확인을 마친 후 수합한 응답 결과 파일 업로드   
- 응답 결과를 한 화면에 배치하여 한 눈에 파악 가능   
### 사외공사 신고 서비스   
- 사외공사자의 음성 파일을 업로드
- 신고된 사외공사에서 날짜, 담당자, 담당자 번호, 공사 위치, 공사 종류 업데이트
- 공사 위치를 알 수 있는 지도 제공
  
<hr></hr>

##3 Tier Architecture
<img src="https://user-images.githubusercontent.com/106011096/278026173-701548a0-dc26-4622-b96f-71f1e6ad4404.png" width="600px" height="300px"/>

<hr></hr>

<hr></hr>

##ERD Diagram
<img src="https://user-images.githubusercontent.com/106011096/278026500-39302bea-8003-4067-a87c-004aceb5e27d.jpg" width="600px" height="300px"/>

<hr></hr>

## Version
- python==3.10.11
- Django==4.2.2
- gunicorn==20.1.0
- ``pip install -r requirements.txt``

## Directory
```
├── AICI_WEB                    # configuration
├── board                       # main page
├── construction                # construction page
├── users                       # sign in / sign up page
├── voc                         # voc page
│
├── media                       # file storage
│   ├── board                   # attatched file in board
│   └── voc                     # attatched excel file in voc
├── static
│   ├── admin
│   │   ├── css
│   │   │   └── vendor
│   │   │       └── select2
│   │   ├── img
│   │   │   └── gis
│   │   └── js
│   │       ├── admin
│   │       └── vendor
│   │           ├── jquery
│   │           ├── select2
│   │           │   └── i18n
│   │           └── xregexp
│   ├── construction
│   ├── home
│   ├── privacy
│   └── service
└── templates
    ├── board
    ├── construction
    ├── users
    └── voc
```

## Apps
### users
- Sign Up / Sign In
- Custom User model
- board
- construction
- voc
