from django.db import models

# Create your models here.


class Bookmark(models.Model):
	title = models.CharField(max_length = 100, blank=True, null=True)
	url = models.URLField('url', unique=True)	#url컬럼에대한 레이블 문구.

	def __str__(self):	#객체를 문자열로 표현할때 사용하는 함수
		return self.title
