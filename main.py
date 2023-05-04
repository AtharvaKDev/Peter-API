from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

with open("data/thirty.txt") as jokes:
    darkjokes_text = jokes.read()

with open("data/jokes.txt", encoding='utf-8') as j:
    jokes_text = j.read()

with open("data/questions.txt") as q:
    questions = q.read()

with open("data/facts.txt") as f:
    facts = f.read()

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/darkjoke')
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
def question():
    question_list = questions.splitlines()
    selected_question = random.choice(question_list)
    return jsonify({
        'question': selected_question
    })

@app.route('/api/fact')
def fact():
    fact_list = facts.splitlines()
    selected_fact = random.choice(fact_list)
    return jsonify({
        'fact': selected_fact
    })

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
