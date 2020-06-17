#python web app for bollywood game
from flask import Flask, render_template, request, redirect
import bollywood_oop as b

game = b.bollywood()

app = Flask(__name__)

@app.route("/")
def start():
	return render_template("start.html")

@app.route("/play", methods=["POST"])
def play():
	temp1 = request.form.get("name")
	player_input = request.form.get("user")
	if(temp1 != None):
		game.player_name = temp1.upper()

	if player_input != None:
		game.input_handle(player_input)
		

		if game.trials < 1:
	
			game.reset()
			return redirect("/lost")

		if(game.check_final_solution()):

			game.reset()
			return redirect("/win")
            
	return render_template("game.html", bollywood_string=game.print_bollywood(), movie_name=game.print_movie())

@app.route("/win")
def win():
	return render_template("win.html", player_name=game.player_name, movie_name=game.pre_movie)

@app.route("/lost")
def lost():
	return render_template("lost.html", player_name=game.player_name, movie_name=game.pre_movie)

@app.route("/rules")
def rules():
	return render_template("rules.html")

if __name__ == "__main__":
	app.run()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
