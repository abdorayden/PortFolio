from flask import Flask, request, jsonify , render_template_string

app = Flask(__name__)

@app.route('/')
def index() :
    with open('templates/index.html') as f :
        chtml = f.read()
    return render_template_string(chtml)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    content = data.get('content', '')
    with open('quotes/quote.txt', 'a') as file:
        file.write("\n" + content + "\n")
    return jsonify({'message': content}), 200

if __name__ == '__main__':
    app.run(port = 80)
