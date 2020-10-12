from django.urls import path, include
from rest_framework import routers, renderers
from . import views
from .views import SnippetViewSet, UserViewSet1, api_root

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'snippet', views.SnippetViewSet)


#for user defined url conf for viewset
# snippet_list = SnippetViewSet.as_view({'get': 'list', 'post': 'create'})
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet1.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet1.as_view({
#     'get': 'retrieve'
# })

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace="rest_framework")),
    # path('users', views.UserList.as_view(), name='user-list'),       # for class based generic view
    # path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),        # for class based generic view
    # # path('snippet', views.snippet_list),  # for function based view
    # path('snippet/<int:pk>', views.snippet_detail),     # for function based view
    # path('snippet', views.SnippetList.as_view(), name='snippet-list'),        # for class based view
    # path('snippet/<int:pk>', views.SnippetDetail.as_view(), name='snippet-detail'),   # for class based view
    path('member', views.MemberList.as_view()),     # for class based mixin views
    path('member/<int:pk>', views.MemberDetail.as_view()),      # for class based mixin views
    path('book', views.BookList.as_view()),     # for class based generic view
    path('book/<int:pk>', views.BookDetail.as_view()),      # for class based generic view
    # path('', views.api_root),
    # path('snippet/<int:pk>/highlight', views.SnippetHighlight.as_view(), name='snippet-highlight'),

    # #for viewset
    # path('users', user_list, name='user-list'),
    # path('users/<int:pk>', user_detail, name='user-detail'),
    # path('snippet', snippet_list, name='snippet-list'),
    # path('snippet/<int:pk>', snippet_detail, name='snippet-detail'),
    # path('snippet/<int:pk>/highlight', snippet_highlight, name='snippet-highlight'),
]
