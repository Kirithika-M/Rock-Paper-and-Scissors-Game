from django.shortcuts import render

import random

choices = ["rock", "paper", "scissors"]

# Create your views here.
def home(request):
    return render(request, "game/home.html")

def login(request):
    return render(request, "game/login.html")

def game(request):
    if request.method == "POST":
        user = request.POST.get("choice")
        computer = random.choice(choices)

        if user == computer:
            reply =  "It's a draw. Try again 🙂"
        elif (computer == "rock" and user == "paper") or (computer == "paper" and user == "scissors") or (computer == "scissors" and user == "rock"):
            reply =  "You win 😊"
        else:
            reply = "You lose 🥺"

        return render(request, "game/game.html", {
            "user": user,
            "computer": computer,
            "reply": reply,
        })

    return render(request, "game/game.html", {})


def logout(request):
    return render(request, "game/home.html")

