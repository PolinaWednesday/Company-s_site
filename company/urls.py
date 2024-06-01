from rest_framework import routers

from company.apps import CompanyConfig
from company.views.contacts import ContactsViewSet
from company.views.product import ProductViewSet
from company.views.company import CompanyViewSet

app_name = CompanyConfig.name

router = routers.SimpleRouter()
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'contact', ContactsViewSet, basename='contact')


urlpatterns = router.urls
