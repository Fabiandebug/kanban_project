from django.urls import path
from .views import ColumnListView, CardListView, graphql_view

urlpatterns = [
    path('columns/', ColumnListView.as_view(), name='column-list'),
    path('cards/', CardListView.as_view(), name='card-list'),
    path('graphql/', graphql_view, name='graphql'),
]
