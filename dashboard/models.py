from django.db import models

# class Person(models.Model):
#     messenger_id = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#
#
# class Complain(models.Model):
#     text = models.CharField(max_length=100)
#     latitude = models.CharField(max_length=50)
#     longitude = models.CharField(max_length=50)
#     upvotes = models.IntegerField(default=True, null=True)
#     category = models.CharField(max_length=50)
#     person = models.ForeignKey(Person, on_delete='cascade')