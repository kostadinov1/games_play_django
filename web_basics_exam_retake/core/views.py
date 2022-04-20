from django.shortcuts import render, redirect

from web_basics_exam_retake.core.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from web_basics_exam_retake.core.models import Game, Profile

def get_profile():
    return Profile.objects.first()

def home_page(request):
    return render(request, 'home-page.html')


def create_profile_page(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = ProfileCreateForm()
    context = {
        'form': form
    }
    return render(request, 'create-profile.html', context)


def dashboard_page(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'dashboard.html', context)


def create_game_page(request):
    if request.method == 'POST':
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    else:
        form = GameCreateForm()
    context = {
        'form': form
    }
    return render(request, 'create-game.html', context)


def details_game_page(request, pk):
    game = Game.objects.get(pk=pk)

    context = {
        'game': game
    }

    return render(request, 'details-game.html', context)


def edit_game_page(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    else:
        form = GameEditForm(instance=game)
    context = {
        'form': form,
        'game': game
    }
    return render(request, 'edit-game.html', context)


def delete_game_page(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    else:
        form = GameDeleteForm(instance=game)
    context = {
        'form': form,
        'game': game
    }
    return render(request, 'delete-game.html', context)


def details_profile_page(request):
    profile = Profile.objects.first()
    games = Game.objects.all()
    total_games_count = len(games)
    average_sum = sum(game.rating for game in games)

    if average_sum > 0:
        average_game_rating = average_sum / total_games_count
    if average_sum == 0:
        average_game_rating = 0

    context = {
        'profile': profile,
        'total_games_count': total_games_count,
        'average_game_rating': average_game_rating,
    }
    return render(request, 'details-profile.html', context)


def edit_profile_page(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    else:
        form = ProfileEditForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile_page(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = ProfileDeleteForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'delete-profile.html', context)

