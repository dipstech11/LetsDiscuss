from django.shortcuts import render
from django.http import HttpResponse
from .models import Board, Topic, Post
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    boards = Board.objects.all()
    # 
    # boards_name = []
    
    # for board in boards:
        # boards_name.append(board.name)
        
    # response_html = "<br>".join(boards_name)
    
    # return HttpResponse(response_html)
    return render(request, 'boards/home.html', {'boards':boards})
