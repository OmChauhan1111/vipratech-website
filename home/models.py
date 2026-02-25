from django.db import models
from django.utils import timezone


# ================= CONTACT MODEL =================
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    focus = models.CharField(max_length=255)
    roadmap = models.TextField()

    def __str__(self):
        return self.name


# ================= JOB APPLICATION MODEL =================
class JobApplication(models.Model):

    ROLE_CHOICES = [
        ('Django Engineer', 'Django Engineer'),
        ('React Engineer', 'React Engineer'),
    ]

    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    experience = models.CharField(max_length=50, blank=True)
    expected_salary = models.IntegerField(null=True, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    about = models.TextField(blank=True)

    resume = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.fullname