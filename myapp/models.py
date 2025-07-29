from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100, blank=True, null=True)
    services = models.TextField()  # ✅ Correct: use TextField, NOT JSONField
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Appointment for {self.name} on {self.date} at {self.time}"
