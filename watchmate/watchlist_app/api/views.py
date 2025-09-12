from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.api.serializers import WatchlistSerializer,StreamPlatformSerializer, ReviewSerializer
from watchlist_app.models import Watchlist, StreamPlatform, Review
from rest_framework import status

class ReviewListAV(APIView):
    def get(self,request):  
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ReviewDetailAV(APIView):
    def get(self,request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(review, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StreamPlatformAV(APIView):
    def get(self,request):  
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

class WatchlistAV(APIView):
    
    def get(self,request):  
        movies = Watchlist.objects.all()
        serializer = WatchlistSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchDetailAV(APIView):
    
    def get(self,request, pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchlistSerializer(movie, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)