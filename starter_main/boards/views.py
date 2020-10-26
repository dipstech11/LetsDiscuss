from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from django.http import Http404

# Create your views here.


def home(request):
    boards = Board.objects.all()

    return render(request, 'boards/home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'boards/topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'boards/new_topic.html',{'board':board})

