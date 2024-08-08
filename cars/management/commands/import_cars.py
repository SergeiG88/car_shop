import json
from django.core.management.base import BaseCommand
from cars.models import Car

class Command(BaseCommand):
    help = 'Import cars data from JSON file'

    def handle(self, *args, **kwargs):
        with open('data/cars.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                features = json.dumps(item['features'])
                Car.objects.update_or_create(
                    id=item['id'],
                    defaults={
                        'make': item['make'],
                        'model': item['model'],
                        'year': item['year'],
                        'price': item['price'],
                        'description': item['description'],
                        'features': features,
                        'image': item['image']
                    }
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported cars data'))

