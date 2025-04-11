
from django.contrib import admin
from django.urls import path
from config.views import index # index import
from blog.views import post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index), # 경로가 없을 때 index View 연결
    path("posts/", post_list),
]
