from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class WaterPlants(models.Model):
    CARBON_DIOXIDE = (
        ("Low", "Low"),
        ("Middle", "Middle"),
        ("High", "High"),
    )
    DIFFICULTY_LEVELS = (
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    )
    name = models.CharField(max_length=120)
    position = models.CharField(max_length=50)
    # picture = CloudinaryField('picture', blank=True, null=True, folder="media/")
    picture = models.ImageField(upload_to='media/')
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
    addition_amount = models.CharField(choices=CARBON_DIOXIDE, max_length=10)
    leaf_length = models.PositiveIntegerField()
    water_quality = models.TextField()

    def __str_(self):
        return "{} の水草情報".format(self.name)