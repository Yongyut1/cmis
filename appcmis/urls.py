from django.urls import path
from . import views

urlpatterns = [
    path('pm-view/', views.pm_view, name='pm_view'),
    path('pm-view2/', views.pm_view_2, name='pm_view_2'),
    path('bpd-view/', views.bpd_view, name='bpd_view'),
    path('aya-view/', views.aya_view, name='aya_view'),
    path('s0-view/', views.s0_view, name='s0_view'),
]