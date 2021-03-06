
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from v1.shop.urls import router as shop_router
from v1.category.urls import router as category_router
from v1.partner.urls import router as partner_router
from v1.item.urls import router as item_router
# from v1.dashboard.urls import router as dashboard_router

urlpatterns = [
    path('admin/', admin.site.urls),
    # Api for signup, login
    path('auth/', include('djoser.urls')),
    # Api for Account activation
    path('auth/', include('v1.third_party.rest_framework_simplejwt.urls')),
    #to view the frontend output
    path('testoutput/', include('v1.dashboard.urls')),
]

router = DefaultRouter(trailing_slash=False)

# router.registry.extend(dashboard_router.registry)
router.registry.extend(shop_router.registry)
router.registry.extend(category_router.registry)
router.registry.extend(partner_router.registry)
router.registry.extend(item_router.registry)
urlpatterns += router.urls
