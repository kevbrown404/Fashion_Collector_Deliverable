from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"), # <- new route
    path('brands/', views.BrandsList.as_view(), name="brands_list"),
    path('brands/new/', views.BrandCreate.as_view(), name="brand_create"),
    # Our new Route including the pk param
    path('brands/<int:pk>/', views.BrandDetail.as_view(), name="brand_detail"),
    path('brands/<int:pk>/update', views.BrandUpdate.as_view(), name="brand_update"),
    # Our new Route including the pk param
    path('brands/<int:pk>/delete',views.BrandDelete.as_view(), name="brand_delete"),
    path('brands/<int:pk>/collections/new/', views.CollectionCreate.as_view(), name="collection_create"),
    path('favorites/<int:pk>/collections/<int:collection_pk>/', views.FavoriteCollectionAssoc.as_view(), name="favorite_collection_assoc"),
]

