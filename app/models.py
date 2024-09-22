import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from app.utils import image_upload_path


class User(AbstractUser):
    pass


class FoodCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=image_upload_path,null=True,blank=True)
    sort =  models.PositiveSmallIntegerField(default=10)
    date_added = models.DateTimeField(auto_now_add=True,db_index=True)
    class Meta:
        app_label = 'app'
        db_table = 'app_food_category'
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Categories'
        ordering = ['sort']
    
    def __str__(self):
        return '%s' %(self.name)


class Food(models.Model):   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=image_upload_path,null=True,blank=True)
    edible_portion = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    serving_size = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    category = models.ForeignKey(FoodCategory,on_delete=models.CASCADE,null=True,blank=True)    
    calories = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Calories (kcal)')
    # macro-nutrients and sub-components
    carbohydrates = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Carbohydrates (grams)')
    cholesterol = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Cholesterol (milligrams)')
    dietary_fibre = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Dietary Fibre (grams)')
    dietary_fibre_soluble = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Soluble Dietary Fibre (grams)')
    dietary_fibre_insoluble = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Insoluble Dietary Fibre (grams)')
    fat_total = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Total Fat (grams)')
    fat_saturated = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True,verbose_name='Saturated Fat (grams)')
    fat_trans = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True,verbose_name='Unsaturated Trans Fat (grams)')
    fat_monounsaturated = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True,verbose_name='Monounsaturated Fat (grams)')
    fat_polyunsaturated = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True,verbose_name='Polyunsaturated Fat (grams)')
    protein = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Protein (grams)')
    sodium = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Sodium (milligrams)')
    starch  = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Starch (grams)')
    sugar_total = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Sugar (grams)')
    iron = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Iron (milligrams)')
    calcium = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Calcium (milligram)')
    replacements = models.ManyToManyField('app.Food', null=True,blank=True,related_name='replacements_set')
    date_added = models.DateTimeField(auto_now_add=True,db_index=True)
    last_modified = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'app'
        db_table = 'app_food'
        verbose_name = 'Food'
        ordering = ['name']
    
    def __str__(self):
        return '%s' %(self.name)


class FoodReplacement(models.Model):
    food = models.ForeignKey(Food,on_delete=models.CASCADE, related_name='replace_from')
    replacement = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='replace_to')
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'app'
        db_table = 'app_foodreplacement'
        verbose_name = 'Food Replacement'
        ordering = ['date_added']

    def __str__(self):
        return '%s' %(self.name)


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.JSONField(default=dict)
    is_pushed = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True,db_index=True)
    last_modified = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'app'
        db_table = 'app_notification'
        verbose_name = 'Notification'
        ordering = ['date_added']

    def __str__(self):
        return '%s' %(self.message)
