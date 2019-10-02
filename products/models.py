from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    hunter = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    url = models.URLField(null=True, blank=True)
    pub_date = models.DateTimeField(null=True, blank=True)
    votes_total = models.IntegerField(default=1)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    icon = models.ImageField(upload_to='images/', null=True, blank=True)

    def summary(self):
        return self.body[:50]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
