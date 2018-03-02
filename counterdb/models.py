from django.db import models
import hashlib
import hmac

# Create your models here.
class Task(models.Model):
    hash=models.CharField(max_length=1000,null='False', blank='False', verbose_name='hash')
    job=models.CharField(max_length=1000,null='False', blank='False', verbose_name='job')
    strm=models.DateTimeField(auto_now=False, auto_now_add=False)
    endm=models.DateTimeField(auto_now=False, auto_now_add=False)
    version=models.CharField(max_length=1000,null='False', blank='False', verbose_name='version')
    status= models.BooleanField(verbose_name='Статус')
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.id 
class Syst_stand (models.Model):
    syst  = models.CharField(max_length=1000,null='False', blank='False', verbose_name='Система')
    stand = models.CharField(max_length=1000,null='False', blank='False', verbose_name='Стенд')
    tested= models.BooleanField(verbose_name='Тестирование')
    thash = models.CharField(max_length=1000,null='False', blank='True', verbose_name='Хеш')
    def _thash(self):
         st=bytearray(self.syst+self.stand,'UTF8')
         hs=hashlib.sha1(st).hexdigest()
         return hs
    
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.id )
    def save(self, *args, **kwargs):
        self.thash=self._thash()
        super().save(*args, **kwargs)
       # return super(Syst_stand, self).save(*args, **kwargs)