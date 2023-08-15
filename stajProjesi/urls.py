
from django.contrib import admin
from django.urls import path
from appUser.views import *
from appMy.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # appMY
    path('',dashboardPage, name='dashboardPage'),
    path('forumDetail',forumDetail, name='forumDetail'),
<<<<<<< HEAD
    path('forumlar/<str:categoryTitle>',forumDetail, name='forumDetail'),
=======
    path('forumlar/<str:pk>',forumDetail, name='forumDetail'),
>>>>>>> main
    
    # appUser
    path('loginPage', loginPage , name='loginPage'),
    path('postDetail',postDetail, name='postDetail'),
    path('messagePost',messagePost, name='messagePost'),
    path('logout',logoutUser, name='logoutUser'),
    
]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
