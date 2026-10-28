from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=100)
    Subtitle = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to='Questions/', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.question


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.subject} from {self.name}'
