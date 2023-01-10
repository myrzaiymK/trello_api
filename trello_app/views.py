from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Q
from .models import Board, Card, Column
from .forms import *
import django_filters


@login_required
def labels(request):
    labels = Card.label.get(pk=request.user.id)
    context = {
        'labels': labels,
    }
    return render(request, 'card/card_detail.html', context)


def create_label(request):
    form = LabelForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return redirect('/home/board/')

    context = {'form': form}
    return render(request, "board/create_view.html", context)



@login_required
def archive_post(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if board.archive.filter(pk=request.user.id).exists():
        board.archive.remove(request.user)
    else:
        board.archive.add(request.user)
    return redirect(reverse("board_index"))


@login_required
def archive_list(request):
    archive_posts = request.user.archive.all()
    context = {
        'archive_posts': archive_posts,
    }
    return render(request, 'board/archive.html', context)


@login_required
def create_card(request):
    context = {}

    form = CardForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return redirect('/home/board/')

    context['form'] = form
    return render(request, "board/create_view.html", context)

@login_required
def card_delete(request, pk, template_name='card/card_delete.html'):
    contact = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, template_name, {'object': contact})


from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

@login_required
def update_view(request, pk):
    context = {}
    obj = get_object_or_404(Card, pk=pk)
    form = CardForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        # return HttpResponseRedirect("/")
        return redirect(reverse("card-detail", kwargs={"pk": pk}))

    context["form"] = form

    return render(request, "card/card_update.html", context)

@login_required
def card_detail(request, pk):
    card = get_object_or_404(Card, pk=pk)
    comments = card.comments.filter(pk=pk)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = card
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'card': card,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form

    }
    return render(request, 'card/card_detail.html', context)


# redirect(reverse('blog_detail', args=[pk]))
#     return redirect(reverse("card_detail" , context))

@login_required
def create_column(request):
    context = {}

    form = ColumnForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "board/create_view.html", context)

@login_required
def column_delete(request, pk, template_name='column/column_delete.html'):
    contact = get_object_or_404(Column, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/home/boards/')
    return render(request, template_name, {'object': contact})

@login_required
def create_view(request):
    if request.method == "POST":
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("board_index"))
    elif request.method == "GET":
        form = BoardForm()
    context = {}
    context['form'] = form
    return render(request, "board/board_create.html", context)

@login_required
def delete(request, pk, template_name='board/board_delete.html'):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        board.delete()
        return redirect('/home/boards/')
    return render(request, template_name, {'object': board})


def board_index(request):
    boards = Board.objects.all()
    user = request.user
    archive_posts = user.archive.all()
    context = {
        'boards': boards,
        'archive_posts': archive_posts,
    }
    return render(request, 'board/board_index.html', context)


def board_detail(request, pk):
    board = Board.objects.get(pk=pk)
    boards = Board.objects.all()
    is_favourite = False
    if board.favourites.filter(pk=request.user.id).exists():
        is_favourite = True

    is_archive = False

    if board.archive.filter(pk=request.user.id).exists():
        is_archive = True

    context = {
        'board': board,
        'boards': boards,
        'is_favourite': is_favourite,
        'is_archive': is_archive,
    }
    return render(request, 'board/board_detail.html', context)

@login_required
def favourite_post(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if board.favourites.filter(pk=request.user.id).exists():
        board.favourites.remove(request.user)
    else:
        board.favourites.add(request.user)
    return redirect(reverse("board_detail", kwargs={"pk": board.id}))

@login_required
def favourite_list(request):
    user = request.user
    favourite_posts = user.favourites.all()
    context = {

        'favourite_posts': favourite_posts,
    }
    return render(request, 'board/favorites.html', context)


def test_board(request):
    return render(request, 'board/boards.html')


def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        results = Board.objects.filter(Q(title__icontains=query)) or  Card.objects.filter(Q(title__icontains=query))

    return render(request, 'board/search.html', {'query': query, 'results': results})


# class Filter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='iexact')
#
#     class Meta:
#         model = Product
#         fields = ['price', 'release_date']



# class ProductFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='iexact')
#
#     class Meta:
#         model = Product
#         fields = ['price', 'release_date']