from django.conf.urls import url
from django.urls import path
from . import views
from .api import views as api_views

# from .api import views

urlpatterns = [
    path('', views.index, name = ''),
    path('api/list', api_views.ContentListView.as_view(), name='ListContentApi'),
    path('api/create/', api_views.ContentCreateView.as_view(), name=None),
    path('api/<str:attraction_name>/', api_views.ContentDetailView.as_view(), name=None)
]