from flask import Flask, render_template

app = Flask(__name__)

# Sample data
programs = [
    {'name': 'Program 1', 'description': 'Description 1', 'download_link': '#'},
    {'name': 'Program 2', 'description': 'Description 2', 'download_link': '#'}
]

@app.route('/')
def index():
    return render_template('index.html', programs=programs)

@app.route('/program/<name>')
def program(name):
    program = next((prog for prog in programs if prog['name'] == name), None)
    return render_template('program.html', program=program)

if __name__ == '__main__':
    app.run(debug=True)

