from django.db import models

# Create your models here.

class Destination(models.Model):

    name = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)


class News(models.Model):

    postname = models.CharField(max_length = 200)
    postimage = models.ImageField(upload_to='pics')
    postdesc = models.TextField()
    postcatagoty = models.TextField()
    date = models.IntegerField()
    month = models.CharField(max_length = 30)

class Destination_individual(models.Model):

    name = models.ForeignKey(Destination, to_field='name', on_delete=models.CASCADE, default = '')
    about_the_city = models.TextField(default='')
    img = models.ImageField(upload_to='pics_indiavidual')
    caption = models.CharField(max_length=100)
    img2 = models.ImageField(upload_to='pics_indiavidual')
    caption2 = models.CharField(max_length=100)
    img3 = models.ImageField(upload_to='pics_indiavidual')
    caption3 = models.CharField(max_length=100)
    img4 = models.ImageField(upload_to='pics_indiavidual')
    caption4 = models.CharField(max_length=100)
    img5 = models.ImageField(upload_to='pics_indiavidual')
    caption5 = models.CharField(max_length=100)

class Destination_indi(models.Model):
    pass
