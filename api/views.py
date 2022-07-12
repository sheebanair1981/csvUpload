from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import FileDetail
from .serializers import FileSerializer
from django.conf import settings
import pandas as pd
import json

class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  #Handling POST data

  def post(self, request, *args, **kwargs):
    try:
      csvFile = request.FILES["file_csv"]
    except:
      return Response({"detail":"File Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if not csvFile.name.endswith('.csv'):
        return Response({"detail":"Not a csv File"}, status=status.HTTP_404_NOT_FOUND)
    else:
        #serializing data
        file_serializer = FileSerializer(data=request.data)
        
        if file_serializer.is_valid():
          fileId = file_serializer.save()
          file_name = fileId.file_csv
          pathfile = settings.MEDIA_ROOT + "/" + str(file_name)
          try:
            file_data = pd.read_csv(pathfile)
          except:
            return Response({"detail":"File Not Readable"}, status=status.HTTP_404_NOT_FOUND)
          else:  
            
            #Parsing Columns and finding Data Types
            responseData = {}
            for name, dtype in file_data.dtypes.iteritems():
                    if dtype =='int64' or dtype =='float64':
                        responseData[name] = "NUMBER"
                    elif dtype == 'datetime64':
                        responseData[name] = "DATETIME"
                    elif dtype == "object" and 'DATE' in str(name).upper():
                        responseData[name]="DATETIME"
                    else:
                        responseData[name]="TEXT" 
            
            #update database
            record = FileDetail.objects.get(pk=fileId.id)
            record.file_csv = file_name
            record.file_path = pathfile
            record.file_columns = json.dumps(responseData)
            record.save()

            data = request.data
            file_serializer = FileSerializer(record,data=data)
            if file_serializer.is_valid():
              return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
              return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)