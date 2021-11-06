from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.caption}"


class Post(models.Model):
    title = models.CharField(max_length=128)
    excerpt = models.CharField(max_length=256)
    image_name = models.CharField(max_length=128)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    # by default db_index is set
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(20)])
    author = models.ForeignKey(
        Author, null=True, on_delete=models.SET_NULL, related_name="posts")

    tags = models.ManyToManyField(Tag)
