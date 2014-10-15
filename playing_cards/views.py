from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from playing_cards.forms import EmailUserCreationForm
from playing_cards.models import Card, WarGame, Player
import random



# Create your views here.
def cards(request):
    data = {
        'cards': Card.objects.all(),
    }
    return render(request, 'cards.html', data)

def card_filters(request):
    data = {
        'cards': Card.objects.all(),
    }
    return render(request, 'card_filters.html', data)

def faq(request):
    return render(request, 'faq.html')


@login_required()
def profile(request):
    games = WarGame.objects.filter(player=request.user)
    score = 0
    wins = 0
    losses = 0
    draws = 0
    for game in games:
        score += game.result
        if game.result == 1:
            wins += 1
        elif game.result == -1:
            losses += 1
        elif game.result == 0:
            draws += 1
    total = wins + losses + draws
    data = {
        'score': score,
        'games': games,
        'wins': wins,
        'losses': losses,
        'draws': draws,
        'total': total
    }
    if total == 10:
        request.user.email_user("Hey there {}!".format(request.user.first_name), "Thanks for playing War!")

    return render(request, 'profile.html', data)

@login_required()
def deal_5(request):
    all_cards = Card.objects.all()
    hand= []
    for i in range(5):
        random_num = random.randint(0,len(all_cards) - 1)
        hand.append(all_cards[random_num])
    data = {
        'cards': Card.objects.all(),
        'hand': hand
    }
    return render(request, 'deal_5.html', data)
@login_required()
def blackjack(request):
    data = {
        'cards': Card.objects.order_by('?')[:2],
    }

    return render(request, 'blackjack.html', data)
@login_required()
def poker(request):
    data = {'cards': Card.objects.order_by('?')[:5]}

    return render(request, 'poker.html', data)
@login_required()
def all_hearts(request):
    data = {
        'cards': Card.objects.filter(suit=3)
    }

    return render(request, 'all_hearts.html', data)


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email_user("Welcome {}!".format(user.first_name), "Thanks for signing up for our website")
            return redirect("profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required()
def war(request):
    random_cards = Card.objects.order_by('?')
    user_card = random_cards[0]
    dealer_card = random_cards[1]

    result = user_card.get_war_result(dealer_card)
    WarGame.objects.create(result=result, player=request.user)
    if result == "win":
        WarGame.player.score += 1
    elif result == "loss":
        WarGame.player.score -= 1
    return render(request, 'war.html', {
        'user_cards': [user_card],
        'dealer_cards': [dealer_card],
        'result': result
    })

def leaderboard(request):
    players = Player.objects.all()
    data = {
        'players': players
    }

    return render(request, "leaderboard.html", data)