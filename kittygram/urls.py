from django.urls import include, path
from rest_framework.routers import SimpleRouter

# from cats.views import cat_list
# from cats.views import APICat, cat_detail
# from cats.views import CatList, CatDetail
from cats.views import CatViewSet

router = SimpleRouter()
router.register('cats', CatViewSet, basename='cats')

urlpatterns = [
    # path('cats/', cat_list),
    # path('cats/', APICat.as_view()),
    # path('cats/<int:pk>/', cat_detail),
    # path('cats/', CatList.as_view()),
    # path('cats/<int:pk>/', CatDetail.as_view()),
    path('', include(router.urls)),
]


