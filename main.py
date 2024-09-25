from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap5
from form import MorseForm
from flask_wtf.csrf import CSRFProtect
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config['SECRET_KEY'] = os.environ.get('CSRF_KEY')

csrf = CSRFProtect(app)

MORSE_CODE = {
                'a': '.-',
                'b': '-...',
                'c': '-.-.',
                'd': '-..',
                'e': '.',
                'f': '..-.',
                'g': '--.',
                'h': '....',
                'i': '..',
                'j': '.---',
                'k': '-.-',
                'l': '.-..',
                'm': '--',
                'n': '-.',
                'o': '---',
                'p': '.--.',
                'q': '--.-',
                'r': '.-.',
                's': '...',
                't': '-',
                'u': '..-',
                'v': '...-',
                'w': '.--',
                'x': '-..-',
                'y': '-.--',
                'z': '--..',
                '1': '.----',
                '2': '..---',
                '3': '...--',
                '4': '....-',
                '5': '.....',
                '6': '-....',
                '7': '--...',
                '8': '---..',
                '9': '----.',
                '0': '-----',
                '/': '/'
              }


@app.route("/", methods=['GET','POST'])
def home():
    form = MorseForm()
    if form.validate_on_submit():
        try: 
            message = [form.text_to_morse.data.replace(" ", "/").lower()] 
            morse = [MORSE_CODE[letter] for letter in message[0] if MORSE_CODE[letter]]
            converted_list = map(str, morse)
            result = ''.join(converted_list)
            form.text_to_morse.data = result
            return render_template('index.html', form=form)
        except KeyError:
            flash("Please insert a valid message, Symbols aren't accepted yet... ")
            return redirect(url_for('home'))
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()