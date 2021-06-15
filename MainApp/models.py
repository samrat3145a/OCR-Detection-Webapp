from django.db import models

class ImageSave(models.Model):
    upload = models.ImageField(upload_to="OCR_detection/static/new_img")
    user_id = models.IntegerField(default=None)

    class Meta:
        db_table = "Image Upload"

class PdfSave(models.Model):
    upload_pdf = models.FileField(upload_to="OCR_detection/static/new_pdf")
    user_id = models.IntegerField(default=None)

    class Meta:
        db_table = "Docx Upload"
        
class DocxSave(models.Model):
    upload_docx = models.FileField(upload_to="OCR_detection/static/new_docx")
    user_id = models.IntegerField(default=None)

    class Meta:
        db_table = "Pdf Upload"
