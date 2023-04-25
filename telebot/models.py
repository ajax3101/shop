from django.db import models


class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=50, verbose_name='�����')
    tg_chat = models.CharField(max_length=50, verbose_name='��� id')
    tg_message = models.TextField(verbose_name='�����������')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = '������������'
        verbose_name_plural = '������������'
