from django.db import models
class tasks(models.Model):
    taskname=models.CharField(max_length=400,verbose_name='Taskname',null=True,blank=True)
    def __str__(self):
        return (f'taskname: "{self.taskname}"')
    