from django.urls import path
from django.conf.urls import url


from .import views

app_name = 'estimator'

urlpatterns = [
        url(r'^$',views.polls_list, name = "list"),
        path('details/<int:poll_id>/', views.poll_detail, name='detail'),
        path('details/<int:poll_id>/vote/', views.poll_vote, name='vote'),

]
