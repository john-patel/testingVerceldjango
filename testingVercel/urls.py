<<<<<<< HEAD
=======
"""
URL configuration for testingVercel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app imrt views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import settings
>>>>>>> fc05f82c7e8cbc49cac12c9a1033705f96295495
from django.contrib import admin
from django.urls import path
from APP import views
from django.conf.urls.static import static
from django.conf import settings


print("Hellow World")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
