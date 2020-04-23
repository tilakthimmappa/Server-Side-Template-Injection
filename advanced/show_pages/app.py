from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os
from jinja2 import Environment

app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY_HMAC'] = 'secret'
app.config['SECRET_KEY_HMAC_2'] = 'am0r3C0mpl3xK3y'
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
app.config['STATIC_FOLDER'] = None
app.config['Environment'] = os.environ
Jinja2 = Environment()
app.debug = False
app.config['MONGODB_SETTINGS'] = {
    'db': 'ctf5',
    'host': 'db_host',
    'port': 'db_port',
    'username': 'db_user',
    'password': 'db_pass'
}
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{0}".format(os.path.join(project_dir, "show_content.sqlite"))
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)


class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    body = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return '<Pages : id={0}, title={1}, body={2}>'.format(self.id, self.title, self.body)


@app.route('/create_page', methods=['GET', 'POST'])
def create_page():
    db.create_all()
    # https: // cdn - images - 1.
    # medium.com / max / 1600 / 0 * GEsDQGQ1BucUNW1g
    if request.method == 'GET':
        return render_template('create_page.html')
    elif request.method == 'POST':
        title = request.form['title']
        body = Jinja2.from_string(request.form['body']).render()
        page = Pages(title=title, body=body)
        db.session.add(page)
        db.session.commit()
        return redirect('/page/{0}'.format(page.id))
    else:
        return redirect('/error/')


@app.route('/', methods=['GET'])
def home_page():
    db.create_all()
    if request.method == 'GET':
        pages = db.session.query(Pages).all()
        return render_template('home.html', output=pages)\


@app.route('/page/<int:page_id>', methods=['GET'])
def individual_page(page_id):
    db.create_all()
    if request.method == 'GET':
        pages = db.session.query(Pages).filter_by(id=page_id).first()
        return render_template('page.html', page=pages)


@app.route('/delete/<int:page_id>', methods=['GET'])
def delete_page(page_id):
    db.create_all()
    if request.method == 'GET':
        db.session.query(Pages).filter_by(id=page_id).delete()
        db.session.commit()
        return redirect('/')


@app.route("/ssti")
def ssti():

    name = request.values.get('name')
    
    # SSTI VULNERABILITY
    # The vulnerability is introduced concatenating the
    # user-provided `name` variable to the template string.
    output = Jinja2.from_string('Hello ' + name + '!').render()
    
    # Instead, the variable should be passed to the template context.
    # Jinja2.from_string('Hello {{name}}!').render(name = name)

    return output


def init_db():
    db.create_all()


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
