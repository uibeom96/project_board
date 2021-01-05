from django.db import models
from base.models import Base_model
from django.conf import settings

class Post(Base_model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="Photo/%Y:%m:%d", blank=True)
    slug = models.SlugField(db_index=True, unique=True, allow_unicode=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes", blank=True)
    dis_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dis_likes", blank=True)
    hit_count = models.IntegerField(default=0, blank=True)
    display_avilable = models.BooleanField("비공개", blank=True)


    class Meta:
        ordering = ("-created", )
        db_table = "posts"


    def __str__(self):
        return self.title