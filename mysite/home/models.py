from django.db import models


class Newborn(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    DELIVERY_CHOICES = [
        ('V', 'Vaginal'),
        ('C', 'Cesarean'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_weight = models.DecimalField(max_digits=4, decimal_places=2)
    delivery_type = models.CharField(max_length=1, choices=DELIVERY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

