from django.conf.urls import url

from . import views

app_name = "ng"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^todos$', views.AllTodo, name='todos'),
    url(r'^todos/(?P<todo_id>[0-9]+)$', views.SingleTodo, name='todos'),
]