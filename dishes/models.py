from django.db import models

class SVGFile(models.Model):
    svg_file = models.FileField(upload_to='svg_files/')

    def __str__(self):
        return self.svg_file.name


class Category(models.Model):
    title = models.CharField(max_length=100)

class Dish(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    weight = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    svgs = models.ManyToManyField(SVGFile)