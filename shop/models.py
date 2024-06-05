from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to="articles/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Profile(models.Model):
    phone = models.CharField(max_length=255, default="")
    mobile = models.CharField(max_length=255, default="")
    address = models.CharField(max_length=255, default="")
    job = models.CharField(max_length=255, default="")
    image = models.ImageField(upload_to="profiles/",
                              null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name="Comment")

    def __str__(self):
        return self.author.username


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f'Корзина для: {self.user.username} | Продукт: {self.article.title}'

    def sum(self):
        return self.article.price * self.quantity


class Favorites(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    articles = models.ForeignKey(to=Article, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'articles')

    def __str__(self):
        return f"{self.user.first_name} - {self.articles.title}"