from django.shortcuts import get_object_or_404, redirect, render

from .forms import studentform

from .models import students # type: ignore

# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')

def add_student(request):
    if request.method=="POST":
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_view')
    else:
        form=studentform()
    return render(request,'add_student.html',{'form':form})

def update_student(request,pk):
    student = get_object_or_404(students,pk=pk) # type: ignore
    if request.method=='POST':
        form=studentform(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_view')
    else:
        form=studentform(instance=student)
    return render(request,'add_student.html',{'form':form})

def delete_student(request,pk):
    student = get_object_or_404(students,pk=pk)
    if request.method=='POST':
        student.delete()
        return redirect('student_view')
    return render(request,'student_delete.html',{'student':student})

def student_view(request):
    student=students.objects.all()
    return render(request,'student_view.html',{'student':student})

def contact(request):
    return render(request,'contact.html')