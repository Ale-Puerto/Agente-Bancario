
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from django.urls import path, include
from .views import ( IndexView,
                    CuentaListView,
                    TransaccionListView,
                    RetirarView,
                    DepositarView,
                    TransaccionDetailView,
                    deposito_transaccion,
                    retiro_transaccion,
                    report,
                    reporte_cuenta)

app_name = 'core'

urlpatterns = [ 
   path('',login_required(IndexView.as_view()), name = 'indexA'),
   path('Consulta/',login_required(CuentaListView.as_view()), name = 'Consulta'),
   path('Transaccion/',TransaccionListView.as_view(), name = 'Transacciones'),
   path('Retiro/', RetirarView.as_view(), name = "Retiro"),
   path('Deposito/', DepositarView.as_view(), name = "Deposito"),
   path('Transaccion/Detalles/<slug>/', TransaccionDetailView.as_view(), name = 'transaccion_detail'),
   path('Deposito/Nuevo/',deposito_transaccion, name = 'deposito_nuevo'),
   path('Retiro/Nuevo/',retiro_transaccion, name = 'retiro_nuevo'),
   path('reporte/<string>',report, name = 'reporte'),
   path('estadoCuenta/<id>', reporte_cuenta, name = 'reporteC')
   
]  
