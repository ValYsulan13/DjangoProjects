from django.urls import path, include
from watchlist_app.api.views import WatchlistAV, WatchDetailAV, StreamPlatformAV, ReviewListAV, ReviewDetailAV

urlpatterns = [
    path('list/', WatchlistAV.as_view(), name='movie-list' ),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-details' ),
    path('stream/', StreamPlatformAV.as_view(), name='stream' ),
    path('review/', ReviewListAV.as_view(), name='review-list' ),
    path('review/<int:pk>', ReviewDetailAV.as_view(), name='review-details'),
]