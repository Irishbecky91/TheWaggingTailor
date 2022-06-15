from django.db import models
from django.contrib.auth.models import User


# Create your models here.
QUERY_CHOICES = {
    ('QUOTE', 'Request A Quote'),
    ('QUERY', 'Ask A Question'),
}


class Query(models.Model):
    """
    Quote Model
    """
    name = models.CharField(max_length=254)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30, blank=True)
    query_type = models.CharField(max_length=20, choices=QUERY_CHOICES)
    description = models.TextField()
    query_date = models.DateField(auto_now_add=True)
    query_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
