from django.urls import path
from .views import ArticleDetailView,BasketView,CheckOutView,function,product_delete,recently


urlpatterns=[
    path('<int:product_id>/detail',ArticleDetailView,name='detail'),
    path('basket',BasketView,name='basket'),
    path('checkout',CheckOutView,name='checkout'),
    path('orders',recently,name='orders'),
    path('<int:product_id>/delete',product_delete,name='delete'),
]