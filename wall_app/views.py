from django.shortcuts import render, redirect
from appy.models import User
from wall_app.models import Message, Comment

# Create your views here.
def theWall(request):
    context = {
        'fname' : request.session['u_fname'],
        'messages' : Message.objects.all(),
        'comments' : Comment.objects.all(),
    }
    return render(request,"wall.html", context)

def postMessage(request):
    if request.method == 'POST':
        new_message = Message.objects.create(
            desc = request.POST['desc'],
            author = User.objects.get(id = request.session['u_id'])
        )
        new_message.save()
    return redirect('/wall')

def postComment(request, val):
    if request.method == 'POST':
        new_comment = Comment.objects.create(desc = request.POST['cmnt'], author = User.objects.get(id = request.session['u_id']), messages = Message.objects.get(id = val)
        )
        new_comment.save()
    return redirect('/wall')

def clear(request):
    request.session.clear()
    return redirect("/")


