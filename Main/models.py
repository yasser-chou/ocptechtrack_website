from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User


class TechManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)

class Tech(AbstractBaseUser):
    username = models.CharField(max_length=30, default='default', unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    email_address = models.EmailField('Employee Email', default='example@example.com')
    site_choices = (
        ('Benguerir', 'Benguerir'),
        ('Casablanca', 'Casablanca'),
        ('Jorf Lasfar', 'Jorf Lasfar'),
        ('Khouribga', 'Khouribga'),
        ('Boucraâ', 'Boucraâ'),
        ('Youssoufia', 'Youssoufia'),
        ('Safi', 'Safi'),
        ('Laâyoune', 'Laâyoune'),
        ('Autre', 'Autre'),
    )
    site = models.CharField(max_length=120, choices=site_choices, default='NoName')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = TechManager()

    def __str__(self):
        return self.username



class Employe(models.Model):
    matricule=models.CharField('employe matricule',max_length=120,default='AB000')
    nom = models.CharField('Employe last name', max_length=120)
    prenom = models.CharField('Employe first name', max_length=120)
    email_address = models.EmailField('Employe Email', default='example@example.com')
    telephone=models.CharField('Contact phone',max_length=30,default='0000000000')
    department = models.CharField(max_length=120)
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/")
    writed=models.ManyToManyField(Tech,blank=True)
    site_choices=(
        ('Benguerir','Benguerir'),
        ('Casablanca','Casablanca'),
        ('Jorf Lasfar','Jorf Lasfar'),
        ('Khouribga','Khouribga'),
        ('Boucraâ','Boucraâ'),
        ('Youssoufia','Youssoufia'),
        ('Safi','Safi'),
        ('Laâyoune','Laâyoune'),
        ('Autre','Autre'),
    )
    site=models.CharField(max_length=120,choices=site_choices,default='NoName')

    def __str__(self):
        return self.nom +' '+self.prenom
    

class Ticket(models.Model):
    title = models.CharField("Ticket Title", max_length=50)
    ticket_date=models.DateTimeField('Ticket Date',auto_now_add=True)
    employe=models.ForeignKey(Employe,blank=True,null=True,on_delete=models.CASCADE)
    material=models.CharField(max_length=120)
    description=models.TextField(blank=False)
    solution=models.TextField(blank=True)
    status_choices=(
        ('completed','completed'),
        ('in progress','in progress'),
        ('pending','pending'),
    )
    status=models.CharField(max_length=120,choices=status_choices)
    writed=models.ManyToManyField(Tech,blank=True)
    writed1 = models.ManyToManyField(User, blank=True, related_name='tickets_assigned')
    completed_at = models.DateTimeField("Completed Date",auto_now_add=True)


    def __str__(self):
        return self.title

    
