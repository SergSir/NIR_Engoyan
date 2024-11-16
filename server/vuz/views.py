from django.shortcuts import render
from django.db.models import F
from .models import (
    Main,
    Vuz,
    Training,
    Program,
    Regions,
    Districts,
    Ministries,
)

def vuz(request):
    vuz = Vuz.objects.all().select_related('id_region', 'id_district', 'id_ministry')
    regions = vuz.values('id_region__region').distinct().order_by('id_region__region')
    districts = vuz.values('id_district__district').distinct().order_by('id_district__district')
    ministry = vuz.values('id_ministry__ministry').distinct().order_by('id_ministry__ministry')
    context = {
        'regions': regions,
        'districts': districts,
        'ministry': ministry,
        'vuz': vuz,
    }
    return render(request, 'vuz/vuz.html', context)

def prog(request, vuz_id):
    vuz = Vuz.objects.get(pk=vuz_id)
    vuzid = vuz.id

    main_obj = Main.objects.filter(id_vuz = vuzid).select_related('fieldid', 'progid', 'id_vuz')
    fieldname = main_obj.values('fieldid__fieldname').distinct().order_by('fieldid__fieldname')
    formname = main_obj.values('formname').distinct().order_by('-formname')
    prog = main_obj.values('progid__progname').distinct().order_by('progid__progname')
    context = {'main_obj': main_obj,
               'fieldname': fieldname,
               'formname': formname,
               'prog': prog,
               }
    return render(request,'vuz/prog.html', context)