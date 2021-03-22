from django.conf.urls import url
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url('output/', views.output, name="output"),
    url('index/', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('Output_1/generate_audio/', views.generate_audio, name="generate_audio"),
    url('translate_language/', views.translate_language, name="translate_language"),
    url('image_conversion/', views.image_conversion, name="image_conversion"),
    url('generate_audio_from_text/', views.generate_audio_from_text, name="generate_audio_from_text"),
    url('Doc_to_Pdf/', views.Doc_to_Pdf, name="Doc_to_Pdf"),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
