from django.contrib import admin
from .models import User, Authorization
from task.models import Task, AssignDetails
from django.contrib import admin
# from .forms import (
#      CustomUserChangeForm, 
#      CustomUserCreationForm
# )
# from django.contrib.auth.admin import UserAdmin 

class UserAdmin(admin.ModelAdmin):
     model = User 
     list_display = [
          'email', 'first_name', 'last_name', 
          'role', 'created', 'updated'
     ]
     exclude = [
          'username', 'groups', 'date_joined',
          'user_permissions', 'last_login'
     ]
     list_filter = ['role', 'created']  
     ordering = ['created']
     # form = CustomUserChangeForm
     # add_form = CustomUserCreationForm

class AuthorizationAdmin(admin.ModelAdmin):
     model = Authorization
     list_display = [
          'user_email', 'administrator', 'status', 
          'status_update'
     ]
     ordering = ['status_update']
     list_filter = ['status']

class TaskAdmin(admin.ModelAdmin):
     model = Task
     list_display = [
          'title', 'priority', 
          'lead_time', 'deadline', 'approval_request'
     ]
     list_filter = [
          'priority', 'approval_request', 'deadline'
     ]
     ordering = ['deadline']

class AssignAdmin(admin.ModelAdmin):
     model = AssignDetails
     list_display = [
          'assignee', 'assignor', 'status',
          'status_update'
     ]
     ordering = ['status_update']
     list_filter = ['status']

admin.site.register(User, UserAdmin)
admin.site.register(Authorization, AuthorizationAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(AssignDetails, AssignAdmin)