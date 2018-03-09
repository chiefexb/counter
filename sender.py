import requests
f=open('./data.csv')
lr=f.readlines()
#startm endm    job     status  hash    ver
base_url="localhost:8000/counter"

#req=requests.get(base_url+'/search/physical',params=
for r in lr:
    rr=r.split(',')
    req=requests.get('http://'+base_url,params=
    {'startm' :rr[0],
     'endm'   :rr[1],
     'job'    :rr[2],
     'status' :rr[3],
     'hash'   :rr[4],
     'ver'    :rr[5]         
         })
    print (req.url, req.status_code)


