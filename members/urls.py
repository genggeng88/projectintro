from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('soujanya/', views.soujanya, name='soujanya'),
    path('andy/', views.andy, name='andy'),
    path('margaret/', views.margaret, name='margaret'),
    path('martin/', views.martin, name='martin'),
    path('qin/', views.qin, name='qin'),
    path('william/', views.william, name='william'),
    path('victor/', views.victor, name='victor'),
]
