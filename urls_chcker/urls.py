"""urls_chcker URL Configuration

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

from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView
from main import views as m_views
from auth_system import views as a_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    path('', login_required(m_views.UrlListView.as_view()), name="main_page"),
    path('ajax/check/', m_views.ajax_check, name="ajax_check"),
    path('add_url/', m_views.add_url, name="add_url"),

    path('register/', a_views.RegisterTemplateView.as_view(), name="register"),
    path('login/', LoginView.as_view(template_name="auth_system/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
