from django.db import models

class PriceCard(models.Model):
    pc_value = models.CharField(max_length=20, verbose_name='ціна')
    pc_description = models.CharField(max_length=200, verbose_name='Опис')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Ціни'
        verbose_name_plural = 'Ціни'

class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name='Послуга')
    pt_old_price = models.CharField(max_length=10, verbose_name='Стара ціна')
    pt_new_price = models.CharField(max_length=10, verbose_name='Нова ціна')

    def __str__(self) -> str:
        return self.name