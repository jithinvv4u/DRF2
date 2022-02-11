from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.views import View
# Create your views here.

def index(request):
    return render(request,'index.html')

def inventoryHome(request):
    if request.method=='POST':
        form=InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
        else:
            return HttpResponse('not valid')
    else:
        form=InventoryForm()
        inventoryData=Inventory.objects.all()
        return render(request,'inventory.html',{'form':form,'inventoryData':inventoryData})

def inventoryUpdate(request,id):
    if request.method=='POST':
        form=InventoryForm(request.POST,instance=Inventory.objects.get(pk=id))
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form=InventoryForm(instance=Inventory.objects.get(pk=id))
        return render(request,'inventoryUpdate.html',{'form':form})

def inventoryDelete(req,id):
    objDep=Inventory.objects.get(pk=id)
    objDep.delete()
    return redirect('inventory')

def purchaseItem(request,id):
    if request.method=='POST':
        quantityPost=request.POST['quantity']
        print(quantityPost)
        obj=Inventory.objects.filter(id=id)
        obj1=obj[0]
        if obj1.quantity >int(quantityPost):
            obj1.quantity -= int(quantityPost)
            obj1.save()
            return redirect('inventory')
        else:
            return HttpResponse('not valid')
    else:
        form=InventoryForm(instance=Inventory.objects.get(pk=id))
        return render(request,'purchase.html',{'form':form})


# class inventoryHome(View):
#     form_class = InventoryForm
#     model = Inventory
#     template = 'inventory.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         inventoryData = self.model.objects.select_related().all()
#         context = {'form': form,'inventoryData':inventoryData}
#         return render(request,'inventory.html',context)

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             form = self.form_class()
#             return redirect('inventory')
#         else:
#             return HttpResponse('not valid')
