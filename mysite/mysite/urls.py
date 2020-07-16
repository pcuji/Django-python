from django.conf.urls import url , include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index ,  name='home'),
    url(r'^about/$',views.about ),
    url(r'^about/$',views.about ),
    url(r'^about/$',views.about ),
    url(r'^about/$',views.about ),
    url(r'services/$',views.services ,name='services'),
    url(r'websites/$', views.websites, name='websites'),
    url(r'packages/$',views.packages ,name='packages'),
    url(r'freelancer/$',views.freelancer ,name='freelancer'),
    url(r'cloud/$',views.cloud ,name='cloud'),
    url(r'applications/$',views.applications ,name='applications'),
    url(r'about/$',views.about ,name='about'),
    url(r'team/$',views.team ,name='team'),
    url(r'careers/$',views.careers ,name='careers'),
    url(r'^articles/', include('articles.urls')),
    url(r'^estimator/', include('estimator.urls', namespace='estimator')),
    url(r'^flashcards/', include('flashcards.urls', namespace='flashcards')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'contact/', include('contact.urls', namespace='contact')), # new


]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from django.conf.urls import url
# from django.views.generic.base import TemplateView
# from .import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^$',views.index ,  name='home'),
#     url(r'^about/$',views.about ),
#     url(r'services/$',views.services ,name='services'),
#     url(r'websites/$', views.websites, name='websites'),
#     url(r'packages/$',views.packages ,name='packages'),
#     url(r'freelancer/$',views.freelancer ,name='freelancer'),
#     url(r'cloud/$',views.cloud ,name='cloud'),
#     url(r'applications/$',views.applications ,name='applications'),
#     url(r'about/$',views.about ,name='about'),
#     url(r'team/$',views.team ,name='team'),
#     url(r'careers/$',views.careers ,name='careers'),
#     url(r'^articles/', include('articles.urls')),
#     url(r'^estimator/', include('estimator.urls', namespace='estimator')),
#     url(r'^accounts/', include('accounts.urls', namespace='accounts')),
#     url(r'contact/', include('contact.urls', namespace='contact')), # new
#
#
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
