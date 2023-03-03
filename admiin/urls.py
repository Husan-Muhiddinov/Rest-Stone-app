from django.urls import path
from .views import AddProductView,OrderView,AdminIndexView,product_update,delete

urlpatterns=[
    path('add', AddProductView, name='add'),
    path('<int:user_id>/order', OrderView, name='order'),
    path('aindex', AdminIndexView, name='aindex'),
    path('<int:product_id>/update',product_update,name='update'),
    path('<int:product_id>/delete',delete,name='delpro'),
]