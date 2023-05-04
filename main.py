from flask import Flask, jsonify, render_template
from flask_limiter import Limiter
import random

app = Flask(__name__)

limiter = Limiter(app)

with open("data/thirty.txt") as jokes:
    darkjokes_text = jokes.read()

with open("data/jokes.txt", encoding='utf-8') as j:
    jokes_text = j.read()

with open("data/questions.txt") as q:
    questions = q.read()

with open("data/facts.txt") as f:
    questions = f.read()

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/darkjoke')
@limiter.limit("100/minute")
def darkjoke():
    jokes_list = darkjokes_text.splitlines()
    selected_joke = random.choice(jokes_list)
    joke_parts = selected_joke.split('?')
    joke_setup = joke_parts[0]
    joke_punchline = joke_parts[1]
    return jsonify({
        'punchline': joke_punchline.strip(),
        'buildup': joke_setup.strip()
    })

@app.route('/api/joke')
@limiter.limit("100/minute")
def joke():
    jokes_list = jokes_text.splitlines()
    selected_joke = random.choice(jokes_list)
    joke_parts = selected_joke.split('?')
    if len(joke_parts) >= 2:
        joke_setup = joke_parts[0]
        joke_punchline = joke_parts[1]
    else:
        joke_setup = selected_joke
        joke_punchline = ""
    return jsonify({
        'punchline': joke_punchline.strip(),
        'buildup': joke_setup.strip()
    })


@app.route('/api/question')
@limiter.limit("100/minute")
def question():
    question_list = questions.splitlines()
    selected_question = random.choice(question_list)
    return jsonify({
        'question': selected_question
    })

@app.route('/api/fact')
@limiter.limit("100/minute")
def fact():
    fact_list = questions.splitlines()
    selected_fact = random.choice(fact_list)
    return jsonify({
        'fact': selected_fact
    })

if __name__ == '__main__':
    app.run('0.0.0.0')
