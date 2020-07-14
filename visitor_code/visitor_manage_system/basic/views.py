from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import datetime
from .forms import *
from django.contrib import messages


def index(request):
    visitor = VisitDetails.objects.all().order_by('-visit_id')
    return render(request,'basic/dashboard.html',{'visitor':visitor,'k':True})


def host(request):
    host =Host.objects.all().order_by('host_id')
    count = host.count()
    return render(request,'basic/host.html',{'host':host,'count':count,'k':False})
def hostdynamic(request,pk):
    host1 = Host.objects.get(host_id=pk)
    return render(request,'basic/hostdynamic.html',{'host':host1,'k':False})
def createhost(request):
    form = HostForm()
    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
            host =Host.objects.all().order_by('host_id')
            count = host.count()
            return render(request,'basic/host.html',{'host':host,'count':count})
    context={'form':form,'k':False}
    return render(request,'basic/create_host.html',context)
def updateHost(request,pk):
    host = Host.objects.get(host_id=pk)
    form = HostForm(instance=host)
    if request.method == 'POST':
        form = HostForm(request.POST,instance=host)
        if form.is_valid():
            form.save()
            host =Host.objects.all().order_by('host_id')
            count = host.count()
            return render(request,'basic/host.html',{'host':host,'count':count,'k':False})    
    context={'form':form,'k':False}
    return render(request,'basic/create_host.html',context)
def deleteHost(request,pk):
    host = Host.objects.get(host_id=pk)
    if request.method == "POST":
        host.delete()
        host =Host.objects.all().order_by('host_id')
        count = host.count()
        return render(request,'basic/host.html',{'host':host,'count':count,'k':False})
    return render(request,'basic/delete_host.html',{'form':host,'k':False})





def visitor(request):
    visitor = Visitor.objects.all().order_by('-visitor_id')
    return render(request,'basic/visitor.html',{'visitor':visitor,'k':False})
def createvisitor(request):
    form = VisitorForm()
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            visitor = Visitor.objects.all().order_by('-visitor_id')
            return render(request,'basic/visitor.html',{'visitor':visitor,'k':False}) 
    context={'form':form,'k':False}
    return render(request,'basic/create_visitor.html',context)
def updatevisitor(request,pk):
    visitor = Visitor.objects.get(visitor_id=pk)
    form = VisitorForm(instance=visitor)
    if request.method == 'POST':
        form = VisitorForm(request.POST,instance=visitor)
        if form.is_valid():
            form.save()
            visitor = Visitor.objects.all().order_by('-visitor_id')
            return render(request,'basic/visitor.html',{'visitor':visitor,'k':False})
    context={'form':form,'k':False}
    return render(request,'basic/create_visitor.html',context)
def deletevisitor(request,pk):
    visitor = Visitor.objects.get(visitor_id=pk)
    if request.method == "POST":
        visitor.delete()
        visitor = Visitor.objects.all().order_by('-visitor_id')
        return render(request,'basic/visitor.html',{'visitor':visitor,'k':False})
    return render(request,'basic/delete_visitor.html',{'form':visitor,'k':False}) 






def events(request):
    complete =0
    event = Event.objects.all()
    upcomming = event.count()
    for i in event:
        a = i.tag
        if a == 'Complete':
            complete +=1
            i.option1 = True
            i.option2 = False
        else:
            i.option1 = False
            i.option2 = True
    upcomming = upcomming - complete
    return render(request,'basic/events.html',{'form':event,'complete':complete,'upcomming':upcomming})
def createevent(request):
    form =EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            complete =0
            event = Event.objects.all()
            upcomming = event.count()
            for i in event:
                a = i.tag
                if a == 'Complete':
                    complete +=1
                    i.option1 = True
                    i.option2 = False
                else:
                    i.option1 = False
                    i.option2 = True
            upcomming = upcomming - complete
            return render(request,'basic/events.html',{'form':event,'complete':complete,'upcomming':upcomming})
    return render(request,'basic/create_event.html',{'form':form,'k':False})
def updateevent(request,pk):
    event = Event.objects.get(event_id=pk)
    form = EventForm(instance=event)
    if request.method == 'POST':
        form = EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            event = Event.objects.all()
            return render(request,'basic/events.html',{'form':event,'k':False})
    context={'form':form,'k':False}
    return render(request,'basic/create_event.html',context)
def deleteevent(request,pk):
    event = Event.objects.get(event_id=pk)
    if request.method == "POST":
        event.delete()
        event = Event.objects.all()
        return render(request,'basic/events.html',{'form':event,'k':False})
    return render(request,'basic/delete_event.html',{'form':event,'k':False}) 







def visitdetails(request):
    form = VisitDetailsForm()
    visitdetail = VisitDetails.objects.all()
    count = visitdetail.count()
    date_object = datetime.date.today()
    date_object = str(date_object)
    count = 0
    for i in visitdetail:
        a = i.visit_date
        day = a.day
        month = a.month
        year = a.year
        if day <10:
            day = str(0)+str(day)
        if month<10:
            month = str(0)+str(month)
        date1 = str(year)+str('-')+str(month)+str('-')+str(day)
        if date_object == date1:
            count =count +1
    if request.method == 'POST':
        a = request.POST
        a1=a['duration']
        a2=a['purpose']
        a3=a['visit_detail']
        a4=a['flat_no']
        a3 = Visitor.objects.get(visitor_id=a3)
        visitdetails = VisitDetails(duration=a1,purpose=a2,visit_detail=a3,flat_no=a4)
        visitdetails.save()
        # messages.success(request,"visit entered successfull")
        return redirect('/')
    context={'form':form,'count':count,'k':False}
    return render(request,'basic/visitdetails.html',context)










def eventvisitor(request):
    form =EventVisitorForm()
    if request.method == 'POST':
        form = EventVisitorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Event guest  entered successfull")
            form =EventVisitorForm()
            return render(request,'basic/eventvisitor.html',{'form':form,'k':False})
    return render(request,'basic/eventvisitor.html',{'form':form,'k':False})
