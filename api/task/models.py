import uuid

from django.db import models
from core.models import User


STATUS = (
     ('APPROVED', "Approved"),
     ('PENDING', "Pending"),
     ('REJECTED', "Rejected"),
)

PRIORITY = (
     ('HIGH', 'High'),
     ('MEDIUM', 'Medium'),
     ('LOW', 'Low')
)

class Task(models.Model):
     id = models.UUIDField(
          primary_key=True,
          editable=False, 
          default=uuid.uuid4
     )
     title = models.CharField(max_length=255, null=False)
     description = models.TextField(null=False)
     priority = models.CharField(
          choices=PRIORITY, 
          default="Medium",
          max_length=50
     )
     tags = models.CharField(max_length=255, default='')
     lead_time = models.DateTimeField(auto_now=True)
     deadline = models.DateTimeField(auto_now=True)
     assign_details = models.ForeignKey(
          "task.AssignDetails", 
          on_delete=models.CASCADE, 
          related_name="assign_details",
          null=True
     )
     approval_request = models.BooleanField(
          default=False,
          max_length=5
     )
     created = models.DateTimeField(
          auto_now_add=True, 
          editable=True
     )
     updated = models.DateTimeField(
          auto_now=True, 
          editable=True
     )

     def __str__(self):
          return self.title

class AssignDetails(models.Model):
     id = models.UUIDField(
          primary_key=True,
          editable=False, 
          default=uuid.uuid4
     )
     assignee = models.ForeignKey(
          "core.User",
          on_delete=models.CASCADE, 
          related_name="assignee",
     )
     assignor = models.ForeignKey(
          'core.User', 
          on_delete=models.CASCADE, 
          related_name="assignor_admin"
     )
     status = models.CharField(
          max_length=50,
          choices=STATUS, 
          default="Pending"
     )
     status_update = models.DateTimeField(
          auto_now=True, 
          editable=True
     )

     def __str__(self):
          return f"{str(self.assignee.email)}-{self.id}"
