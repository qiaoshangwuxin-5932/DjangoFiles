from django.db import models

# Create your models here.




#
class Slogan(models.Model):
    # choices = (
    #     ()
    # )
    slogan = models.CharField(max_length=30,null=True)
    def __unicode__(self):
        return self.slogan
    class Meta:
        db_table= 'Slogan'

class RecruitmentNews(models.Model):
    slogan = models.ForeignKey(Slogan,on_delete=models.SET,null=True)
    username = models.CharField(max_length=20,blank=False,null=False,unique=True)
    photo = models.ImageField(upload_to="image",null=True,db_index=True)
    def __unicode__(self):
        return self.username
    class Meta:
        db_table = 'rnew'
        verbose_name = "Rnews"
        verbose_name_plural = verbose_name





