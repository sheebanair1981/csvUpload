from django.core.files import File
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient, APITestCase
import os


class UploadTest(APITestCase):
    client_class = APIClient

    def test_csvUpload(self):
        pathfile = os.path.join(settings.BASE_DIR,"test.csv")
        data = File(open(pathfile, 'rb'))
        file = SimpleUploadedFile(pathfile, data.read(), content_type="text/csv")
        params = {"file_csv": file}
        response = self.client.post("http://127.0.0.1/api/", params, format="multipart")
        self.assertEqual(response.status_code, 201)



