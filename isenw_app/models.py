from django.db import models


# Create your models here.
class Content(models.Model):
    id=models.AutoField(primary_key=True,max_length=20,serialize=False)
    image=models.ImageField(default='',upload_to='isenw_app/uploads',blank=False,max_length=500)
    # image=CameraImageField(aspect_ratio=Fr)
    # bin_image=models.BinaryField(blank=True)

    def __str__(self):
        return "IMAGE"
