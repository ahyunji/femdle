from flask import Flask, jsonify, render_template, request
from datascience import *
import numpy as np

app = Flask(__name__)

# Table of women in STEM and their biographies
names = Table().read_table('women_names.csv')
past_names = []

# Choose a random name from NAMES
def pick_random_name():
    name = np.random.choice(names.column('First Name'))
    while name in past_names:
        name = np.random.choice(names.column('First Name'))
    past_names.append(name)
    return name

# Check character correctness and return array of colors for the tiles.
# KEY: 'gray' - Not in TRUE_NAME, 'yellow' - In TRUE_NAME but incorrect position, 'green' - In TRUE_NAME and correct position
def color_tiles(answer, guess):
    colors = []
    answer_array = list(answer)
    for i in range(len(answer) - 1):
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
#def play_femdle():
#    true_name = pick_random_name().upper()
#    true_name_arr = list(true_name)
#    attempt = 0
#    guess_colors = list(true_name)

#    while attempt < 6:
#        guess_name = "Sunmi"
#        guess_name_arr = list(guess_name)
#        colors = color_tiles(true_name_arr, guess_name_arr)
#        guess_colors = guess_colors.with_row(colors)
#        if guess_name == guess_name:
#            break
#        else:
#            attempt += 1
#            if attempt == 6:
#                break


@app.route('/')
def test():
    #output = request.get_json()
    return render_template('frontend.html')

#if __name__ == '__main__':
#    play_femdle()
        


    
