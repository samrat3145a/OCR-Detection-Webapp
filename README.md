
# DocCo -> The document management System


This Online document management system is a simple and convenient way for anyone who wants to manage the document, basically getting the OCR of it.
Here Optical Character Recognition, or OCR generator, enables you to convert different types of image documents, such as scanned paper documents, images captured by a digital camera into editable and searchable data.
This system is enabled by the internet – it is the internet only that connects this OCR generator to anyone who access this site.

## Features

- OCR Detection
- Language Translation
- Audio Translation
- PDF to DOC/DOC to PDF
- Image Conversion (supports jpg, png, jpeg, black and white, grayscale)
- Image Compression
  
## Installation 

Installing Xampp
- Install Xampp (Download Link) -> https://sourceforge.net/projects/xampp/

Installing all the dependencies :

```bash 
  pip install django, mysqlclient, opencv-python, pytesseract, requests, winspeech, SpeechRecognition, googletrans, gtts
```
- Create a database name "Samrat" (You can change this name in settings.py)
 
Installing pytesseract application ->

- tesseract-ocr-setup-3.02.02 ->  https://webwerks.dl.sourceforge.net/project/tesseract-ocr-alt/tesseract-ocr-setup-3.02.02.exe
- Install tesseract-ocr-setup-3.02.02
- Open Xampp Control Panel
- Turn on Apache and Mysql in Xampp
- Go to project directory and open a terminal

```bash 
  python manage.py migrate 
  python manage.py runserver
```
- If any error shows up run the following commands : 
```bash 
  python manage.py drop
  python manage.py sqlflush
```
- Some screenshots of this project -> 
- ![image](https://user-images.githubusercontent.com/52879078/124522384-b4da9900-de10-11eb-91f8-95d6136f356d.png)
- ![image](https://user-images.githubusercontent.com/52879078/124522398-c02dc480-de10-11eb-93b5-98d2d256bee7.png)
- ![image](https://user-images.githubusercontent.com/52879078/124522405-c4f27880-de10-11eb-8ac9-cd79a4bbd9c5.png)
- ![image](https://user-images.githubusercontent.com/52879078/124522409-c885ff80-de10-11eb-9af4-0a30118db4e1.png)
- ![image](https://user-images.githubusercontent.com/52879078/124522411-ccb21d00-de10-11eb-86ca-eaaa4df99497.png)
- ![image](https://user-images.githubusercontent.com/52879078/124522418-cfad0d80-de10-11eb-8841-79e2182a50db.png)
![image](https://user-images.githubusercontent.com/52879078/124522426-d50a5800-de10-11eb-965a-5320a24b354a.png)
![image](https://user-images.githubusercontent.com/52879078/124522433-dc316600-de10-11eb-9bbc-566fa0058947.png)







