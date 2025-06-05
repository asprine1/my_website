
from django.db import models
from django.utils import timezone

# Create your models here.
class Daily(models.Model):
    today_topic = models.CharField(max_length=30)
    topic_description = models.CharField(max_length= 150)
    created_at = models.DateTimeField(default = timezone.now) #auto_now_add=True

    def __str__(self):
        return "%s %s" %(self.today_topic, self.created_at)



