from django.shortcuts import render
import requests

def home(request):
    if request.method=="POST":
        uid=request.POST['uid']
        d=requests.get("http://restapittt.herokuapp.com/products/"+uid)
        data=[d.json()]
    else:
        res=requests.get("http://restapittt.herokuapp.com/products/")
        data=res.json();
    return render(request,'index.html',{'data':data})
def addpro(request):
    name=request.POST['name']
    price=request.POST['price']
    cat=request.POST['cat']
    cmp=request.POST['cmp']
    res=requests.post("http://restapittt.herokuapp.com/products/",{
        'name':name,
        'price':int(price),
        'cat':cat,
        'cmp':cmp
        
    })
    res=requests.get("http://restapittt.herokuapp.com/products/")
    data=res.json();
    return render(request,'index.html',{'data':data})
def delete(request):
    uid=request.GET['id']
    requests.delete("http://restapittt.herokuapp.com/products/"+uid)
    res=requests.get("http://restapittt.herokuapp.com/products/")
    data=res.json();
    return render(request,'index.html',{'data':data})
def update(request):
    id=request.POST['id']
    name=request.POST['name']
    price=request.POST['price']
    cat=request.POST['cat']
    cmp=request.POST['cmp']
    res=requests.put("http://restapittt.herokuapp.com/products/"+id+"/",{
        'name':name,
        'price':int(price),
        'cat':cat,
        'cmp':cmp
        
    })
    res=requests.get("http://restapittt.herokuapp.com/products/")
    data=res.json();
    return render(request,'index.html',{'data':data})
    
    
    
    
