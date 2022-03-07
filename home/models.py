from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
import datetime
class Autor(models.Model):
	name=models.CharField(max_length=200,null=True,blank=True)
	img=models.ImageField(upload_to="media/autor",blank=True,null=True)

	def __str__(self):
		return "autor"
class Banner(models.Model):
	img1=models.ImageField(upload_to="media/banner",null=True,blank=True)
	img2=models.ImageField(upload_to="media/banner",null=True,blank=True)
	img3=models.ImageField(upload_to="media/banner",null=True,blank=True)

	def __str__(self):
		return "Banner"

class About(models.Model):
	title=models.CharField(max_length=200,null=True,blank=True)
	text=models.TextField(null=True,blank=True)
	img = models.ImageField(upload_to="media/banner", null=True,blank=True)

	def __str__(self):
		return self.title
class Teachers(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	img = models.ImageField(upload_to="media/banner", null=True,blank=True)
	subject=models.CharField(max_length=200,null=True,blank=True)
	phone=models.CharField(max_length=200,null=True,blank=True)

	def __str__(self):
		return  self.name

class Galarey(models.Model):


	img=models.ImageField(upload_to="media/galarey",blank=True,null=True)
	def __str__(self):
		return  "galareya"

class News(models.Model):
	title = models.CharField(max_length=200, blank=True, null=True)
	img1 = models.ImageField(upload_to="media/news",blank=True,null=True)
	img2 = models.ImageField(upload_to="media/news",blank=True,null=True)

	text=models.TextField(null=True,blank=True)
	slug = models.SlugField(null=True,blank=True, max_length=125)

	def save(self, *args, **kwargs):  # new
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)
	def __str__(self):
		return self.title
class Contact(models.Model):
	name= models.CharField(max_length=200, blank=True, null=True)
	email= models.EmailField(max_length=200, blank=True, null=True)
	message= models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.name








