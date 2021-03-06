"""log_in URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app1 import views as login_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_view.login),
    url(r'^main/', login_view.main),
    url(r'^login/', login_view.login),
    url(r'^return/', login_view.base_return),

] + static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
