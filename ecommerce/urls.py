from django.contrib import admin
from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('product/<int:product_id>/', views.product_detail),
    path('cart/', views.cart_view),
    path('add-to-cart/<int:product_id>/', views.add_to_cart),
    path('place-order/', views.place_order),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)