from django.urls import path
from .views import ThingList,ThingDetail,PostList,PostDetail
urlpatterns = [
    path('',ThingList.as_view(),name='thinge_list'),
    path('/<int:pk>/',ThingDetail.as_view(),name='thinge_detail'),
    path('/post/',PostList.as_view(),name='post_list'),
    path('/post/<int:pk>/',PostDetail.as_view(),name='post_detail'),
]