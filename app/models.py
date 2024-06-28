from django.db import models

#Blog - title ,photo,description, published date,author


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Blog/image')
    description = models.TextField()
    published_date = models.DateTimeField(auto_now=True)

    author = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
    
class Contact(models.Model):
    COUNTRIES =(
        ('uz',"Uzbekistan"),
        ('rus', 'Rossiya'),
        ('usa', 'America')
    )
    first_name = models.CharField(max_length=800)
    last_name = models.CharField(max_length=800)
    country = models.CharField(max_length=70,choices=COUNTRIES,default='uz')
    subject = models.TextField()

def __str__(self) -> str:
    return f'{self.first_name} {self.country}'