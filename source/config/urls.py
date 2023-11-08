"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

import config.settings

# Custom administration template
admin.site.site_header = "High School Admin"
admin.site.site_title = "Somewhere city"
admin.site.index_title = "High School Administration panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.main.urls")),
    path("auth/", include("django.contrib.auth.urls")),

]

if config.settings.DEBUG:
    urlpatterns = urlpatterns + [path("__debug__/", include("debug_toolbar.urls"))]
