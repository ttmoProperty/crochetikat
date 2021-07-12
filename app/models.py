from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    item_id = models.CharField(max_length=255, db_index=True)
    item_name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    item_image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('item_name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.item_name 

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])