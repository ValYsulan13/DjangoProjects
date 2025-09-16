from django.urls import path, include
from watchlist_app.api.views import WatchlistAV, WatchDetailAV, StreamPlatformAV, ReviewList, ReviewDetails

urlpatterns = [
    path('list/', WatchlistAV.as_view(), name='movie-list' ),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-details' ),
    path('stream/', StreamPlatformAV.as_view(), name='stream' ),
    path('review/list', ReviewList.as_view(), name='review-list' ),
    path('review/<int:pk>', ReviewDetails.as_view(), name='review-details'),
]