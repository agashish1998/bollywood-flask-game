#python web app for bollywood game
from flask import Flask, render_template, request, redirect
from movie_list import movies
import random

player_name = ""
wrong_guessed_letters = ['A', 'E', 'I', 'O', 'U']
guessed_letters = wrong_guessed_letters
trials = 9
pre_movie = ""
player_input = ""

def movie_selector():
    word_index = random.randint(0, len(movies)-1)
    return movies[word_index].upper()

global movie_name
movie_name = movie_selector().upper()

def check_guess(x):
    for a in movie_name:
        if(a == x):
            return True
    return False  

def print_movie():
    s = ""
    for a in movie_name:
        if(a == ' '):
            s += " "
        elif(a in guessed_letters):
            s += a
        else:
            s += '_'
    return s.split()

def check_final_solution():
    for a in movie_name:
        if (a not in guessed_letters and a != ' '):
            return False

    return True

def print_bollywood():
    s = "BOLLYWOOD"
    x = ""
    for i in range(trials):
        x += s[i]
    for i in range(trials, 9):
        x += '_'
    return x

def reseter(arr):
    while(len(arr) > 5):
        arr.pop()

app = Flask(__name__)
@app.route("/")

def start():
    return render_template("start.html")

@app.route("/play", methods=["POST"])
def play():
    #print(player_name)
    global player_name
    temp1 = request.form.get("name")
    player_input = request.form.get("user")
    if(temp1 != None):
        player_name = temp1.upper()

    if player_input != None:
        global trials
        global guessed_letters
        global wrong_guessed_letters
        global movie_name
        global pre_movie
        player_input = player_input.upper()

        for a in player_input:
            if(a < 'A' or a >'Z' or (a in guessed_letters) or (a in wrong_guessed_letters)):
                continue
            if check_guess(a):
                guessed_letters.append(a)
            else:
                trials = trials -1
                wrong_guessed_letters.append(a)

        if trials < 1:
            reseter(guessed_letters)
            reseter(wrong_guessed_letters)
            trials = 9
            pre_movie = movie_name
            movie_name = movie_selector().upper()
            return redirect("/lost")

        if(check_final_solution()):
            reseter(guessed_letters)
            reseter(wrong_guessed_letters)
            trials = 9
            pre_movie = movie_name
            movie_name = movie_selector().upper()
            return redirect("/win")
            
    return render_template("game.html", bollywood_string=print_bollywood(), movie_name=print_movie())

@app.route("/win")
def win():
    return render_template("win.html", player_name=player_name, movie_name=pre_movie)

@app.route("/lost")
def lost():
    return render_template("lost.html", player_name=player_name, movie_name=pre_movie)

@app.route("/rules")
def rules():
    return render_template("rules.html")

if __name__ == "__main__":
    app.run()