from django.db import models


# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Review(models.Model):

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"

    text = models.TextField()
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
