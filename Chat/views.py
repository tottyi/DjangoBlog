from winreg import DeleteValue
from django.shortcuts import render, redirect
from . models import User, Posts
from .forms import RegisterForm, Registracia
from django.views.generic import DeleteView
from django.urls import reverse_lazy
import requests
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ApiSerializer


# Create your views here.

def home(request):

    blog = Posts.objects.all()
    
    response=requests.get('https://jsonplaceholder.typicode.com/posts').json()

    return render(request, 'home.html', {'blog': blog, 'response': response})

def reg(request):

    if request.method == 'GET':
        return render(request, 'reg.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')

    reg = User(user=user, password=password)
    reg.save()

    return redirect('home')

def blog(request):

    if request.method == 'GET':
        return render(request, 'blog.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        userid = request.POST.get('userid')

        blog = Posts(title=title, body=body, userId=userid)
        blog.save()

        return redirect('home')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('home')
    else:
        form = RegisterForm()

        return render(request, "register.html", {"form":form})

def edit(request, id):

    blog = Posts.objects.get(id=id)
    form = Registracia(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'edit.html', {'blog': blog,'form': form })

class DeletePostView(DeleteView):
    model = Posts
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ApiViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = ApiSerializer
    #permission_classes = [permissions.IsAuthenticated]