from django.db import models

# Create your models here.
class Profile(models.Model):
    DEPARTMENT_CHOICES = [
        ('Talent', 'Talent'),
        ('Development', 'Development'),
        ('Payroll', 'Payroll'),
        ('Operations', 'Operations'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    position = models.CharField(max_length=100)
    personal_statement = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name