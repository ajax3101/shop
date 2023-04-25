from django.db import models


class StatusCRM(models.Model):
    status_name = models.CharField(max_length=100, verbose_name="назва статусу")


    def __str__(self) -> str:
        return self.status_name
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статуси'

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Ім\'я')
    order_form = models.CharField(max_length=20, verbose_name='Telefon')
    order_status = models.ForeignKey(StatusCRM, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self) -> str:
        return self.order_name
    
    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

class CommentCRM(models.Model):
    pass # add