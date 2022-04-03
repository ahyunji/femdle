from flask import Flask, render_template, request
from datascience import *
import numpy as np

app = Flask(__name__, template_folder = 'template')

# Table of women in STEM and their biographies
names = Table().read_table('women_names.csv')
past_names = []
guess_name_list, color_tile_list, attempt =[], [], 0
answer = False


# Choose a random name from NAMES
def pick_random_name():
    name = np.random.choice(names.column('First Name'))
    while name in past_names:
        name = np.random.choice(names.column('First Name'))
    past_names.append(name)
    return name
true_name = pick_random_name().upper()
print(true_name)
# true_name = "Hyunji"

# Check character correctness and return array of colors for the tiles.
# KEY: 'gray' - Not in TRUE_NAME, 'yellow' - In TRUE_NAME but incorrect position, 'green' - In TRUE_NAME and correct position
def color_tiles(answer, guess):
    colors = []
    answer_array = list(answer)
    for i in range(len(answer)):
        guess_char = guess[i]
        if guess_char == answer[i]:
            colors.append('green')
            answer_array.remove(guess_char)
        elif guess_char in answer_array:
            colors.append('yellow')
        else:
            colors.append('gray')
    return colors

# Play game function
@app.route('/play', methods=["POST", "GET"])
def play_femdle():
    global attempt
    global answer
    global true_name

    #check attempt and error if exceeds remaining num of trials
    if attempt < 6:
        if request.method == "POST":
            attempt += 1
            guess_name = request.form["guessname"]
            guess_name_list.append(guess_name)
            curr_color_tile = call_femdle(true_name, guess_name)
            color_tile_list.append(curr_color_tile)

            result = {'name_list': guess_name_list, 'color_tile': color_tile_list, 'answer': answer, 'bio': 'bio'}
            return render_template("colortile.html", result = result)
        else:
            return render_template("frontend.html", true_length = {'length': len(true_name)})
    else:
        return render_template("frontend.html", error="your attempts ended!", true_length = {})


def call_femdle(true_name, guess_name):
    true_name_arr = list(true_name)

    # guess_name = "Sunmi"
    guess_name.upper()
    guess_name_arr = list(guess_name)

    colors = color_tiles(true_name_arr, guess_name_arr)
    
    if guess_name == guess_name:
        answer = True
    
    #return array of colors
    return colors