from django.db import models


class Pablic(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    anons = models.CharField('Подзаголовок', max_length=250)
    full_text = models.TextField('Текст')
    date = models.DateTimeField('Публикация')


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/textsuit/{self.id}'


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
# Create your models here.
