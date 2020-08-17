from django.shortcuts import render,redirect,get_object_or_404
from .models import Crud

from django.http import JsonResponse


def home(request):
    users = Crud.objects.all()
    return render(request,'base.html',{'users':users})


def createuser(request):
    name1 = request.POST.get('name',None)
    address1 = request.POST.get('address',None)
    phone1 = request.POST.get('phone',None)


    obj = Crud.objects.create(
        name = name1,
        address = address1,
        phone = phone1
    )
    obj.save()

    # user = {'id':obj.id,'name':obj.name,'address':obj.address,'phone':obj.phone}
    #
    # data = {
    #     'user':user
    # }
    #
    # return JsonResponse(data)
    return redirect('home')



def update(request):
    id1 = request.POST.get('formId',None)
    name1 = request.POST.get('formName')
    address1 = request.POST.get('formAddress')
    phone1 = request.POST.get('formPhone')
    print(id1)
    print(name1)
    obj = Crud.objects.get(id=id1)
    print(obj)
    obj.name = name1
    obj.address = address1
    obj.phone = phone1
    obj.save()

    return redirect('home')


def delete(request,id):
    obj = get_object_or_404(Crud,pk=id)

    obj.delete()
    return redirect('home')

