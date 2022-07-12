	1. Clone Project: git clone https://github.com/sheebakv/csvUpload.git
	2. cd csvUpload
	3. Create Virtual Environment: pipenv shell (or use: python -m venv env and activate it using: source env/bin/activate
	4. pip install -r requirements.txt
	5. python manage.py makemigrations
	6. python manage.py migrate
	7. python manage.py runserver
	8. Open Postman app:
	9. Create a collection and enter http://127.0.0.1:8000/api/ in url field and set the method to POST which is at the left of the url field. Go to Body section and make sure that ‘form-data’ is checked.
	10. In the key field write 'file_csv’, which should match the name of your model's File field name. In this case, it is 'file_csv'. Then from the drop-down select ‘File’ instead of ‘Text’. In value field, browse the file and select it.
	11. Now click Send, your file will be uploaded and you will get the file data in response.
	12. If you want to see the database storage details through admin panel, do the following steps:
	13. Uncomment the commented lines from api/admin.py file.
	14. Run the command: python manage.py createsuperuser
	15. Access the admin panel using: http://127.0.0.1:8000/admin
	


