from django.urls import path
from django.contrib.auth.models import User
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('profile/<int:userID>', views.profile, name='profile'),
    path('add-car/', views.add_car, name='add_car'),
    path('logout/', views.logout, name='logout'),
    
    # Add the 'place_bid' URL pattern
    path('place-bid/<int:car_id>/', views.place_bid, name='place_bid'),
    path('delete-auction/<int:car_id>/', views.delete_auction, name='delete_auction'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
