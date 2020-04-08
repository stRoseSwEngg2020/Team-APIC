from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('administration/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),

    path('streamers/create/', StreamerCreateView.as_view(),
         name="create-streamer"),
    path('streamers/list/', StreamerListView.as_view(), name="list-streamer"),
    path('streamers/<int:pk>/update/',
         StreamerUpdateView.as_view(), name="update-streamer"),
    path('streamers/<int:pk>/delete/',
         StreamerDeleteView.as_view(), name="delete-streamer"),
    path('movie/details/', MovieDetailView.as_view(), name="detail")
]
