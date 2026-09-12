from django.db import models

# Create your models here.

class Post(models.Model):
    # author
    # image
    title = models.CharField(max_length=(255))
    content = models.TextField()
    # category
    # tag
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
    
    class Meta:
        ordering = ["-created_date"]
    
    def __str__(self) -> str:
        return f"{self.title} - {self.id}" 
    
