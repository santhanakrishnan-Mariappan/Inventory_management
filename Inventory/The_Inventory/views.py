from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.

def Index(request):
    return render(request, 'index.html')

def display_Laptops(request):
    items = Laptop.objects.all()
    context = {
        'items': items,
        'HEADER': 'LAPTOPS',

    }
    return render(request, 'index.html', context)

def display_Desktops(request):
    items = DeskTop.objects.all()
    context = {
        'items': items,
        'HEADER': 'DESKTOPS',
    }
    return render(request, 'index.html', context)

def display_Mobiles(request):
    items = Mobile.objects.all()
    context = {
        'items': items,
        'HEADER': 'MOBILES',
    }
    return render(request, 'index.html', context)

def add_device(request, cls):
    if request.method == 'POST':
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Index_page')
        else:
            return HttpResponse("<h1>There is a error creating the record</h1>")
    else:
        form = cls()
        if cls == LaptopForm:
            Device = 'Laptop'
        elif cls == DesktopForm:
            Device = 'Desktop'
        elif cls == MobileForm:
            Device = 'Mobile'
        context = {
            'form': form,
            'Device': Device,
        }
        return render(request, 'create.html', context)

def add_laptop(request):
    return add_device(request, LaptopForm)

def add_Desktop(request):
    return add_device(request, DesktopForm)

def add_Mobile(request):
    return add_device(request, MobileForm)

def edit_device(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('Index_page')
    else:
        form = cls(instance = item)
        return render(request, 'edit.html', {'form': form})

def edit_Laptop(request, pk):
    return edit_device(request, pk, Laptop, LaptopForm)

def edit_Desktop(request, pk):
    return edit_device(request, pk, DeskTop, DesktopForm)

def edit_Mobile(request, pk):
    return edit_device(request, pk, Mobile, MobileForm)

def delete_Laptop(request, pk):
    item = Laptop.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('display_Laptops')
    else:
        form = LaptopForm(instance=item)
        return render(request, 'delete.html', {'form': form})

def delete_Desktop(request, pk):
    item = DeskTop.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('display_Laptops')
    else:
        form = DesktopForm(instance=item)
        return render(request, 'delete.html', {'form': form})

def delete_Mobile(request, pk):
    item = Mobile.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('display_Laptops')
    else:
        form = MobileForm(instance=item)
        return render(request, 'delete.html', {'form': form})









