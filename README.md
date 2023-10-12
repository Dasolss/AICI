# AICI_BigProject
![AICI_Web_Main](https://postfiles.pstatic.net/MjAyMzEwMTJfNjUg/MDAxNjk3MTE4MjYyMDcz.exIyNe-qbXsZ7uLveJrh6IbOGV9LwYBmD4pOtiuzmkEg.kdIrsUPPBbi6-NtPjHK2oDlxnQheFiM-_O7Z9pmAAfwg.PNG.dasol4596/%EC%BA%A1%EC%B2%98.PNG?type=w966)



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
