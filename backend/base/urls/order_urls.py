from django.urls import path 
from base.views.order_views import *



urlpatterns= [
    path('', getOrders.as_view(), name='orders'),
    path('add', addOrderItems.as_view(), name='orders-add'),
    path('<str:pk>', getOrderById.as_view(), name='user-order'),
    path('<str:pk>/pay', updateOrderToPaid.as_view(), name='pay'),
    path('<str:pk>/delivered', updateOrderToDelivered.as_view(), name='user-delivered'),
]