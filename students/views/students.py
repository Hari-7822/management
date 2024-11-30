from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

from students.models import Student 
from students.models import user 
from students.forms import StudentForm

@login_required(login_url="user/login/")
def index(request):
    list = user.objects.all()
    # print(request.user)
    return render(request, 'list.j2', {'user': list,'meta': meta})

@login_required(login_url="user/login")
def info(request):
    return "Info"

@login_required(login_url="user/login")
def perms(request):
    return "Info"

@login_required(login_url="user/login")
def settings(request):
    return "Info"

def Add_Student(request):
    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            stu = form.cleaned_data['name']
            form.save()
            print(stu)
            messages.success(request, f"Student {stu} is added successfully") if form.save() else messages.error(request, f"Student not added");form=StudentForm(request.POST)
            return redirect("list/")
    else:
        form = StudentForm()

    return render(request, 'forms/student.j2', {'form':form})

# def Edit_Student(request):
#     if request.method == "POST":
#         form=StudentForm(request.POST)
#         if form.is_valid():
#             if not Student.objects.filter(id = form.cleaned_data['roll_number']):
#                 form.save()
#             else:
#                 messages.error(request, f'Roll number {id} already exists!')
#                 # form=StudentForm(request.POST)
#     else:
#         form = StudentForm()
#     return render(request, 'forms/student.j2', {'form':form})


# def View_Student(request, *input):
#     query=get_object_or_404(Student, username=input.name, id=input.id)
#     return render(request, 'student_view.j2', {'data':query})


# def PrintStudent(request, *input):
#     query = get_object_or_404(Student, id= input.id, username= input.name)
#     return render(request, 'print.j2', {'data':query})