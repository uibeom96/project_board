from django.db import models
from base.models import Base_model
from django.conf import settings
from django.shortcuts import reverse

class Post(Base_model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="Photo/%Y-%m-%d")
    slug = models.SlugField(db_index=True, allow_unicode=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes", blank=True)
    dis_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dis_likes", blank=True)
    hit_count = models.IntegerField(default=0, blank=True)
    display_avilable = models.BooleanField("비공개", blank=True)


    class Meta:
        ordering = ("-created", )
        db_table = "posts"


    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("board:board_detail", args=[self.pk, self.slug])


class Comment(Base_model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)

    class Meta:
        ordering = ("-created", )
        db_table = "comments"

    def __str__(self):
        return str(self.author)+"의 댓글"


