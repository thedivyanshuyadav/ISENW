from django.db import models
from .storage import OverwriteStorage

from django.conf import settings
# Create your models here.
import urllib,os

class File(models.Model):
    file=models.FileField(upload_to="icml\\images",storage=OverwriteStorage())


class Item(models.Model):
    image_file = models.ImageField(upload_to='images')
    image_url = models.URLField()


    def get_remote_image(self):
        if self.image_url and not self.image_file:
            result = urllib.urlretrieve(self.image_url)
            self.image_file.save(
                    os.path.basename(self.image_url),
                    File(open(result[0]))
                    )
            self.save()