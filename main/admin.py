from django.contrib import admin
from .models import ContactSubmission, Questions

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question', 'Subtitle', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['question', 'Subtitle', 'message']
    ordering = ['-created_at']
    list_editable = ['is_active']


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    ordering = ['-created_at']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
