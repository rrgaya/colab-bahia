from os import terminal_size
from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    create_at = models.DateField(auto_created=True, auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)

class SubCategory(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)

class Post(BaseModel):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    support_case = models.PositiveIntegerField()

    def __str__(self) -> str:
        return str(self.title)
