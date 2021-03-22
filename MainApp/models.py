from django.db import models

class ImageSave(models.Model):
    upload = models.ImageField(upload_to="OCR_detection/static/new_img")

    class Meta:
        db_table = "Image Upload"

class PdfSave(models.Model):
    upload_pdf = models.FileField(upload_to="OCR_detection/static/new_pdf")

    class Meta:
        db_table = "Docx Upload"
        
class DocxSave(models.Model):
    upload_docx = models.FileField(upload_to="OCR_detection/static/new_docx")

    class Meta:
        db_table = "Pdf Upload"

class SignupData(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    qualification = models.CharField(max_length=20)

    class Meta:
        db_table = "Signup Data"