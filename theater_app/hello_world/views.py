from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RenewTicketDate
from django.urls import reverse

from hello_world.models import Play
from hello_world.models import Actor
from hello_world.models import Ticket
from hello_world.models import PlayInfo
from hello_world.models import Author
from .models import Review


def hello_world(request):
    return render(request, 'hello_world.html', {})


def play_page(request):
    plays = Play.objects.filter(type="1")
    plays2 = Play.objects.filter(type="2")
    plays3 = Play.objects.filter(type="3")
    plays4 = Play.objects.filter(type="4")
    context = {'plays': plays, 'plays2': plays2, 'plays3': plays3, 'plays4': plays4}
    return render(request, 'play_page.html', context)


def team_page(request):
    actors = Actor.objects.all()
    context = {'actors': actors}
    return render(request, 'team_page.html', context)


def gallery_page(request):
    plays = Play.objects.all()
    context = {'plays': plays}
    return render(request, 'gallery_page.html', context)


def tickets_page(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'tickets_page.html', context)


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['play', 'date_of_play', 'price', 'quantity', 'buyer_name']


def ticket_create(request, template_name='ticket_form.html'):
    form = TicketForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/tickets')
    return render(request, template_name, {'form': form})


def ticket_update(request, pk, template_name='ticket_form.html'):
    ticket = get_object_or_404(Ticket, pk=pk)
    form = TicketForm(request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()
        return redirect('/tickets')
    return render(request, template_name, {'form': form})


def ticket_delete(request, pk, template_name='ticket_confirm_delete.html'):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('/tickets')
    return render(request, template_name, {'object': ticket})


def playinfo_page(request):
    playinfo = PlayInfo.objects.all()
    context = {'play_infos': playinfo}
    return render(request, 'playinfo_page.html', context)


def author_page(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'author_page.html', context)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'play', 'text', 'reviewer_name']


def review_create(request, template_name='review_form.html'):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/reviews')
    return render(request, template_name, {'form': form})


def reviews_page(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'reviews_page.html', context)


from django.views import generic


class author_page(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author


class review_page(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Review


class actor_detail(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Actor


