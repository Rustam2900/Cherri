from django.urls import path

from order.views import AddItemToCartView, ListItemsFromCardView, RemoveItemFromCartView, OrderCreateView, RemoveCart, \
    OrderHistoryListView, OrderCancelView, OrderMinSumView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('', OrderHistoryListView.as_view(), name='order_history_list'),
    path('<int:order_id>/cancel/', OrderCancelView.as_view(), name='order_cancel'),
    path('min-sum/', OrderMinSumView.as_view(), name='order_min_sum'),
    path('cart-items/', ListItemsFromCardView.as_view(), name='cart_item_list'),
    path('delete-all-carts/', RemoveCart.as_view(), name='cart_delete'),
    path('add-item-to-cart/<int:product_id>/', AddItemToCartView.as_view(), name='add_cart_item'),
    path('cart-items/<int:product_id>/', RemoveItemFromCartView.as_view(), name='cart_items'),
]