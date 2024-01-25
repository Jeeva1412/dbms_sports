from django.db import models

# Create your models here.
class studentdatas(models.Model):
  stu_id=models.IntegerField(default="")
  stu_name=models.CharField(max_length=20,default="")
  stu_year=models.IntegerField(default="")
  stu_sport=models.CharField(max_length=20,default="")


