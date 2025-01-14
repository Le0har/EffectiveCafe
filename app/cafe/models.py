from django.db import models


STATUS = (
    ('waiting', 'в ожидании'),
    ('paid', 'оплачено'),
    ('ready', 'готово'),
)


class OrderItem(models.Model):
    name = models.CharField(unique=True, verbose_name='Название')
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name


class Order(models.Model):
    table_number = models.IntegerField(verbose_name='Номер стола')
    items = models.ManyToManyField(OrderItem, related_name='orders', verbose_name='Блюда')
    # total_price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    status = models.CharField(default='waiting', choices=STATUS, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ для стола # {self.table_number}'

    