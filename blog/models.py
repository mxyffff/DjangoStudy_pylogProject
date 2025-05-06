from idlelib.debugobj_r import remote_object_tree_item

from django.db import models

class Post(models.Model):
    title = models.CharField("포스트 제목", max_length=100)
    content = models.TextField("포스트 내용")
    thumbnail = models.ImageField("썸네일 이미지", upload_to="post", blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # Post 모델과 ForeignKey 관계로 연결
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"
