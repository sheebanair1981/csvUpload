from django.db import models
from django.core.files.storage import FileSystemStorage

#To avoid changing file names by django
class CustomStorage(FileSystemStorage):
        def get_valid_name(self, name):
            # return get_valid_filename(name)
            return name

#Model for saving File Details
class FileDetail(models.Model):
    file_csv = models.FileField(blank=False, null=False,storage=CustomStorage())
    file_path = models.CharField(max_length=255,blank =True)
    file_columns = models.TextField(blank=True)

    def __str__(self):
        return str(self.file_csv)
