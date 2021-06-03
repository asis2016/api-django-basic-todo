import uuid
from django.db import models

class Todo(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title=models.CharField(max_length=100)
    body=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=models.DateTimeField(auto_now=True, blank=True)

    def __str__(self) -> str:
        return self.title