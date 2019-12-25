from django.db import models



class Enquiry(models.Model):
    
    name=models.CharField(max_length=500)
    email=models.EmailField(max_length=300)
    message =  models.TextField(max_length=2000,null=True) 
 
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name