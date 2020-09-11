from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from Blog.models import Post

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=140, default='Your Bio is empty')
    cover_img = models.ImageField(default='default_cover.jpg', upload_to='profile_cover_pics')
    dob = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        c_img = Image.open(self.cover_img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        if c_img.height > 300 or c_img.width > 300:
            output_size = (300,300)
            c_img.thumbnail(output_size)
            c_img.save(self.cover_img.path)


    