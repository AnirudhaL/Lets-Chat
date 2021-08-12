from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Room, Message
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    # room = request.POST['room-id']
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username' : username,
        'room' : room,
        'room_details': room_details
    })
def checkview(request):
    room = request.POST['room-id']
    username = request.POST['user']
    if username and room != "":
        if Room.objects.filter(name=room).exists():
            return redirect('/' + room + '/?username=' + username)
        else:
            new_room = Room.objects.create(name=room)
            new_room.save()
            return redirect('/' + room + '/?username=' + username)
    else:
        return redirect(home)

def send(request):
    message = request.POST['message']
    Username = request.POST['username']
    room_id = request.POST['room_id']
    data = datetime.now()

    if message == "":
        pass
    else:
        new_message = Message.objects.create(value=message, user=Username, room=room_id, data=data)
        new_message.save()
        return HttpResponse('Message sent')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"message":list(messages.values())})