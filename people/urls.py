from django.urls import path
from .views import NeighborView

app_name = 'people'


urlpatterns = [
    path('people/', NeighborView.as_view()),
]