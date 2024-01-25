from django.shortcuts import render
from django.http import HttpResponse
from .models import studentdatas


# Create your views here.
def home(request):
  return render(request,'home.html')

def login(request):
  return render(request,'login.html')

def insert(request):
  if request.method=='POST':
    student_id=request.POST['student_id']
    student_name=request.POST['student_name']
    student_year=request.POST['student_year']
    student_sports=request.POST['student_sports']

    obj=studentdatas()
    obj.stu_id=student_id
    obj.stu_name=student_name
    obj.stu_year=student_year
    obj.stu_sport=student_sports
    obj.save()
  return render(request,'insert.html')

def delete(request):
  return render(request,'delete.html')

def display(request):
  return render(request,'display.html')
