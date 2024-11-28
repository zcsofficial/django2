from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Destination
from .forms import DestinationForm

# Destination CRUD Views
def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'list.html', {'destinations': destinations})

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'detail.html', {'destination': destination})

def destination_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.created_by = request.user
            destination.save()
            return redirect('destination_list')
    else:
        form = DestinationForm()
    return render(request, 'create.html', {'form': form})

def destination_update(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    
    # Ensure that the user who created the destination is the one trying to update it
    if not request.user == destination.created_by:
        return redirect('destination_list')

    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destination_detail', pk=destination.pk)  # Redirect to the detail view after update
    else:
        form = DestinationForm(instance=destination)
    
    return render(request, 'update.html', {'form': form, 'destination': destination})

def destination_delete(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    
    # Ensure that the user who created the destination is the one trying to delete it
    if not request.user == destination.created_by:
        return redirect('destination_list')
    
    if request.method == 'POST':
        destination.delete()
        return redirect('destination_list')
    return render(request, 'delete.html', {'destination': destination})

# Login and Register Views
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('destination_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('destination_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
