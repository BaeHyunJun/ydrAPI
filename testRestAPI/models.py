from django.db import models

# Create your models here.
class testRestAPI(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Data(models.Model):
    specific_id = models.CharField('specific_id', max_length=156)
    horizon_width = models.CharField('horizon_width', max_length=100)
    vertical_width = models.CharField('vertical_width', max_length=100)
    x_location = models.CharField('x_location', max_length=100)
    y_location = models.CharField('y_location', max_length=100)

    def __str__(self):
        return str(self.specific_id)


class Calc(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    rate = models.FloatField()
    count = models.IntegerField()