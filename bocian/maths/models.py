from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

OPERATION_CHOICES = (
    ("add", "Add"),
    ("sub", "Sub"),
    ("div", "Div"),
    ("mul", "Mul")
)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("categories")

class Math(models.Model):
    operation = models.CharField(max_length=10, choices=OPERATION_CHOICES)  # w bazie to będzie varchar
    a = models.IntegerField()
    b = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    result = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="maths")

    def __str__(self):
        return f"Math {self.operation} | {self.a} | {self.b}"



