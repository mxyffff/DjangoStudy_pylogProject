from sys import prefix

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from config.views import index # index import
from blog.views import post_list, post_detail, post_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index), # 경로가 없을 때 index View 연결
    path("posts/", post_list),
    path("posts/<int:post_id>/", post_detail),
    path("posts/add/", post_add),
]
urlpatterns += static(
    # URL의 접두어가 MEDIA_URL일 때는 정적파일을 돌려준다
    prefix = settings.MEDIA_URL,
    # 돌려줄 디렉터리는 MEDIA_ROOT를 기준으로 한다
    document_root=settings.MEDIA_ROOT,
)