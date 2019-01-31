from django.db import models
from django.urls import reverse

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        # 객체를 출력할 때 나타날 값
        return "이름 : "+self.site_name + ", 주소 : " + self.url


    #Todo : get_absolute_url method


    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


    class Meta:
        ordering = ['site_name']


#모델의 냉숑을 데이토베이스 반영
#두가지 명령어를 이용해서 -> python manage.py makemigrations migrate

