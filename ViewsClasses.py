from email import message
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import is_valid_path, reverse_lazy
from .models import Board
from django.contrib.auth.models import User
from .models import Topic, Post
from .forms import NewTopicForm, PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic import View, CreateView

#! Function based view


def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    # user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                created_by=request.user,
                topic=topic,
            )

            return redirect('boards_topics', board_id=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})

#! Class Based view


class NewTopicView(View):
    def rendering(self, request):
        return redirect('boards_topics', board_id=board.pk)

    def post(self, request):
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                created_by=request.user,
                topic=topic,
            )
        return self.rendering(request)

    def get(self, request):
        form = NewTopicForm()
        return self.rendering(request)


#! Generic Class Based View

class NewTopicView(CreateView):
    # ? specify our model
    model = Post
    # ? specify our form
    form_class = NewTopicForm
    # ? what happen when success (redirect)
    success_url = reverse_lazy('boards_topics')
    # ? the name of rendered template (HTML File)
    template_name = 'new_topic.html'
