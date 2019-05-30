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
    
    path('api/ownerPosts/list', myApp.views.owner_post_list, name = "ownerPosts/list"),
    path('api/finderPosts/list', myApp.views.finder_post_list, name = "finderPosts/list"),
    path('api/ownerPosts/create', myApp.views.owner_post_create, name="ownerPosts/create"),
    path('api/finderPosts/create', myApp.views.finder_post_create, name="finderPosts/create"),
    path('api/ownerPosts/detail/<int:pk>', myApp.views.owner_post_detail, name="ownerPosts/detail"),
    path('api/finderPosts/detail/<int:pk>', myApp.views.finder_post_detail, name="finderPosts/detail"),
    
    path('api/comments/create', myApp.views.comment_create, name="comments/create"),
    
    path('api/posts/filter', myApp.views.post_filter, name="posts/filter"),
    path('api/classification', myApp.views.classificationImage, name="classification"),
    path('api/dogShelter/near', myApp.views.FindNearShelter, name = "dogShelter/near"),
    path('api/ownerPosts/filter/dogType', myApp.views.filteringOwner, name = "ownerPosts/filter/dogType"),
    path('api/finderPosts/filter/dogType', myApp.views.filteringFinder, name = "finderPosts/filter/dogType"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
