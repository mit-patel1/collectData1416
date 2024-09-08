from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserData(BaseModel):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(blank=True)
    description = models.CharField(max_length=1500, blank=True)
    dob = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name
        