from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_text = models.CharField(max_length=80)
    category = models.CharField(max_length=16)
    pub_date = models.DateTimeField('date created')

    def __str__(self):
      return self.todo_text
