from django.urls import path
from .views import NeighborView, RadiusGetView

app_name = 'people'


urlpatterns = [
    path('people/', NeighborView.as_view()),
    path('people/<int:pk>', NeighborView.as_view()),
    path('people/search/<str:x1>/<str:y1>/<str:radius>/<int:quantity>', RadiusGetView.as_view()),
]