from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Provider(models.Model):
    company = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.company


class Offer(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='offers')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return "%s, %s" % (self.title, self.provider)


class Image(models.Model):
    description = models.TextField()
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.image


class Tour(models.Model):
    date = models.DateField()
    participants = models.IntegerField(default=0)
    max_participants = models.IntegerField(validators=[MinValueValidator(0)])
    min_participants = models.IntegerField(validators=[MinValueValidator(0)])
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='tours')

    def __str__(self):
        return "%s, %s" % (self.date, self.offer)


class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return "%s %s, %s" % (self.first_name, self.last_name, self.email)


class Reservation(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reservations')
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='reservations')
    number_participants = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return "%s %s, %s" % (self.tour, self.participant, self.number_participants)
