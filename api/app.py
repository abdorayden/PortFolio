from flask import Flask, request, jsonify , render_template_string

app = Flask(__name__, static_folder='../static', template_folder='../templates')

@app.route('/raylist')
def raylist() :
    with open('templates/projects/raylist.html') as f :
        chtml = f.read()
    return render_template_string(chtml)

@app.route('/raylist/future')
def raylist() :
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
    data = request.json
    content = data.get('content', '')
    try :
        with open('quotes/quote.txt', 'a') as file:
            file.write("\n" + content + "\n")
    except Exception as err:
        return jsonify({'message': err}), 404

    return jsonify({'message': "ok"}), 200

if __name__ == '__main__':
    app.run()
