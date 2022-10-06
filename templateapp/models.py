from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from templateapp.abstract_models import DateAbstarctModel
from ckeditor.fields import RichTextField

class CategoryModel(models.Model):
    title = models.CharField(max_length=40, blank = False, null = False)
    slug = AutoSlugField(populate_from='title', unique=True)
    
    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        
    def __str__(self):
        return self.title

class TextModel(DateAbstarctModel):
    title = models.CharField(max_length=50, blank = False, null = False)
    text = RichTextField()
    image = models.ImageField(upload_to='images/text_images/', blank = True, null = True)
    slug = AutoSlugField(populate_from='title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='text')
    author = models.ForeignKey('account.CustomUserModel', related_name='texts', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Texts'
        verbose_name = 'Text'
        db_table = "Text"
    
    def __str__(self):
        return self.title
    
class CommentModel(DateAbstarctModel):
    writer = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')
    text = models.ForeignKey(TextModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(blank=False, null=False)
 
    class Meta:
        db_table = 'comment'
        verbose_name_plural = 'Comments'
        verbose_name = 'Comment'
    
    def __str__(self):
        return self.writer.username
    
    