from flask import Flask, request, render_template
from jinja2 import Environment

app = Flask(__name__)
Jinja2 = Environment()

@app.route('/',methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
        output = "Welcome to Server Side Template Injection"
        is_value = False
        return  render_template('home.html', output=output,is_value=is_value)
    else:
        name = request.values.get('name', None)
        output = Jinja2.from_string('Hello ' + name + '!').render()
        is_value = True
        return render_template('home.html', output=output,is_value=is_value)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
