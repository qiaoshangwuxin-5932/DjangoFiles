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
    username = models.CharField(max_length=20,blank=False,null=False,unique=True,verbose_name="用户名字")
    photo = models.ImageField(upload_to="image",null=True,db_index=True)
    def __unicode__(self):
        return self.username
    class Meta:
        db_table = 'rnew'
        verbose_name = "Rnews"
        verbose_name_plural = verbose_name



# class Data(models.Model):
#     pass
#     choice = (
#         ('A','A:我'),
#         ('B','B:你'),  # 四个选项
#         ('C','C:他'),
#         ('D','D:她'),
#     )
#     content = models.TextField(verbose_name='text文字')
#     answer = models.CharField(max_length=1,choice=choice,)
#     class Meta:
#         db_table = 'data'
#         verbose_name = 'data'
#         verbose_name_plural = verbose_name


