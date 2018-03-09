from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import  json
from counterdb.models import *
import datetime

def counter(request):
    gt=request.GET
    a={}
    if (['hash','job','startm','endm','ver','status'].sort() == list(gt.keys()).sort() ):
        print (list(gt.keys()).sort())
        p=Syst_stand.objects.filter(thash=gt['hash'])
        if p.count()>0:
            a['hash']='OK'
        else:
            a['hash']='no found'
        try:
           startd=datetime.datetime.strptime(gt['startm'],'%d.%m.%Y_%H:%M:%S')
        except:
           a['startm']='not'+gt['startm']
        else:
           a['startm']='OK'
        try:
           endd=datetime.datetime.strptime(gt['endm'],'%d.%m.%Y_%H:%M:%S')
        except:
           a['endm']='not '+gt['endm']
        else:
           a['endm']='OK'
        if gt['status'] in ['0','1']:
            a['status']='OK'
        else:
            a['status']='not'
        
         
        if list(a.values()).count('OK') ==4:    
      
             a['res']='TRUE' 
        else:  a['res']='FALSE'
    else:
        a['res']='FALSE'
    if a['res']=='TRUE':
        if a['status']=='1':
            st=True
        else:
            st=False
        p2=Task(thash=gt['hash'],job=gt['job'],strm=startd,endm=endd, version=gt['ver'],status=st )
        p2.save()
     #json.dumps(gt)   
    return HttpResponse (json.dumps(a) )
def index (request):
    #t = get_template('templates/base.html')
    #now = datetime.datetime.now()
    #html = t.render(context=None, request=None)
    #p=Task.objects.filter(thash=gt['hash'])
    p=Task.objects
    a=p.values()[0]
    #html=json.dumps(a['job'])
    t = get_template('templates/base.html')
    now = datetime.datetime.now()
    html = t.render(context={'tasks':p}, request=None)
    return HttpResponse(html)
