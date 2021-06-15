
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
