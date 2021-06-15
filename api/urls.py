from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
	path('entry-list/', views.entrylist ,name='entry-list'),
	path('entry-search/', views.entrysearch ,name='entry-search'),
	path('entry-random/', views.entryrandom ,name='entry-random'),
	path('entry-detail/<int:pk>/', views.entrydeatil ,name='entry-detail'),
	path('entry-create/', views.entrycreate ,name='entry-create'),
	path('entry-update/<int:pk>/', views.entryupdate ,name='entry-update'),
	path('entry-delete/<int:pk>/', views.entrydelete ,name='entry-delete'),
]
urlpatterns = format_suffix_patterns(urlpatterns) # in order to accept URLS like "/entry-details/2.json" or "/entry-details/2.api" or "/entry-list.json"
