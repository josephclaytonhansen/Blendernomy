from django.db import models
from django.urls import reverse

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Author(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name

class Tag(models.Model):
    tag = models.CharField(max_length=256)
    display = models.CharField(max_length=256,default='',blank=True)
    slug = models.SlugField(default='',blank=True)
    def __str__(self):
        return self.tag
    def get_absolute_url(self):
        return reverse('socialtutorial:tag', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        self.slug = self.tag
        if self.display == '':
            self.display = self.tag
        super(Tag, self).save(*args, **kwargs)
        

class SuperTag(models.Model):
    tag = models.CharField(max_length=256)
    display = models.CharField(max_length=256,default='',blank=True)
    slug = models.SlugField(default='',blank=True)
    def __str__(self):
        return self.tag
    def get_absolute_url(self):
        return reverse('socialtutorial:supertag', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        self.slug = self.tag
        if self.display == '':
            self.display = self.tag
        super(SuperTag, self).save(*args, **kwargs)

class CTA(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(max_length=2056)
    location = models.CharField(max_length = 30,choices = (("top","top"),("bottom","bottom"),("middle","middle"),("pop-up","pop-up"),("sidebar","sidebar")))
    published = models.BooleanField(default=False)
    link = models.CharField(max_length=1024, blank=True, default = "")
    def __str__(self):
        return self.title
    
class Banner(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(max_length=256)
    published = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class DigitalProduct(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(max_length=2056)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="products")
    published = models.BooleanField(default=False)
    stripe_url = models.CharField(max_length=256)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, default='')
    featured_video = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, default='')
    price = models.FloatField(default="0.0")
    saleprice = models.FloatField(default="0.0")
    onsale = models.BooleanField(default=False)
    rating = models.FloatField(default="0.0")
    sales = models.IntegerField(default=0)
    slug = models.SlugField(default='',blank=True)
    def __str__(self):
        if self.published:
            return (f"{self.title} - " f"Sales: {self.sales}" f" Rating: {self.rating}" )
        else:
            return (f"{self.title} - " f" (DRAFT)")
    
    def get_absolute_url(self):
        return reverse('socialtutorial:product', kwargs={'slug': self.slug}) 
 
class ProductKey(models.Model):
    active = models.BooleanField(default=True)
    email = models.CharField(max_length=256)
    key = models.CharField(max_length=64)
    products = models.ForeignKey(DigitalProduct, related_name="products", on_delete=models.DO_NOTHING, null=True,blank=True)
    slug = models.SlugField(default='',blank=True)
    def __str__(self):
        return self.email
    def save(self, *args, **kwargs):
        if self.slug is '':
            self.slug = self.key
        super(ProductKey, self).save(*args, **kwargs)
        
class SheepFrame(models.Model):
    frames = models.IntegerField()

class FeaturedVideo(models.Model):
    url = models.CharField(default='',max_length=300)
 
class Article(models.Model):
    user = models.ForeignKey(User, related_name="articles", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    body = models.TextField()
    video = models.CharField(max_length=1024, blank=True, default='')
    tags = models.ManyToManyField(Tag, related_name="articles")
    supertags = models.ManyToManyField(SuperTag, related_name="articles", blank=True)
    cta = models.ForeignKey(CTA, related_name="cta", on_delete=models.DO_NOTHING)
    
    slug = models.CharField(max_length=50, unique=True)
    published = models.BooleanField(default=False)
    featured_on_home_page = models.BooleanField(default=False)
    featured_on_tag_page = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    meta_author = models.CharField(max_length=50, blank=True, default='Joseph Hansen')
    meta_description = models.CharField(max_length=300)
    meta_keywords = models.CharField(max_length=300, blank=True, default='')

    meta_url = models.CharField(max_length=160, blank=True, default='')
    meta_site = models.CharField(max_length=64, default='Blendernomy')
    meta_image = models.FileField(upload_to='media/uploads/%Y/%m/%d/', blank=True, default='')
    meta_image_alt = models.CharField(max_length=300, blank=True, default='')

    meta_twitter = models.CharField(max_length=50, blank=True, default='@j_claytonhansen')
    
    def save(self, *args, **kwargs):
        if self.meta_url is '':
            self.meta_url = "https://blendernomy.com/"+self.slug
        if self.meta_image_alt is '':
            self.meta_image_alt = self.meta_description
        try:
            tags = self.tags.all()
            supertags = self.supertags.all()
            self.meta_keywords = ""
            for t in tags:
                self.meta_keywords += str(t.tag) + ","
            for t in supertags:
                self.meta_keywords += "blender " + str(t.tag) + ","
        except:
            self.meta_keywords = ""
        if self.video is None:
            self.video = ""
        super(Article, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('socialtutorial:purchaseview', kwargs={'slug': self.slug})
        
    def __str__(self):
        if self.published:
            return (f"{self.title} - " f"{self.created_at:%B %d}" f" (PUBLISHED)")
        else:
            return (f"{self.title} - " f"{self.created_at:%B %d}" f" (DRAFT)")
    
    def get_absolute_url(self):
        return reverse('socialtutorial:article', kwargs={'slug': self.slug})
        