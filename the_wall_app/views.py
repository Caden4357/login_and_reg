from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.register(request.POST)
        request.session['user_id'] = user.id
        return redirect('/blog')


def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email_address'], request.POST['password']):
        messages.error(request, "Invalid Email or Password")
        return redirect('/')
    user = User.objects.get(email_address=request.POST['email_address'])
    request.session['user_id'] = user.id
    return redirect('/blog')

def logout(request):
    request.session.clear()
    return redirect('/')


def blog_page(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'messages': Message.objects.all(),
    }
    return render(request, 'user_page.html', context)


def post_message(request):
    if request.method == "GET":
        return redirect('/')
    Message.objects.create(
        message = request.POST['post_message'],
        posted_by = User.objects.get(id=request.session['user_id'])
    )
    return redirect('/blog')

def post_comment(request, id):
    if request.method == "GET":
        return redirect('/')
    message = Message.objects.get(id=id)
    Comment.objects.create(
        comment = request.POST['post_comment'],
        message = message,
        owner = User.objects.get(id=request.session['user_id'])
    )
    return redirect('/blog')

# def delete_message(request, id):
#     to_delete = Message.objects.get(id=id)
#     to_delete.delete()
#     return redirect('/blog')