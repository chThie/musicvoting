import time

from django.shortcuts import render, redirect

from .models import Song


def index(request):
    if request.method == "POST":
        new_choice = Song()
        new_choice.interpret = request.POST['interpret']
        new_choice.song_title = request.POST['song_title']
        new_choice.save()

        return redirect('index')
    else:
        context = dict()
        if Song.objects.all():
            context['choices'] = Song.objects.order_by('played', '-votes')
        else:
            context['choices'] = False
        if request.GET.get('already_voted', False):
            context['cant_vote'] = True
        return render(request, 'votingapp/index.html', context=context)


def vote(request, choice_id):
    if request.method == "GET":
        last_voted = request.session.get('last_voted')
        now = time.time()
        if last_voted:
            time_passed = now - last_voted
            if time_passed < 60*3: # 3 Minutes
                return redirect('/?already_voted=True')

        request.session['last_voted'] = now

        choice = Song.objects.get(id=choice_id)
        if not choice.played:
            choice.votes = choice.votes + 1
            choice.save()

        return redirect('index')
