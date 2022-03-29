from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class PublicManager(models.Manager):
    def get_queryset(self):
        return super(PublicManager, self).get_queryset().filter(date_added__lte=timezone.now())



# Create your models here.
class UserRegistration(models.Model):
    useremail = models.EmailField(unique=True, db_column='USEREMAIL', max_length=200)
    username = models.CharField(primary_key=True, db_column='USERNAME', max_length=200)

    firstname = models.CharField(db_column='FIRSTNAME', max_length=200)
    middlename = models.CharField(db_column='MIDDLENAME', max_length=200)
    lastname = models.CharField(db_column='LASTNAME', max_length=200)
    address = models.TextField(db_column='ADDRESS', max_length=500)
    phone = models.IntegerField(db_column='PHONE')
    age = models.IntegerField(db_column='AGE')
    lga = models.CharField(db_column='L.G.A', max_length=200)

    # password = models.CharField(db_column='PASSWORD', max_length=200)
    datereg = models.DateTimeField(auto_now_add=True)
    class Meta:
        # managed = False
        db_table = 'registered_users'








STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
        db_table = 'posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])





