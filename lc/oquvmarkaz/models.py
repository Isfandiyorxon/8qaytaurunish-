from django.db import models

# Create your models here.

class Curs(models.Model):
    name=models.CharField(max_length=100,verbose_name='kurs nomi')
    def __str__(self):
        return self.name

class Lesson(models.Model):
    curs=models.ForeignKey(Curs,on_delete=models.CASCADE,verbose_name='kurs nomi')
    name=models.CharField(max_length=150,verbose_name='dars nomi')
    lesson=models.TextField(null=True,blank=True,verbose_name="darsning ma'lumotlari")
    def __str__(self):
        return self.name


