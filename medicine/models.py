

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)

class Patient(models.Model):
    name = models.CharField(max_length=255)
    passport = models.CharField(max_length=10)
    date_of_birth = models.DateField()

class Pharmacy(models.Model):
    location = models.CharField(max_length=255)

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    active_substance = models.CharField(max_length=255)

class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=255)
    quantity = models.IntegerField()
    recommendations = models.CharField(max_length=255)
    date_of_issue = models.DateTimeField()

class Order(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

class Analogs(models.Model):
    medicine1 = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='medicine1')
    medicine2 = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='medicine2')


# регистрация
# class User(models.Model):
#     USER_TYPE_CHOICES = (
#         ('patient', 'Patient'),
#         ('doctor', 'Doctor'),
#         ('pharmacist', 'Pharmacist'),
#     )
    
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

#     # Дополнительные поля для профиля, если необходимо
#     # Например, для пациента можно добавить поле с номером телефона
#     phone_number = models.CharField(max_length=15, blank=True)




# class UserRegistrationForm(UserCreationForm):
#     user_type = forms.ChoiceField(choices=[
#         ('patient', 'Patient'),
#         ('doctor', 'Doctor'),
#         ('pharmacist', 'Pharmacist'),
#     ])

#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2', 'user_type']