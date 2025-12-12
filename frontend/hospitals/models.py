from django.db import models
import uuid

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    batch_id = models.UUIDField(default=uuid.uuid4, db_index=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
