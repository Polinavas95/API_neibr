from django.urls import path
from .views import NeighborView, DistanceGetView, DistanceGetNeighborView

app_name = 'people'

urlpatterns = [
    path('people/', NeighborView.as_view(), name='all_neighbors'),
    path('people/<int:pk>', NeighborView.as_view(), name='neighbor_action'),
    path('people/search/<str:x1>/<str:y1>/<str:radius>/<int:quantity>',
         DistanceGetView.as_view(),
         name='neighbor_search'
         ),
    path('people/<int:id>/search',
         DistanceGetNeighborView.as_view(),
         name='id_neighbor_search'
         ),
]
