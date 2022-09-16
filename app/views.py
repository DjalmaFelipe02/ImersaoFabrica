from multiprocessing import context
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import StudentForm
from .models import Student
from .filters import StudentFilter

def student_page(request):
    queryset=Student.objects.all()

    filter_students = StudentFilter(request.GET, queryset)

    pagineted_filter_students = Paginator(filter_students.qs, 4)
    page_number = request.GET.get('page')
    student_page_obj = pagineted_filter_students.get_page(page_number)

    context = {                                  
        'filter_students': filter_students,
        'student_page_obj': student_page_obj       
    }

    return render(request, 'home.html', context)    

def register_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('student_filters')

    context ={'form': form}    

    return render(request, 'student-form.html', context)

def update_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('student_filters')

    context={
        'form': form, 
        'student': student
    }

    return render(request, 'update-student.html', context)

def delete_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_filters')

    context={ 'student': student }

    return render(request, 'delete-confirm.html', context)