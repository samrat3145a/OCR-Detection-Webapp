import cv2
import numpy as np
import pytesseract
from PIL import Image
import os
import requests
import json
import io
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import googletrans 

def Detect_Text_Image_Letter(img_b,path):
    hImg,wImg,_ =  img_b.shape
    boxes=pytesseract.image_to_boxes(img_b)
    for b in boxes.splitlines():
        b=b.split(' ')
        #print(b[0],end ="")
        x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
        cv2.rectangle(img_b,(x,hImg-y),(w,hImg-h),(0,0,255),1) #for showing boxes
        #cv2.putText(img_b,b[0],(x,hImg-y+10),cv2.FONT_HERSHEY_PLAIN,1,(50,50,255),1)
    
    n=len(path)
    f_type=""
    if(path[n-4] == '.' and path[n-3]=='p' and path[n-2]=='n' and path[n-1]=='g'):
        x = path.replace(".png", "")
        f_type=".png"
    if(path[n-5] == '.' and path[n-4] == 'j' and path[n-3]=='p' and path[n-2]=='e' and path[n-1]=='g'):
        x = path.replace(".jpeg", "")
        f_type=".jpeg"
    if(path[n-4] == '.' and path[n-3]=='j' and path[n-2]=='p' and path[n-1]=='g'):
        x = path.replace(".jpg", "")
        f_type=".jpg"
    final_path = str(x)+"_final_output"+f_type
    cv2.imwrite(os.path.join(final_path), img_b)
    #cv2.imshow('Detecting all the Words and Display',img_b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    final_path = final_path.replace("OCR_detection/","/")
    return final_path
    
#For Detection of Word
def Detect_Text_Image_Word(test_image):
    hImg,wImg,_ =  img_b.shape
    boxes=pytesseract.image_to_data(img_b)
    for x,b in enumerate(boxes.splitlines()):
        if(x!=0):    
            b=b.split()
            if(len(b) == 12):
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.rectangle(img_b,(x,y),(w+x,h+y),(0,0,255),1)
                #cv2.putText(img_b,b[11],(x,y),cv2.FONT_HERSHEY_PLAIN,1,(50,50,255),1)
                #For showing the words
    cv2.imshow('Detecting All Word !!!',img_b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def GetImageOCR(img):
    img=cv2.resize(img,None,fx=0.9,fy=0.9)
    #cv2.imshow("Resize Image",img)
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #img_b = cv2.cvtColor(img_b,cv2.COLOR_BGR2RGB)
    #cv2.imshow("GrayScale Image",gray)
    
    adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 85,11)
    #cv2.imshow('Value',adaptive_threshold)
    
    config="--psm 3"
    text=pytesseract.image_to_string(adaptive_threshold,config=config)
    #cv2.imwrite(os.path.join("OCR_detection/static/final_output.jpeg"), adaptive_threshold)
    #print(text)
    #cv2.imshow("Adaptive Threshold",adaptive_threshold)
	#cv2.imwrite(filename="saved_img-final.jpg",img=adaptive_threshold)
    #cv2.imshow("Adaptive Threshold 2",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return(text)

def OCR(get_image_path):
    a = get_image_path
    img=cv2.imread(os.path.join(a))
    text=GetImageOCR(img)
    final_path = Detect_Text_Image_Letter(img,get_image_path)
    return (text,final_path)

def Text_to_Audio(path):
    img=cv2.imread(path)
    height,width,_=img.shape

    #image show
    #cv2.imshow("Original Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #ocr
    url_api='https://api.ocr.space/parse/image'
    _,compressedimage=cv2.imencode(".jpeg",img,[1,90])

    file_bytes=io.BytesIO(compressedimage)

    result=requests.post(url_api,
                files={"new_img.png":file_bytes},
                data={"apikey":"d33ef54eba88957"})

    #print(result.content.decode())

    result=result.content.decode()
    result = json.loads(result)

    parsed_results = result.get("ParsedResults")[0]

    text_detected = parsed_results.get("ParsedText")
    #print(text_detected)
    import speech_recognition as spr
    from googletrans import Translator
    import os
    from gtts import gTTS
    import os

    #YOU HAVE TO GIVE THE LANGUAGE CODE IN WHICH THE TEXT IS TO LISTEN IN AUDIO 
    speak = gTTS(text=text_detected, lang='en', slow= False)
    n=len(path)
    f_type=""
    if(path[n-4] == '.' and path[n-3]=='p' and path[n-2]=='n' and path[n-1]=='g'):
        x = path.replace(".png", "")
        f_type=".png"
    if(path[n-5] == '.' and path[n-4] == 'j' and path[n-3]=='p' and path[n-2]=='e' and path[n-1]=='g'):
        x = path.replace(".jpeg", "")
        f_type=".jpeg"
    if(path[n-4] == '.' and path[n-3]=='j' and path[n-2]=='p' and path[n-1]=='g'):
        x = path.replace(".jpg", "")
        f_type=".jpg"
    final_path_str = x + "_english_output" + ".mp3"
    final_path_img = str(x) + "_final_output" + f_type
    speak.save(final_path_str)
    final_path_str = final_path_str.replace("OCR_detection/","/")
    final_path_img = final_path_img.replace("OCR_detection/","/")
    #print(final_path_str)
    #print(final_path_img)
    return text_detected,final_path_str,final_path_img

def Language_Translator(path,Lgn):
    img=cv2.imread(os.path.join(path))
    height,width,_=img.shape
    #image show
    #cv2.imshow("Original Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    url_api='https://api.ocr.space/parse/image'
    _,compressedimage=cv2.imencode(".jpg",img,[1,90])
    file_bytes=io.BytesIO(compressedimage)
    lang='ger'
    result=requests.post(url_api,
                files={"german.jpg":file_bytes},
                data={"apikey":"d33ef54eba88957",
                    "language":lang})
    #print(result.content.decode())
    result=result.content.decode()
    result = json.loads(result)
    parsed_results = result.get("ParsedResults")[0]
    text_detected = parsed_results.get("ParsedText")
    #print(text_detected)
    translator = Translator()
    text__=translator.translate(text=text_detected,src='de',dest=Lgn)
    #BELOW A DICTIONARY IS PRINTED
    #print(text__)
    #TO ONLY EXTRACT TEXT FROM THE ABOVE DICTIONARY
    y=text__.text
    #print(y)
    return y

def Get_Languages():
    return(googletrans.LANGUAGES)

def Generate_Audio_Only(text):
    speak = gTTS(text=text, lang='en', slow= False)
    path = "OCR_detection/static/Generated_Audio/audio_generated.mp3"
    speak.save(path)
    path = path.replace("OCR_detection/","/")
    return path

def Generate_Audio_Using_Text_and_Lang(text,lang):
    speak = gTTS(text=text, lang='en', slow= False)
    path = "OCR_detection/static/Generated_Audio/audio_generated.mp3"
    speak.save(path)
    path = path.replace("OCR_detection/","/")
    return path

def Language_Translator_With_Text(text,Lgn):
    translator = Translator()
    text__=translator.translate(text=text,src='en',dest=Lgn)
    y=text__.text
    #print(y)
    return y

def PDF_to_DOC(path_of_pdf):
    from pdf2docx import parse
    pdf_file = path_of_pdf
    docx_file = path_of_pdf.replace(".pdf","")+"_final_output.docx"
    parse(pdf_file, docx_file, start=0, end=1)
    doc_path = str(docx_file).replace("OCR_detection/","/")
    return doc_path

def DOCX_to_PDF(path_of_doc):
    from docx2pdf import convert
    docx_file = path_of_doc
    pdf_file = path_of_doc.replace(".docx","")+"_final_output.pdf"
    convert(docx_file ,pdf_file)
    pdf_path = str(pdf_file).replace("OCR_detection/","/")
    return pdf_path

def conversion(img,file_type):  
    resized = img
    filename = 'output_compress'+ file_type
    img_resized = cv2.imwrite(filename=filename, img=resized)


def getInputType(ip):
    n = len(ip)
    filename = ""
    if(ip[n-4]=="." and ip[n-3]=="p" and ip[n-2]=="n" and ip[n-1]=="g"):
        filename = ".png"
    elif(ip[n-4]=="j" and ip[n-3]=="p" and ip[n-2]=="e" and ip[n-1]=="g"):
        filename = ".jpeg"
    elif(ip[n-4]=="." and ip[n-3]=="j" and ip[n-2]=="p" and ip[n-1]=="g"):
        filename = ".jpg"
    return filename

def convert_image(input_path,file_type):
    img=cv2.imread(os.path.join(input_path)) 
    if(file_type=="grayscale"):
        filename = "OCR_detection/static/converted_img/output" + getInputType(input_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY ) 
    elif(file_type=="black"):
        filename = "OCR_detection/static/converted_img/output" + getInputType(input_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY ) 
        (thresh, img) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    else:
        filename = "OCR_detection/static/converted_img/output" + file_type
    cv2.imwrite(filename=filename, img=img)
    output_path = filename.replace("OCR_detection/","/")
    return output_path

def compress_img(input_path,scale): 
    img=cv2.imread(os.path.join(input_path)) 
    scale = int(scale)   
    width = int(img.shape[1] * scale / 100)  
    height = int(img.shape[0] * scale / 100)  
    dim = (width, height)  

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) 
    filename = "OCR_detection/static/compressed_img/output" + getInputType(input_path)
    cv2.imwrite(filename=filename, img=resized)
    output_path = filename.replace("OCR_detection/","/")
    compressed_size = os.path.getsize(filename)
    return output_path,compressed_size
