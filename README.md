# RoshpitWishList

RoshpitWishList是一個用來追蹤[Roshpit Champions](https://www.roshpit.ca)拍賣品的網站。使用者在網站上設定想要購買的道具屬性，當Roshpit Champions的拍賣場出現符合的拍賣品時，將會透過Line或者是E-mail做通知，通知的內容包含拍賣品詳細的數值與拍賣品連結，透過該連結即可直接前往拍賣場購買。

RoshpitWishList需要搭配[RoshpitCrawler](https://github.com/edensquall/RoshpitCrawler)才能發揮完整的功能，RoshpitCrawler負責爬取Roshpit Champions道具、拍賣品資料與發送通知。

![p1](https://user-images.githubusercontent.com/9337122/71715726-5c0df700-2e4d-11ea-9adb-a13b8bd90b85.jpg) ![p2](https://user-images.githubusercontent.com/9337122/71715756-71832100-2e4d-11ea-8115-b039d57ec2d3.jpg) ![p3](https://user-images.githubusercontent.com/9337122/71715766-7b0c8900-2e4d-11ea-924e-dfd9472e6db6.jpg) ![p4](https://user-images.githubusercontent.com/9337122/71715778-852e8780-2e4d-11ea-9e8f-845684ea015b.jpg)

## 使用框架

- Web框架: [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- ORM框架: [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- 前端框架: [BootStrap](https://getbootstrap.com)

## 架構設計

- 3-Tier Architecture
- MVC Pattern
- Repository Pattern
- Unit of Work Pattern
- Dependency Injection

## 目錄結構
```
.
├── app
│   ├── __init__.py				app的初始化
│   ├── field.py					自訂的WTForms Field
│   ├── forms.py					WTForms表單
│   ├── models						各種Model (MVC:Model)
│   ├── module.py					提供注入物件
│   ├── repositories			各種Repository			
│   ├── services					各種Application Service
│   ├── static						靜態檔案css,img,js
│   ├── templates					各種html頁面模板 (MVC:View)
│   ├── unit_of_works			各種Unit of Work
│   └── views							各種View (MVC:Controller)
├── .env									各種環境變數 (須自行建立)
├── app.yaml							Google App Engine的Python應用程式設定
├── config.py							應用程式設定
├── deploy.yaml						Google App Engine的建構設定
├── requirements.txt			記錄所有需要的套件
├── run.py								程式的進入點
└── venv									虛擬環境 (須自行建立)
```

## 需求

-	Python 3.7+
  https://www.python.org/downloads/
-	MySQL
  https://www.mysql.com


## 安裝與設定

- 建立虛擬環境
```
python3 -m venv venv
```
https://docs.python.org/zh-tw/3/tutorial/venv.html
- 啟動虛擬環境
- 使用pip安裝需要的套件
```
pip install -r requirements.txt
```
https://pip.pypa.io/en/stable/user_guide/#requirements-files2
- 在RoshpitWishList目錄下建立.env檔案
  .env檔案內容如下，此處變數將於config.py被使用，請自行設定 = 後的內容
```
FLASK_ENV = production
FLASK_APP = [FLASK_APP]
SECRET_KEY = [SECRET_KEY]
DATABASE_URL = [DATABASE_URL]
APP_SETTINGS = config.ProductionConfig

CLIENT_ID = [CLIENT_ID]
CLIENT_SECRET = [CLIENT_SECRET]
CALLBACK_URL = [CALLBACK_URL]

IMG_DIR_URL = [IMG_DIR_URL]
```

## 執行

```
python3 run.py
```

## 相關連結

- Roshpit Champions: https://www.roshpit.ca
- RoshpitCrawler: https://github.com/edensquall/RoshpitCrawler
- Flask: https://flask.palletsprojects.com/en/1.1.x/