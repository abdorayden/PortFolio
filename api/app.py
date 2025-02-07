from flask import Flask, request, jsonify , render_template_string
import random

app = Flask(__name__, static_folder='../static', template_folder='../templates')

# vercel doesn't allow me to write a file sooo 1000 quote gonna be fine 
# i just wanted to share with you guys
quotes = { 
          1 : "just be positive :)",
          2 : "everything is gonna be  fine :)))"
}
count = 3

@app.route('/raylist')
def raylist() :
    with open('templates/projects/raylist.html') as f :
        chtml = f.read()
    return render_template_string(chtml)

@app.route('/raylist/future')
def future() :
    with open('templates/projects/future.html') as f :
        chtml = f.read()
    return render_template_string(chtml)

@app.route('/')
def index() :
    with open('templates/index.html') as f :
        chtml = f.read()
    return render_template_string(chtml)

@app.route('/submit', methods=['POST'])
def submit():
    global quotes
    global count
    data = request.json
    content = data.get('content', '')

    if len(quotes) <= 1000 :
        content = "".join([
            char for char in content
            if char not in ["<" , ">"]
        ])
        quotes[count] = content
        count += 1

    return jsonify({'message': "ok"}), 200

@app.route('/quote')
def random_quote() :
    global quotes
    global count
    q = quotes.get(random.randrange(1 , count))
    return jsonify({'quote': q}), 200

if __name__ == '__main__':
    app.run()
