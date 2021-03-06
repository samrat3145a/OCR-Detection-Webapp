from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from MainApp.forms import ImageUpload
from MainApp.models import ImageSave
from MainApp.OCR_ALGORITHM import *

from MainApp.forms import ImageUpload,SignupForm,PdfUpload ,DocxUpload
from MainApp.models import ImageSave,PdfSave,DocxSave

from django.contrib import messages, auth
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection

@login_required(login_url='login')
def index(request):
    current_user = request.user.id
    print(current_user)
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
    context={'form':form,'image':latest_image,"user_id":current_user}
    return render(request,'index.html',context)

@login_required(login_url='login')    
def upload_for_language_translator(request):
    current_user = request.user.id
    if request.method == "POST":
        form = ImageUpload(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image Successfully Uploaded !')
            return redirect('upload_for_language_translator')
        else:
            print(form.errors)
    form = ImageUpload(request.POST)
    latest_image = ImageSave.objects.last()
    context={'form':form,'image':latest_image,"user_id":current_user}
    return render(request,'upload_for_language_translator.html',context)


def home(request):
    return render(request,'home.html')

@login_required(login_url='login')	
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

@login_required(login_url='login')
def generate_audio(request):
    if request.method == 'POST':
        latest_image = ImageSave.objects.last()
        # print(str(latest_image.upload))
        text,final_path,final_path_img = Text_to_Audio(str(latest_image.upload))
        messages.success(request, 'Audio Generated Successfully !')
        context={'image':latest_image,'text':text,'final_path':final_path,'final_path_img':final_path_img }
        return render(request,'output.html',context)
    return redirect('output')

@login_required(login_url='login')
def translate_language(request):
    latest_image = ImageSave.objects.last()
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
                path_of_audio_file = Generate_Audio_Using_Text_and_Lang(str(translated_text),language1)
                context={'image':latest_image,'text':text,'languages':languages,
                    'path_of_translated_audio': path_of_audio_file,'y':translated_text,'lng':language1}
                return render(request,'translate_language.html',context)
            else :
                messages.error(request, 'Language not Selected! Please Select Again !')
    context={'image':latest_image,'text':text,'languages':languages}
    return render(request,'translate_language.html',context)
    
@login_required(login_url='login')   
def generate_audio_from_text(request):
    languages = Get_Languages()
    if request.method == "POST":
        text = request.POST.get('textarea1')
        language = request.POST.get('language')
        # print(text)
        # print(language)
        if language:
            original_audio = Generate_Audio_Using_Text_and_Lang_and_name("original_audio",str(text),'en')
            translated_text = Language_Translator_With_Text(str(text),language)
            translate_audio = Generate_Audio_Using_Text_and_Lang_and_name("translated_audio",str(translated_text),language)
            context={'path_of_original_audio':original_audio,'translated_text':translated_text,'language':language,'path_of_translated_audio': translate_audio,'messages':'Text Successfully Translated !!'}
            return JsonResponse(context)
    context={'languages':languages}
    return render(request,'generate_audio_from_text.html',context)

@login_required(login_url='login')
def Doc_to_Pdf(request):
    if request.method == "POST":
        form2 = DocxUpload(request.POST or None,request.FILES or None)
        form = PdfUpload(request.POST or None,request.FILES or None)
        if form.is_valid():
            print("444444444444444444")
            form.save()
            latest_file = PdfSave.objects.last()
            # print(str(latest_file.upload_pdf))
            path_of_doc = PDF_to_DOC(str(latest_file.upload_pdf))
            # print(path_of_doc)
            context={'path_of_doc':path_of_doc,"messages":"File Successfully Converted to Docx !"}
            return JsonResponse(context)

        elif form2.is_valid():
            form2.save()
            latest_file = DocxSave.objects.last()
            # print(str(latest_file.upload_docx))
            path_of_pdf = DOCX_to_PDF(str(latest_file.upload_docx))
            # print(path_of_pdf)
            context={'path_of_pdf':path_of_pdf,"messages":"File Successfully Converted to Pdf !"}
            return JsonResponse(context)
        else:
            print(form.errors)
    current_user = request.user.id
    context={"user_id":current_user}
    return render(request,'doc2pdf.html',context)

@login_required(login_url='login')
def image_conversion(request):
    current_user = request.user.id
    if request.method == "GET":
        latest_image = ImageSave.objects.last()
        file_type = request.GET.get('file_type')
        # print(file_type)
        if(file_type):
            output_path = convert_image(str(latest_image.upload),file_type)
            messages.success(request, 'Image Successfully Converted !')
            context={'output_image':output_path,'file_type':file_type,'user_id':current_user}
            return render(request,'image_conversion.html',context)
    if request.method == "POST":
        form = ImageUpload(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image Successfully Uploaded !')
            latest_image = ImageSave.objects.last()
            context={'input_image':latest_image,"user_id":current_user}
            return render(request,'image_conversion.html',context)
        else:
            print(form.errors)
    
    context={"user_id":current_user}
    return render(request,'image_conversion.html',context)

@login_required(login_url='login')
def compress_result(request):
    if request.method == 'GET':
        latest_image = ImageSave.objects.last()
        percentage = request.GET['value']
        if(percentage):
            output_path,compressed_size = compress_img(str(latest_image.upload),percentage)
            # messages.success(request, 'Image Successfully Compressed !')
            context={'output_image':output_path,'compressed_size':compressed_size,'messages':'Image Successfully Compressed !'}
            return JsonResponse(context)
    else:
        return HttpResponse("Request method is not a GET")

@login_required(login_url='login')            
def image_compression(request):
    if request.method == "POST":
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
        form = ImageUpload(data = request.POST , files=request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Image Successfully Uploaded !')
            latest_image = ImageSave.objects.last().upload
            image_size = os.path.getsize(str(latest_image))
            context={'input_image':str(latest_image),'image_size':image_size,'messages':'Image Successfully Uploaded !'}
            return JsonResponse(context)
        else:
            print(form.errors)
    current_user = request.user.id
    context={"user_id":current_user}
    return render(request,'image_compression.html',context)