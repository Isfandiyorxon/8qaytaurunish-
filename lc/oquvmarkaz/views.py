from django.shortcuts import render
from .models import Curs,Lesson
from django.shortcuts import render, get_object_or_404,redirect
from .forms import forms,LesonForm

# Create your views here.
def home(request):
    curs=Curs.objects.all()
    lesons=Lesson.objects.all()
    return render(request,'index.html',{'curs':curs,'lesons':lesons})

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'kurslar.html', {'lesson': lesson})

def lesson_to_curse(request, pk):
    leson = Lesson.objects.filter(pk=pk)
    curs = Curs.objects.all()
    context = {'leson': leson, 'curs': curs}
    return render(request, 'index.html', context)

    return render(request,'index.html',context)
# def home(request):
#     curs = Curs.objects.all()  # Barcha Curs obyektlarini olish
#     lesson = Lesson.objects.all()  # Barcha Lesson obyektlarini olish
#     return render(request, 'index.html', {'curs': curs, 'lesson': lesson})

def add_lesson(request):
    if request.method=='POST':
        forms=LesonForm(data=request.POST,files=request.FILES)
        if forms.is_valid():
            leson=forms.create()
            return redirect('lesson_detail',pk=leson.pk)
    else:
            forms=LesonForm()
    contex={
                'forms':forms
            }
    return render(request,'add_leson.html',contex)
