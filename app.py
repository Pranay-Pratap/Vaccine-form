from flask import Flask, request, flash, url_for, redirect, render_template
from flask_migrate import Migrate
from models import db, Employees

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/myVaccination"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '1234'
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def show():
   return render_template('show.html')


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['age'] or not request.form['gender'] or not request.form['vaccine']:
            flash('Please enter all the fields', 'error')
        else:
            employee = Employees(request.form['name'], request.form['age'],
                                 request.form['gender'], request.form['vaccine'])

            db.session.add(employee)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show'))
    return render_template('new.html')


if __name__ == '__main__':
    app.run(debug=True)
