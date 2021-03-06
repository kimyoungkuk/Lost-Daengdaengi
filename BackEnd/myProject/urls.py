"""LD_Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

import myApp.views

router = routers.DefaultRouter()
router.register(r'create', myApp.views.PostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api_auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('api/dogShelter', myApp.views.Dog_shelter_list, name = "dogShelter"),
    path('api/users/login', myApp.views.login, name = "login"),
    path('api/users/signUp', myApp.views.signup, name = "signUp"),
    path('api/users/changeNickname', myApp.views.signup, name = "changeNickname"),
    
    path('api/ownerPosts/list', myApp.views.owner_post_list, name = "ownerPosts/list"),
    path('api/finderPosts/list', myApp.views.finder_post_list, name = "finderPosts/list"),
    path('api/ownerPosts/create', myApp.views.owner_post_create, name="ownerPosts/create"),
    path('api/finderPosts/create', myApp.views.finder_post_create, name="finderPosts/create"),
    path('api/ownerPosts/detail/<int:pk>', myApp.views.owner_post_detail, name="ownerPosts/detail"),
    path('api/finderPosts/detail/<int:pk>', myApp.views.finder_post_detail, name="finderPosts/detail"),
    path('api/ownerPosts/delete/<int:pk>', myApp.views.owner_post_delete, name="ownerPosts/delete"),
    path('api/finderPosts/delete/<int:pk>', myApp.views.finder_post_delete, name="finderPosts/delete"),
    
    path('api/comments/create', myApp.views.comment_create, name="comments/create"),
    
    path('api/reports/create', myApp.views.report_create, name="reports/create"),
    
    # path('api/posts/filter', myApp.views.post_filter, name="posts/filter"),
    
    path('api/ownerPosts/filter/with', myApp.views.owner_post_filter_with, name="ownerPosts/filter/with"),
    path('api/finderPosts/filter/with', myApp.views.finder_post_filter_with, name="finderPosts/filter/with"),
    
    path('api/ownerPosts/recommend/<int:pk>', myApp.views.o2f_recommend, name="ownerPosts/recommend"),
    path('api/finderPosts/recommend/<int:pk>', myApp.views.f2o_recommend, name="finderPosts/recommend"),
    
    path('api/ownerPosts/finish/<int:pk>', myApp.views.owner_post_finish, name="ownerPosts/recommend"),
    path('api/finderPosts/finish/<int:pk>', myApp.views.finder_post_finish, name="finderPosts/recommend"),
    
    path('api/finishPosts/list', myApp.views.finish_post_list, name = "finishPosts/list"),
    
    path('api/classification', myApp.views.classificationImage, name="classification"),
    path('api/dogShelter/near', myApp.views.FindNearShelter, name = "dogShelter/near"),
    path('api/ownerPosts/filter', myApp.views.filteringOwner, name = "ownerPosts/filter"),
    path('api/finderPosts/filter', myApp.views.filteringFinder, name = "finderPosts/filter"),


    path('adopt/login',myApp.views.adopt_login,name="adopt_login"),
    path('adopt/post/list',myApp.views.adopt_post_list,name="adopt_post_list"),
    path('adopt/post/create',myApp.views.adopt_post_create,name="adopt_post_create"),
    path('adopt/post/detail/<int:pk>',myApp.views.adopt_post_detail,name="adopt_post_detail"),
    path('adopt/post/delete/<int:pk>',myApp.views.adopt_post_delete,name="adopt_post_delete"),


    path('master_login/',myApp.views.master_login, name = "master_login"),
    path('master_home/',myApp.views.master_home, name = "master_home"),
    
    path('master_user_list/',myApp.views.master_user_list, name = "master_user_list"),
    path('master_user_detail/<int:pk>',myApp.views.master_user_detail, name = "master_user_detail"),
    path('master_user_update/<int:pk>',myApp.views.master_user_update, name = "master_user_update"),
    path('master_user_delete/<int:pk>',myApp.views.master_user_delete, name = "master_user_delete"),
    
    path('master_owner_post_list/',myApp.views.master_owner_post_list, name = "master_owner_post_list"),
    path('master_owner_post_detail/<int:pk>',myApp.views.master_owner_post_detail, name = "master_owner_post_detail"),
    path('master_owner_post_update/<int:pk>',myApp.views.master_owner_post_update, name = "master_owner_post_update"),
    path('master_owner_post_delete/<int:pk>',myApp.views.master_owner_post_delete, name = "master_owner_post_delete"),
    
    path('master_finder_post_list/',myApp.views.master_finder_post_list, name = "master_finder_post_list"),
    path('master_finder_post_detail/<int:pk>',myApp.views.master_finder_post_detail, name = "master_finder_post_detail"),
    path('master_finder_post_update/<int:pk>',myApp.views.master_finder_post_update, name = "master_finder_post_update"),
    path('master_finder_post_delete/<int:pk>',myApp.views.master_finder_post_delete, name = "master_finder_post_delete"),
    
    path('master_dog_shelter_list/',myApp.views.master_dog_shelter_list, name = "master_dog_shelter_list"),
    path('master_dog_shelter_detail/<int:pk>',myApp.views.master_dog_shelter_detail, name = "master_dog_shelter_detail"),
    path('master_dog_shelter_update/<int:pk>',myApp.views.master_dog_shelter_update, name = "master_dog_shelter_update"),
    path('master_dog_shelter_delete/<int:pk>',myApp.views.master_dog_shelter_delete, name = "master_dog_shelter_delete"),
    
    path('master_report_list/',myApp.views.master_report_list, name = "master_report_list"),
    path('master_report_detail/<int:pk>',myApp.views.master_report_detail, name = "master_report_detail"),
    path('master_report_update/<int:pk>',myApp.views.master_report_update, name = "master_report_update"),
    path('master_report_delete/<int:pk>',myApp.views.master_report_delete, name = "master_report_delete"),
    
    path('master_adopt_post_list/',myApp.views.master_adopt_post_list, name = "master_adopt_post_list"),
    path('master_adopt_post_detail/<int:pk>',myApp.views.master_adopt_post_detail, name = "master_adopt_post_detail"),
    path('master_adopt_post_update/<int:pk>',myApp.views.master_adopt_post_update, name = "master_adopt_post_update"),
    path('master_adopt_post_delete/<int:pk>',myApp.views.master_adopt_post_delete, name = "master_adopt_post_delete"),
    
    path('api/poster_email',myApp.views.poster_email, name = "poster_email"),

    path('api/myPosts/',myApp.views.my_post, name = "my_post"),    

    path('api/ownerPosts/list/portal/', myApp.views.owner_post_list_portal, name = "ownerPosts/list/portal"),
    path('api/finderPosts/list/portal/', myApp.views.finder_post_list_portal, name = "finderPosts/list/portal"),
    path('api/finishPosts/list/portal/', myApp.views.finish_post_list_portal, name = "finishPosts/list/portal"),
    path('adopt/post/list/portal/',myApp.views.adopt_post_list_portal,name="adopt_post_list/portal"),
    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
