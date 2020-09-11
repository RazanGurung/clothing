from django.db import models

class Client(models.Model):
	C_Id= models.AutoField(auto_created=True, primary_key=True)
	Name= models.CharField(max_length=50)
	Email= models.CharField(max_length=50)
	Phone=models.IntegerField()
	Code=models.IntegerField()
	password=models.CharField(max_length=50)
	dob=models.DateField()
	gender= models.CharField(max_length=10)

	class Meta:
		db_table = "client_table"
