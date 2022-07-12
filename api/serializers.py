from rest_framework import serializers
from .models import FileDetail

class FileSerializer(serializers.ModelSerializer):
  class Meta:
    model = FileDetail
    fields = ('id','file_csv','file_columns')