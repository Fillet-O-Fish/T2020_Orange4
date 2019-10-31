# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from . import main
from django.urls import path

urlpatterns = [
]
router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'transactionDetails', views.userDetail,basename='MyModel')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('login/', main.getTransactionDataByRange_cat("01-01-2018","02-01-2019", "2")),
    path('login/', main.init("limzeyang")),
    # path('login/', main.init("limzeyang")),
]
