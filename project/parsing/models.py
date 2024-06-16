from django.db import models
from shops.models import Shop


class ParsingSetting(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField()
    parsing_args = models.JSONField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
