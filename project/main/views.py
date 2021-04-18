from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from .assets import assets
import requests


def index(req:WSGIRequest):
    return render(req, 'index.html')

def search(req:WSGIRequest):
    return render(req, 'search.html')

def user(req:WSGIRequest):
    if req.method == 'GET':
        post = req.GET.get('username') or None
        if post:
            url = assets.url
            headers = assets.headers
            body = assets.getuserbody(post)
            request = requests.post(url, headers=headers, data=body)
            json = request.json()['data']['userByUsername']
            posts = json['posts']['items']
            karma = json['karma']
            username = json['username']
            bio = json['bio']
            i_d = json['id']
            return render(req, 'user.html', {'posts': posts, 'karma': karma, 'username': username, 'bio': bio, 'id': i_d})
        else:
            return redirect('index')
    else:
        return redirect('index')