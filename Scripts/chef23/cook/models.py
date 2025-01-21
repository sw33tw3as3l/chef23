from django.db import models
from django.contrib.auth.models import User
import json
from django.utils import timezone

# Create your models here.

class GraphProject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    is_public = models.BooleanField(default=False)
    edge = models.CharField(max_length=100000, default='')
    vertex = models.CharField(max_length=100000, default='')
    pub_date = models.DateTimeField(default=timezone.now)

    @property
    def vertex_list(self):
        nodes = self.vertex.split('-')

        return nodes
    
    @property
    def edge_list(self):
        data = json.loads(self.edges)
        return data
    
    def __str__(self):
        return self.project_name
    