from django.db import models

# Create your models here.


class Product_Type(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f"{self.title}"


class Product(models.Model):
    # class Meta:
    # 	verbose_name_plural = 'All Product'
    slug = models.SlugField(unique=True, max_length=100)
    title = models.CharField(max_length=225)
    type = models.ForeignKey(
        "app_product.Product_Type", on_delete=models.CASCADE, null=True
    )
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    special_price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    is_premium = models.BooleanField(default=False)
    promotion_end = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    photo = models.ImageField(
        default="default.png", upload_to="image_product", blank=True, null=True
    )
    def __str__(self) -> str:
    	return f'{self.title}'
