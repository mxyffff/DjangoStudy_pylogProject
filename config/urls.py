from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from config.views import index # index import
from blog.views import post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index), # 경로가 없을 때 index View 연결
    path("posts/", post_list),
]

# 개발 환경일 때만 static 파일 제공
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
