from django.db import models
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
        id = models.AutoField(primary_key=True)
        title = models.CharField(max_length=100)
        date = models.DateField()
        image = models.ImageField(upload_to="images/")
        content = RichTextField()
        def __str__(self):
                    return self.title