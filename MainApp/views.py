from django.shortcuts import render,redirect
from MainApp.forms import ImageUpload
from MainApp.models import ImageSave
from MainApp.OCR_ALGORITHM import *

from MainApp.forms import ImageUpload,SignupForm,PdfUpload ,DocxUpload
from MainApp.models import ImageSave,PdfSave,DocxSave

from django.contrib import messages, auth
from django.utils.html import strip_tags
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection

def index(request):
    if request.method == "POST":
        form = ImageUpload(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image Successfully Uploaded !')
            return redirect('index')
        else:
            print(form.errors)
    form = ImageUpload(request.POST)
    latest_image = ImageSave.objects.last()
    context={'form':form,'image':latest_image}
    return render(request,'index.html',context)

def home(request):
    return render(request,'home.html')
	
def output(request):
    latest_image = ImageSave.objects.last()
    text,final_path_img = OCR(str(latest_image.upload))
    context={'image':latest_image,'text':text,'final_path_img':final_path_img}
    return render(request,'output.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have successfully login!')
            return redirect('index')
        else:
            messages.success(request, ' Error Logging In / Please try again !')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            x=form.errors.as_json
            print(x)
            messages.success(request,'Please enter the Valid Details!')
            return redirect('register')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('login')

def generate_audio(request):
    if request.method == 'POST':
        latest_image = ImageSave.objects.last()
        # print(str(latest_image.upload))
        text,final_path,final_path_img = Text_to_Audio(str(latest_image.upload))
        messages.success(request, 'Audio Generated Successfully !')
        context={'image':latest_image,'text':text,'final_path':final_path,'final_path_img':final_path_img }
        return render(request,'output.html',context)
    return redirect('output')

def translate_language(request):
    latest_image = ImageSave.objects.last()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")
    print(latest_image)
    text,final_path_img = OCR(str(latest_image.upload))
    languages = Get_Languages()
    if request.method == "GET":
        language = request.GET.get('language')
        if(language):
            y = Language_Translator(str(latest_image.upload),language)
            languages = Get_Languages()
            context={'image':latest_image,'text':text,'final_path_img':final_path_img,'y':y,
                    'languages':languages,'lng':language}
            return render(request,'translate_language.html',context)
    if request.method == "POST":
        original_text = request.POST.get('textarea1')
        translated_text = request.POST.get('textarea2')
        language1 = request.POST.get('Lang')
        if str(original_text) != "None":
            path_of_audio_file = Generate_Audio_Only(str(original_text))
            context={'image':latest_image,'text':text,'languages':languages,'lng':language1,'path_of_original_audio': path_of_audio_file}
            return render(request,'translate_language.html',context)
        if str(translated_text) != "None":
            if language1:
                print(language1)
                path_of_audio_file = Generate_Audio_Using_Text_and_Lang(str(translated_text),language1)
                context={'image':latest_image,'text':text,'languages':languages,
                    'path_of_translated_audio': path_of_audio_file,'y':translated_text,'lng':language1}
                return render(request,'translate_language.html',context)
            else :
                messages.error(request, 'Language not Selected! Please Select Again !')
    context={'image':latest_image,'text':text,'languages':languages}
    return render(request,'translate_language.html',context)
    
    
def generate_audio_from_text(request):
    languages = Get_Languages()
    if request.method == "POST":
        text = request.POST.get('textarea1')
        language = request.POST.get('language')
        if language:
            translated_text = Language_Translator_With_Text(str(text),language)
            path_of_audio_file = Generate_Audio_Using_Text_and_Lang(str(text),language)
            context={'path':path_of_audio_file,'languages':languages,
                    'translated_text':translated_text,'language':language}
            return render(request,'generate_audio_from_text.html',context)
    if request.method == "GET":
        text = request.GET.get('textarea2')
        language = request.GET.get('language')
        path_of_audio_file = Generate_Audio_Using_Text_and_Lang(str(text),language)
        context={'text':text,'languages':languages,'path_of_translated_audio': path_of_audio_file,
                'translated_text':text}
        return render(request,'generate_audio_from_text.html',context)
    context={'languages':languages}
    return render(request,'generate_audio_from_text.html',context)

def Doc_to_Pdf(request):
    if request.method == "POST":
        form2 = DocxUpload(request.POST or None,request.FILES or None)
        form = PdfUpload(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            latest_file = PdfSave.objects.last()
            print(str(latest_file.upload_pdf))
            path_of_doc = PDF_to_DOC(str(latest_file.upload_pdf))
            print(path_of_doc)
            messages.success(request, 'File Successfully Converted to Docx !')
            context={'form':form,'file':latest_file,'path_of_doc':path_of_doc}
            return render(request,'doc2pdf.html',context)
        elif form2.is_valid():
            form2.save()
            latest_file = DocxSave.objects.last()
            print(str(latest_file.upload_docx))
            path_of_pdf = DOCX_to_PDF(str(latest_file.upload_docx))
            print(path_of_pdf)
            messages.success(request, 'File Successfully Converted to Pdf !')
            context={'form':form,'file':latest_file,'path_of_pdf':path_of_pdf}
            return render(request,'doc2pdf.html',context)
        else:
            print(form.errors)
    return render(request,'doc2pdf.html')

def image_conversion(request):
    if request.method == "GET":
        latest_image = ImageSave.objects.last()
        file_type = request.GET.get('file_type')
        print(file_type)
        if(file_type):
            output_path = convert_image(str(latest_image.upload),file_type)
            messages.success(request, 'Image Successfully Converted !')
            context={'output_image':output_path}
            return render(request,'image_conversion.html',context)
    if request.method == "POST":
        form = ImageUpload(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image Successfully Uploaded !')
            latest_image = ImageSave.objects.last()
            context={'input_image':latest_image}
            return render(request,'image_conversion.html',context)
        else:
            print(form.errors)
    return render(request,'image_conversion.html')