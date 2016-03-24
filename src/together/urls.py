"""together URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from users.forms import RegistrationForm
from registration.backends.default.views import RegistrationView

urlpatterns = [
    url(r'^$', 'users.views.home', name='home'),
    url(r'^about/$', 'users.views.about', name='about'),
    url(r'^contact/$', 'users.views.contact', name='contact'),
    url(r'^profile/$', 'users.views.myprofile', name='profile'),
    url(r'^profile/edit/$', 'users.views.editprofile', name='editprofile'),
    url(r'^projects/$', 'project.views.myprojects', name='projects'),
    url(r'^discussions/$', 'discussion.views.discussions', name='discussions'),

    # url(r'^messages/$', 'message.views.messages', name='messages'),
    # url(r'^discussion/$', 'discussion.views.home', name='discussion'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class = RegistrationForm), name = 'registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^messages/', include('django_messages.urls')),

] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
