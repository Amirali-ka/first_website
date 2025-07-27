from django.db import models

# Create your models here.
class post (models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    status=models.BooleanField(default=0)
def __str__(self):
    return self.id
    #return '{}_{}'.format(self.name,self.id)
