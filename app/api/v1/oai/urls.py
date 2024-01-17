from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.endpoints, name='endpoints'),
    path('single-cu-config', views.ConfigSingleCU, name='single-cu-config'),
    path('single-du-config', views.ConfigSingleDU, name='single-du-config'),
    path('single-ue-config', views.ConfigSingleUE, name='single-ue-config'),
    path('multignb-cu-config', views.ConfigMultignbCU, name='multignb-cu-config'),
    path('multignb-du1-config', views.ConfigMultignbDU1, name='multignb-du1-config'),
    path('multignb-du2-config', views.ConfigMultignbDU2, name='multignb-du2-config'),
    path('multignb-ue-config', views.ConfigMultignbUE, name='multignb-ue-config'),
    path('multiue-cu-config', views.ConfigMultiueCU, name='multiue-cu-config'),
    path('multiue-du-config', views.ConfigMultiueDU, name='multiue-du-config'),
    path('multiue-ue1-config', views.ConfigMultiueUE1, name='multiue-ue1-config'),
    path('multiue-ue2-config', views.ConfigMultiueUE2, name='multiue-ue2-config'),

    path('single-cu-start', views.StartSingleCU, name='single-cu-start'),
    path('single-du-start', views.StartSingleDU, name='single-du-start'),
    path('single-ue-start', views.StartSingleUE, name='single-ue-start'),
    path('multignb-cu-start', views.StartMultignbCU, name='multignb-cu-start'),
    path('multignb-du1-start', views.StartMultignbDU1, name='multignb-du1-start'),
    path('multignb-du2-start', views.StartMultignbDU2, name='multignb-du2-start'),
    path('multignb-ue-start', views.StartMultignbUE, name='multignb-ue-start'),
    path('multiue-cu-start', views.StartMultiueCU, name='multiue-cu-start'),
    path('multiue-du-start', views.StartMultiueDU, name='multiue-du-start'),
    path('multiue-ue1-start', views.StartMultiueUE1, name='multiue-ue1-start'),
    path('multiue-ue2-start', views.StartMultiueUE2, name='multiue-ue2-start'),

    path('single-cu-stop', views.StopSingleCU, name='single-cu-stop'),
    path('single-du-stop', views.StopSingleDU, name='single-du-stop'),
    path('single-ue-stop', views.StopSingleUE, name='single-ue-stop'),
    path('multignb-cu-stop', views.StopMultignbCU, name='multignb-cu-stop'),
    path('multignb-du1-stop', views.StopMultignbDU1, name='multignb-du1-stop'),
    path('multignb-du2-stop', views.StopMultignbDU2, name='multignb-du2-stop'),
    path('multignb-ue-stop', views.StopMultignbUE, name='multignb-ue-stop'),
    path('multiue-cu-stop', views.StopMultiueCU, name='multiue-cu-stop'),
    path('multiue-du-stop', views.StopMultiueDU, name='multiue-du-stop'),
    path('multiue-ue1-stop', views.StopMultiueUE1, name='multiue-ue1-stop'),
    path('multiue-ue2-stop', views.StartMultiueUE2, name='multiue-ue2-stop'),

    path('create-all-5g', views.CreateAll5G, name='all5g'),
]