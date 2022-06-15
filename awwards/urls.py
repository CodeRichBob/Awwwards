from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

#API routes
router = routers.DefaultRouter()
router.register('profiles',views.ProfileView)
router.register('projects',views.ProjectsView)
router.register('projects_ratings',views.RatingsView)

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('profile/update/',views.update_profile,name='profileUpdate'),
    path('post_project/',views.post_project,name='post_project'),
    path('search/project/',views.search_project,name='search_project'),
    path('rate_project/<int:project_id>',views.rate_project,name='rate'),
    path('details/project/<int:project_id>',views.project_details,name='project_details'),
    path('api/',include(router.urls)),
    path('login/',views.signin,name='login'),
    path('register/',views.register,name='register'),
    path('signout/',views.signout,name='signout'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)