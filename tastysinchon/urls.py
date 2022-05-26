from django.contrib import admin
from django.urls import path
from tastyapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('newpost/', views.newpost, name='newpost'),
    path('create/', views.create, name='create'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('input_comment/<int:post_id>', views.input_comment, name='input_comment'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
