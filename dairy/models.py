from django.db import models

# Create your models here.
class Daily(models.Model):
    today_topic = models.CharField(max_length=255)
    topic_description = models.CharField(max_length= 255)
