from enum import unique
from django.db import models
from django.forms import CharField, SlugField

from users.models import User

from django.utils.timezone import now
from django.utils.text import slugify
from tinymce.models import HTMLField



class contrgrupp(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200,unique=True)
    guid = models.CharField(max_length=99,unique=True, verbose_name='guid')
    pusers=models.ManyToManyField(User,blank=True, related_name='users')
    
    class Meta:
        db_table = 'contrgrupp'
        verbose_name = 'Група контрагентів'
        verbose_name_plural = 'Групи контрагентів'

    def __str__(self):
        return self.name

  
class Priv(models.Model):
    grup=models.ForeignKey(contrgrupp, on_delete=models.CASCADE, verbose_name='Група')
    us=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Група')
    cod=models.CharField( max_length=150,verbose_name='cod')

    class Meta:
        db_table = 'priv'
        verbose_name = 'Група  - юзер'
        verbose_name_plural = 'Група  - юзер'

class Counterparts(models.Model):
    name = models.CharField(max_length=150,unique=True)
    full_name=models.CharField(blank=True,max_length=800,verbose_name='Повна назва')
    slug = models.SlugField(max_length=200,unique=True)
    adres=models.CharField(blank=True,max_length=800,verbose_name='Адреса')
    country=models.CharField(blank=True,max_length=100,verbose_name='Країна')
    city=models.CharField(blank=True,max_length=100,verbose_name='Місто')
    street=models.CharField(blank=True,max_length=300,verbose_name='Вулиця')
    number=models.CharField(blank=True,max_length=8,verbose_name='Номер будинку')
    letter=models.CharField(blank=True,max_length=2,verbose_name='Дріб')
    okpo_cod=models.CharField(blank=True,max_length=10,verbose_name='Код ЄДРПОУ')
    inn=models.CharField(blank=True,max_length=12,verbose_name='ІПН')
    director=models.CharField(blank=True,max_length=100,verbose_name='Керівник')
    phone=models.CharField(blank=True,max_length=100,verbose_name='Телефон')
    create_at = models.DateTimeField(blank=True,auto_now_add=True, verbose_name='Дата створення')
    group=models.ForeignKey(contrgrupp, on_delete=models.CASCADE, verbose_name='Група')
    guid = models.CharField(max_length=99,unique=True, verbose_name='guid')
    
    class Meta:
        db_table = 'counterpart'
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенти'
        
    def __str__(self):
        return self.name


class licenss(models.Model):
    guid = models.CharField(max_length=99,unique=True, verbose_name='guid')
    create_at = models.DateTimeField(blank=True,auto_now_add=True, verbose_name='Дата створення')
    data_po=models.DateTimeField(blank=True, verbose_name='Ліцензія діє по')
   # contragent=models.ForeignKey(Counterparts, on_delete=models.PROTECT, verbose_name='Контрагент')
    okpo=models.CharField(max_length=10, verbose_name='okpo')
    contragent = models.CharField(max_length=500, verbose_name='назва контрагента')
    link = models.URLField(max_length=500, verbose_name="посилання на акт")

    class Meta:
        db_table = 'licenss'
        verbose_name = 'Ліцензія'
        verbose_name_plural = 'Ліцензії'

class mg(models.Model):
    mg = models.CharField(max_length=500, verbose_name='mg')
    create_at = models.DateTimeField(blank=True,auto_now_add=True, verbose_name='Дата створення')
    okpo=models.CharField(max_length=10, verbose_name='okpo')
    contragent = models.CharField(max_length=500, verbose_name='назва контрагента')
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        db_table = 'mg'
        verbose_name = 'пов'
        verbose_name_plural = 'пов'

class Resume(models.Model):
    
    name = models.CharField(max_length= 255, blank=False, null=False)
    file = models.FileField(upload_to= 'files/',null=True)

    def __repr__(self):
        return 'Resume(%s, %s)' % (self.name, self.file)

    def __str__ (self):
        return self.name
    
    def save(self, *args, **kwargs):
      try:
        this = Resume.objects.get(id=self.id)
        if this.image != self.file:
              this.image.delete()
        
      except: pass
      super(Resume, self).save(*args, **kwargs)
        


    
    
    


