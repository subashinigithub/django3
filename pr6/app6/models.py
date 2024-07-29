from django.db import models
class Item(models.Model):
    category=models.CharField(max_length=225)
    subcategory=models.CharField(max_length=225)
    name=models.CharField(max_length=225)
    amount=models.PositiveIntegerField(null=True)
    ratings=models.BooleanField(null=True)




    def __str__(self) ->str:
        return self.name