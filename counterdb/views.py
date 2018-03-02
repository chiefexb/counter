from django.shortcuts import render
from django.http import HttpResponse
import  json
from counterdb.models import *

# Create your views here.
def counter(request):
    gt=request.GET
    a={}
    #datetime.datetime.strptime(datem,'%d.%m.%Y_%H:%M:%S')
    #counter?hash=44b4df546ad5f7c9777d1594a4b6b1a4b6f887be&
    #job=job&
    #startm=13.01.2018_13:00:23
    #&endm=13.01.2018_14:00:23
    #&ver=D23.0.0.0.0
    if '[hash','job','startm','endm','ver']in gt.keys():
        p=Syst_stand.objects.filter(thash=gt['hash'])
        if p.count>0:
            a['hash']='OK'
         else:
            a['hash']='nofound'
        startd=
        #datetime.datetime(2018, 1, 13, 14, 0, 23)
        #p2 = Dodavatel(nazov='Petr', dostupnost=1)
      
        #a='OK'
        print(p.values())
        # p=Syst_stand.objects.filter(thash='44b4df546ad5f7c9777d1594a4b6b1a4b6f887be')
    #http://localhost:5555/counter?hash=44b4df546ad5f7c9777d1594a4b6b1a4b6f887be&job=job&startm=13.01.2018_13:00:23&endm=13.01.2018_14:00:23&ver=D23.0.0.0.0
    print ()
    return HttpResponse ( json.dumps(a))
def index (request):
    t = get_template('templates/base.html')
    now = datetime.datetime.now()
    html = t.render(context=None, request=None)
    
    return HttpResponse(html)