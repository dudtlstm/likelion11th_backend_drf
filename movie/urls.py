from django.urls import path
# 두 줄 추가
from django.conf.urls.static import static
from django.conf import settings

from .views import *
from . import views

app_name = "movie"
urlpatterns = [
    path('', views.movie_list_create),
    path('<int:movie_id>', views.movie_detail_update_delete),
    path('<int:movie_id>/comments', views.comment_read_create),
    path('tags/<str:tag_name>', views.find_tag),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)