from django.core.management import BaseCommand, CommandError
from cafe.models import Order, OrderItem


class Command(BaseCommand):
    help = 'Creating data for a database'

    def handle(self, *args, **options):
        # Creating items
        items = [
            {
                'name': 'Солянка сборная мясная',
                'price': 260.00
            },
            {
                'name': 'Окрошка на квасе',
                'price': 200.00
            },
            {
                'name': 'Гречневая каша с грибами и луком',
                'price': 199.00
            }
        ]
        new_items = []
        for item in items:
            try:
                new_item, created = OrderItem.objects.get_or_create(**item)
                if created:
                    self.stdout.write(f'Блюдо {new_item.name} создано!')
                new_items.append(new_item)
            except:
                raise CommandError('Не получилось создать блюда с ценами!')
            
        self.stdout.write(self.style.SUCCESS('Блюда созданы успешно!'))    
        
        # Creating orders
        first, second, third = new_items

        try:
            new_order, created = Order.objects.get_or_create(table_number=1)
            if created:
                new_order.items.set((first, second))
                self.stdout.write(f'{new_order} создан!')
        except:
            raise CommandError('Не получилось создать заказ!')
        
        try:
            new_order, created = Order.objects.get_or_create(table_number=2)
            if created:
                new_order.items.set((second))
                self.stdout.write(f'{new_order} создан!')
        except:
            raise CommandError('Не получилось создать заказ!')
        
        try:
            new_order, created = Order.objects.get_or_create(table_number=3)
            if created:
                new_order.items.set((first, second, third))
                self.stdout.write(f'{new_order} создан!')
        except:
            raise CommandError('Не получилось создать заказ!')

        self.stdout.write(self.style.SUCCESS('Заказы созданы успешно!')) 
        