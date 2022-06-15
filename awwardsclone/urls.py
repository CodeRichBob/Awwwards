from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('awwards.urls')),
    # path('accounts/',include('registration.backends.simple.urls')),
    # path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'),{"next_page":'/'}),
    path('api_auth/',include('rest_framework.urls')),
]