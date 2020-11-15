import logging
from django.db import models

# Create your models here.
logger = logging.getLogger(__name__)



class BaseModel(models.Model):
    """
    Abstract Model .
    """

created_at = models.DateTimeField(auto_now_add=True, db_index=True)

updated_at = models.DateTimeField(auto_now=True)

class Meta:
    abstract = True

