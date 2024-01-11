from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Rooms, Topic, Messeag
# from .forms import RoomForm, CreateNewUser, MessageForm
from .forms import RoomForm, MessageForm, CreateNewUser
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.



def resigter(request):
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateNewUser()
    context={"form": form}
    return render(request, 'base/resigter.html', context)

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            username=User.objects.get(username=username)
        except:
            messages.error(request, 'User Does Not Exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context={}
    # context={'user': user}
    return render(request, 'base/login-register.html', context)

@login_required(login_url='/resigter/')
def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'base/log_out.html')


def home(request):
    user_login = request.user
    nav_search = request.GET.get('nav_search')
    q = request.GET.get('q')
    tops = request.GET.get('top')
    if nav_search != None and q == None:
        q = nav_search
    if tops!=None :
        topics = Topic.objects.filter(name__contains=tops)
    else:
        topics = Topic.objects.all()
    
    if q != None :
        rooms=Rooms.objects.filter(
            Q(topic__name__contains=q)|
            Q(name__icontains=q)|
            Q(descriptions__icontains=q))
        
    else:
        rooms = Rooms.objects.all()
    try:
        mess = Messeag.objects.filter(Q(room__topic__name__icontains=q))
    except:
        mess = Messeag.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms,
                'topics':topics[0:8],
                'room_count': room_count,
                'user_check': user_login,
                'last_message': mess,
                }
    return render(request, 'base/home.html', context)


@login_required(login_url='/resigter/')
def room(request, pk):
    rooms = Rooms.objects.get(pk=pk)
    participants = rooms.participants.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            test_room = Rooms.objects.get(pk=pk)
            saving=form.save(commit=False)
            saving.user = request.user
            saving.room = test_room
            form.save()
            rooms.participants.add(request.user)
            return redirect('room', pk=pk)
    else:
        form = MessageForm()
    mess = Messeag.objects.filter(room_id=pk)
    context = {'room': rooms, 'form': form, "mess": mess, 'part': participants}
    return render(request, 'base/room.html', context)

# def room_withoutLogin(request, pk):
#     mess = Messeag.objects.filter(room_id=pk)
#     context = {'mess': mess}
#     return render(request, 'base/room.html', context)


@login_required(login_url='/resigter/')
def createRoom(request):
    user = request.user.id
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST['host'] )

        form = RoomForm(request.POST)


        # form = Rooms.objects.create(host_id=user)
        # request.POST['name'] = user
        # print(form)
        # print(request.POST.__dict__)
        # print(request.POST['host'])
        if form.is_valid():
            saving= form.save(commit=False)
            saving.host = request.user
            saving.save()
            return redirect('home')
    else:
        form = RoomForm()
    
    context={'form':form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='/resigter/')
def update(request, pk):
    room = Rooms.objects.get(pk=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST ,instance=room)
        if form .is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'obj':room}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='/resigter/')
def delete(request, pk):
    obj = Rooms.objects.get(pk=pk)
    if request.method == 'POST':    
        obj.delete()
        return redirect('home')
    context = {'obj': obj}
    return render(request, 'base/delete.html', context)










