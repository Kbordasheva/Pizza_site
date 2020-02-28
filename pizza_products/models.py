from django.db import models


class PizzaProduct(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='pizzas_images/', default="default image")

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"

