from flask import Flask, jsonify, render_template, send_from_directory
import random
import json
import os

app = Flask(__name__)

with open("data/questions.json") as q:
    questions = json.load(q)

with open("data/facts.json", "r") as f:
    facts = json.load(f)

with open("data/roasts.txt") as r:
    roasts = r.read()

with open("data/darkjokes.json", "r") as g:
    darkjokes = json.load(g)

with open("data/jokes.json", "r", encoding='utf-8') as j:
    jokes = json.load(j)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/playground')
def playground():
    return render_template("playground.html")

@app.route('/api/version')
def version():
    return jsonify({
        'version' : '1.0.0',
        'Last Updated' : '4 May 2023 '
    })

@app.route('/api/darkjoke')
def darkjoke():
    random_joke = random.choice(darkjokes["jokes"])
    return jsonify({'setup': random_joke['buildup'], 'punchline': random_joke['punchline'], 'id': random_joke['id']})

@app.route('/api/joke')
def joke():
    random_joke = random.choice(jokes["jokes"])
    return jsonify({'setup': random_joke['buildup'], 'punchline': random_joke['punchline'], 'id': random_joke['id']})


@app.route('/api/question')
def question():
    random_que = random.choice(questions["questions"])
    return jsonify({'question': random_que['question'], 'id': random_que['id']})

@app.route('/api/fact')
def fact():
    random_fact = random.choice(facts["facts"])
    return jsonify({'fact': random_fact['fact'], 'id': random_fact['id']})

@app.route('/api/roast/<username>')
def roast(username):
    roast_list = roasts.splitlines()
    selected_roast = random.choice(roast_list)
    return jsonify({
        'roast': f"{username}, {selected_roast}",
        'target': username
    })

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
