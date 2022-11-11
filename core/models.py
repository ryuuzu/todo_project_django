import datetime
from django.db import models

# Create your models here.


def parse_duration(duration: int):
    minutes, seconds = divmod(duration, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    if duration > 0:
        leftText = "remaining"
    else:
        leftText = "late"

    if days > 0:
        return ('{} days {}'.format(days, leftText))
    if hours > 0:
        return ('{} hrs {}'.format(hours, leftText))
    if minutes > 0:
        return ('{} mins {}'.format(minutes, leftText))

    return ('{} secs {}'.format(seconds, leftText))


class Collection(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Todo(models.Model):
    STATUS = (("COMPLETED", "COMPLETED"), ("PENDING", "PENDING"))
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default="PENDING", choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE)

    @property
    def deadLine(self) -> str:
        if self.deadline is None:
            return ""
        return parse_duration(int((self.deadline - datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)).total_seconds()))

    def __str__(self):
        return self.title
