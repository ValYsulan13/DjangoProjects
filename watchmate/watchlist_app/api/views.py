from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from watchlist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from watchlist_app.api.serializers import WatchlistSerializer,StreamPlatformSerializer, ReviewSerializer
from watchlist_app.models import Watchlist, StreamPlatform, Review
from rest_framework import status
#from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework_swagger.views import get_swagger_view


# @extend_schema_view(
#     list=extend_schema(description='Get a list of all reviews'),
#     retrieve=extend_schema(description='Get details of a specific review'),
#     create=extend_schema(description='Create a new review'),
#     update=extend_schema(description='Update an existing review'),
#     destroy=extend_schema(description='Delete a review')
# )

class ReviewList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    permission_classes = [AdminOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class ReviewDetails(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    permission_classes = [AdminOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

# @extend_schema_view(
#     list=extend_schema(description='Get a list of all platforms'),
#     retrieve=extend_schema(description='Get details of a specific platform'),
#     create=extend_schema(description='Create a new platform'),
#     update=extend_schema(description='Update an existing platform'),
#     destroy=extend_schema(description='Delete a paltform')
# )

    
class StreamPlatformAV(APIView):
    permission_classes = [AdminOrReadOnly]
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
    


# @extend_schema_view(
#     list=extend_schema(
#         description='Get a list of all blog posts',
#         responses={200: WatchlistSerializer(many=True)}
#     ),
#     retrieve=extend_schema(
#         description='Get details of a specific blog post including comments',
#         responses={200: WatchlistSerializer}
#     ),
#     create=extend_schema(
#         description='Create a new blog post',
#         responses={201: WatchlistSerializer}
#     ),
#     update=extend_schema(
#         description='Update an existing blog post',
#         responses={200: WatchlistSerializer}
#     ),
#     destroy=extend_schema(
#         description='Delete a blog post',
#         responses={204: None}
#     )
# )

class WatchlistAV(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
    
    
    
    
    
    
    
    
    
    # class ReviewListAV(APIView):
   # permission_classes = [AdminOrReadOnly]
    
#     queryset = Review.objects.all
    
    
#     def get(self,request):  
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True, context={'request': request})
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)



# class ReviewDetailAV(APIView):
#     permission_classes = [ReviewUserOrReadOnly]
#     def get(self,request, pk):
#         try:
#             review = Review.objects.get(pk=pk)
#         except Review.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ReviewSerializer(review, context={'request': request})
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         review = Review.objects.get(pk=pk)
#         serializer = ReviewSerializer(review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     def delete(self, request, pk):
#         review = Review.objects.get(pk=pk)
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)