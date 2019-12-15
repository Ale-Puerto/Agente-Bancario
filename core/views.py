from django.shortcuts import render, redirect
from django.http import  HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.views.generic import TemplateView, ListView,DetailView
from django.views import generic
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from django.core import serializers
from io import BytesIO
from django.http import FileResponse
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import date
from datetime import datetime

import winsound


from .models import  *
# Create your views here.


class IndexView(TemplateView):
    template_name = "estado/index.html"
   
class CuentaListView(generic.ListView):
    model = Cuenta
   
    template_name = "estado/consulta.html"


class TransaccionListView(generic.ListView):
    model = Transaccion
    template_name = "estado/transaccion.html"
    
    
class RetirarView(TemplateView):
    template_name = "estado/retiros.html"
    
    
class DepositarView(TemplateView):
    template_name = "estado/depositos.html"




        
        
class TransaccionDetailView(DetailView):
    model = Transaccion
    template_name = "estado/detalle.html"


def deposito_transaccion(request):
   
    monto = request.GET.get('monto',None)
    monto = float(monto)
    cuenta = get_object_or_404(Cuenta, IdCuenta = '1')
    saldo_anterior = cuenta.Monto
    nuevo_saldo = monto + saldo_anterior
    cuenta.Monto = nuevo_saldo
    cuenta.save(update_fields = ['Monto'])
    slug = get_random_string(length = 8)
    transaccion = Transaccion(slug = slug,
                              Id_Cuenta = cuenta.IdCuenta,
                              Tipo = 'Deposito',
                              Monto = monto,
                              Saldo_anterior = saldo_anterior,
                              Saldo_nuevo = nuevo_saldo)
    transaccion.save()
    
    data = {
            'is_OK':'True'
        }
    return JsonResponse(data)
    
  


def retiro_transaccion(request):
       
    monto = request.GET.get('monto',None)
    monto = float(monto)
    cuenta = get_object_or_404(Cuenta, IdCuenta = '1')
    if monto < cuenta.Monto:
        saldo_anterior = cuenta.Monto
        nuevo_saldo = saldo_anterior - monto
        cuenta.Monto = nuevo_saldo
        cuenta.save(update_fields = ['Monto'])
        slug = get_random_string(length = 8)
        transaccion = Transaccion(slug = slug,
                                Id_Cuenta = cuenta.IdCuenta,
                                Tipo = 'Retiro',
                                Monto = monto,
                                Saldo_anterior = saldo_anterior,
                                Saldo_nuevo = nuevo_saldo)
        transaccion.save()
        winsound(1500, 500 )
        data = {
            'is_OK':'True'
        }
        return JsonResponse(data)
    
    else:
        data = {
            'Failed': 'False'
        }
        
    
    
    

def report(request, string):
    
    transaccion = get_object_or_404(Transaccion, slug = string)
    response = HttpResponse(content_type = 'application/pdf')
    monto = str(transaccion.Monto)
    saldoA = str(transaccion.Saldo_anterior)
    saldoN = str(transaccion.Saldo_nuevo)
    response['Content-Disposition'] = 'attachment; filename = Reporte.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    
    #header
    c.setLineWidth(3)
    c.setFont('Helvetica', 22)
    c.drawString(30, 750, 'Reporte de Transaccion')
    c.setFont('Helvetica', 12)
    c.drawString(30, 735, 'Report')
    
    c.setFont('Helvetica-Bold', 12)
    c.drawString(480, 750, "01/07/2016")
    
    #ESTILOS
    c.setFont('Helvetica', 12)
    c.drawString(45, 550, "ID CUENTA ")
    c.setFont('Helvetica', 12)
    c.drawString(300, 550,  "XXX-XXX-XXX")
    
    c.setFont('Helvetica', 12)
    c.drawString(45, 500 , " Cliente ")
    c.setFont('Helvetica', 12)
    c.drawString(300, 500, request.user.username)
    
    c.setFont('Helvetica', 12)
    c.drawString(45, 450, "Tipo")
    c.setFont('Helvetica', 12)
    c.drawString(300, 450, transaccion.Tipo)
    
    c.setFont('Helvetica', 12)
    c.drawString(45, 400, "Monto ")
    c.setFont('Helvetica', 12)
    c.drawString(300, 400, monto)
    
    c.setFont('Helvetica', 12)
    c.drawString(45, 350, "Saldo Anterior ")
    c.setFont('Helvetica', 12)
    c.drawString(300, 350, saldoA )
    
    c.setFont('Helvetica', 12)
    c.drawString(45, 300, "Saldo Restante ")
    c.setFont('Helvetica', 12)
    c.drawString(300, 300, saldoN)
    
     
    
    
   # c.drawString(45, 700, reporte.slug)
    
    
    c.line(460, 747,560,747)
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
    
    
def reporte_cuenta(request, id):
      
    estado = get_object_or_404(Cuenta, IdCuenta = id)
    response = HttpResponse(content_type = 'application/pdf')
    fecha = date.today()
    hora = datetime.today()
    
    fecha = str(fecha)
    hora = str(hora)
    
    response['Content-Disposition'] = 'attachment; filename = Estado De Cuenta.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    
    c.setLineWidth(3)
    c.setFont('Helvetica', 22)
    c.drawString(30, 750, 'Reporte de Estado de Cuenta')
    c.setFont('Helvetica', 12)
    c.drawString(30, 735, 'Report')
    
    c.setFont('Helvetica-Bold', 12)
   
    c.drawString(350, 750, hora)
    
    c.setFont('Helvetica', 12)
    c.drawString(45, 550, "ID CUENTA ")
    c.setFont('Helvetica', 12)
    c.drawString(300, 550,  "XXX-XXX-XXX")
    
    c.setFont('Helvetica', 12)
    c.drawString(45, 500 , " Cliente ")
    c.setFont('Helvetica', 12)
    c.drawString(300, 500, request.user.username)
    
    c.setFont('Helvetica', 12)
    c.drawString(45, 450, "Saldo Actual ")
    c.setFont('Helvetica', 12)
    c.drawString(300, 450,  str(estado.Monto))
    
    c.line(460, 747,560,747)
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
    
   
