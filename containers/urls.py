from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.ContractList.as_view(), name='contract_list'),
    path('view/<int:pk>', views.ContractDetail.as_view(), name='contract_detail'),
    path('new', views.ContractCreate.as_view(), name='contract_new'),
    path('edit/<int:pk>', views.ContractUpdate.as_view(), name='contract_edit'),
    path('delete/<int:pk>', views.ContractDelete.as_view(), name='contract_delete'),
]


