from django.db import models
import json

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    features = models.TextField()
    image = models.ImageField(upload_to='cars/images/')

    def set_features(self, features):
        self.features = json.dumps(features)

    def get_features(self):
        return json.loads(self.features)
