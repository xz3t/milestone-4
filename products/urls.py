from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('addreview/<int:product_id>/', views.add_review, name="add_review"),
    path('editreview/<int:product_id>/<int:review_id>/', views.edit_review, name="edit_review"),
]
