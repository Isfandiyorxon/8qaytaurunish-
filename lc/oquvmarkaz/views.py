from django.shortcuts import render
from .models import Curs,Lesson
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home(request):
    curs=Curs.objects.all()
    lesons=Lesson.objects.all()
    return render(request,'index.html',{'curs':curs,'lesons':lesons})

def lesson_detail(request, id):
    lesson = get_object_or_404(Lesson, id=id)
    return render(request, 'kurslar.html', {'lesson': lesson})

def lesson_to_curse(request,pk):
    leson=get_object_or_404(Lesson,pk=pk)
    curs=Curs.objects.all()
    context= {'leson':leson,
     'curs':curs}
    return render(request,'home.html',context)
# def home(request):
#     curs = Curs.objects.all()  # Barcha Curs obyektlarini olish
#     lesson = Lesson.objects.all()  # Barcha Lesson obyektlarini olish
#     return render(request, 'index.html', {'curs': curs, 'lesson': lesson})