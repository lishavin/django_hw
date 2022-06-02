from django.contrib import admin
from django.urls import path
from tastyapp import views
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as acc_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('newpost/', views.newpost, name='newpost'),
    path('create/', views.create, name='create'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('input_comment/<int:post_id>', views.input_comment, name='input_comment'),

    path('login/', acc_views.login, name='login'),
    path('logout/', acc_views.logout, name='logout'),
    path('signup/', acc_views.signup, name='signup'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
