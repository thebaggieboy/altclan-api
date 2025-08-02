
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from core.views import *
from accounts.views import *
from brands.views import *
#from brands.views import *
from notifications import consumers
from notifications import views
from core.views import HealthCheckView
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'merchandises', MerchandiseViewSet)
router.register(r'user_profile', ProfileViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'coupons', CouponViewSet)
router.register(r'refund', RefundViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'wishlist', WishListViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/notifications/', views.NotificationListAPI.as_view(), name='notification-list'),
    path('api/notifications/unread_count/', views.UnreadNotificationCountAPI.as_view(), name='unread-count'),
    path('api/notifications/mark_as_read/', views.MarkAsReadAPI.as_view(), name='mark-as-read'),
    # In urls.py
    path('health/', HealthCheckView.as_view(), name='health'),
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   

