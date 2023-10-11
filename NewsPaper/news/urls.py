from django.urls import path, include
from django.views.decorators.cache import cache_page
from .views import *
from .views import upgrade_me

urlpatterns = [
    path('', cache_page(10)(PostList.as_view()), name='news'),
    path('<int:pk>', cache_page(10)(PostDetail.as_view()), name='new_s'),
    path('search', SearchList.as_view(), name='search'),
    path('add', PostCreateView.as_view(), name='add_post'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('login/', LoginView.as_view(template_name='login_page.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout_page.html'), name='logout'),
    path('', IndexView.as_view(), name='index'),
    path('login/signup/', RegisterView.as_view(), name='signup'),
    path('accounts/', include('allauth.urls')),
    path('getauthor/', get_author, name='getauthor'),
    path('upgrade/', upgrade_me,name='upgrade'),
    path('categories', PostCategoryView.as_view(), name='categories'),
    path('categories/<int:pk>', CategoryDetail.as_view(), name='cat_detail'),
    path('subscribe/<int:pk>', subscribe_to_category, name='subscribe'),
    path('unsubscribe/<int:pk>', unsubscribe_from_category, name='unsubscribe'),
]