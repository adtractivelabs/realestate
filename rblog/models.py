from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import  get_user_model

User = get_user_model()

# Author Profile Model Structure
class AuthorProfile(models.Model):
    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    name            = models.CharField(max_length=45)
    photo           = models.ImageField(upload_to='author/')
    about           = models.TextField()
    gender          = models.CharField(choices=GENDER_CHOICE, max_length=15)
    date_created    = models.DateTimeField(auto_now_add=True)
    date_modified   = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Author Profile'

    def __str__(self):
        return self.name


# Blog Category Model Structure
class BlogCategory(models.Model):
    title        = models.CharField(max_length=50, null=True)
    desc         = models.TextField(null=True,blank=True)
    name         = models.CharField(max_length=20, null=True)
    image        = models.ImageField(upload_to="product/")
    author       = models.ForeignKey(AuthorProfile,on_delete=models.SET_NULL, null=True)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Blog Category'

# Tag Model Structure
class Tag(models.Model):
    name         = models.CharField(max_length=20, unique=True)
    author       = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True)
    is_draft     = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Tag'

    def __str__(self):
        return self.name


# Blog Model Structure
class Blog(models.Model):
    blog_category       = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True)
    blog_title          = models.CharField(max_length=50, null=True)
    blog_image          = models.ImageField(upload_to="product/")
    blog_slug           = models.SlugField(max_length=100, unique=True, db_index=True, null=True,blank=True)
    blog_tag            = models.ManyToManyField(Tag)
    blog_author         = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True,blank=True)
    is_draft            = models.BooleanField(default=False)
    pub_date            = models.DateField()
    description         = RichTextUploadingField()
    created_date        = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.blog_category)

    class Meta:
        verbose_name_plural = 'Blog'
