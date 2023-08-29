from rest_framework.routers import DefaultRouter

from api.views import UserModelViewSet, FoldModelViewSet, ProductModelViewSet, TakeModelViewSet


router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('folds', FoldModelViewSet)
router.register('products', ProductModelViewSet)
router.register('takes', TakeModelViewSet)

urlpatterns = [

]

urlpatterns.extend(router.urls)