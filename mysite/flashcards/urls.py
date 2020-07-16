from django.urls import path
from django.conf.urls import url


from .import views

app_name = 'flashcards'

urlpatterns = [
        url(r'^$',views.decks, name = "decks"),
        path(r'edit/',views.edit_set ,name='edit_set'),
        path(r'decks/',views.decks ,name='decks'),
        path(r'^flashcards/(?P<set_id>[0-9]+)(:show)?/?$', views.review , name='review'),
        # path(r'^flip/', views.flip, name='flip'),
        path(r'^flashcards/(?P<set_id>[0-9]+)/flip/?$', views.flip, name='flip'),

        path('details/<int:poll_id>/', views.flashcard_detail, name='detail'),



]
