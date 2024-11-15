from django.urls import include, path
from rest_framework.routers import DefaultRouter
from wishlist.wishlistAPI.views import WishlistViewSet

router = DefaultRouter()
router.register(r'wishlist', WishlistViewSet, basename='wishlist')

urlpatterns = [
    path('', include(router.urls)),
]