from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class School(models.Model):
    # fields for school

    name = models.CharField(max_length=50)
    principal = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cbvapp:detail', kwargs={'pk':self.pk})

class Student(models.Model):
    # fields for students
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    school = models.ForeignKey('School', related_name="students")

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('index')
