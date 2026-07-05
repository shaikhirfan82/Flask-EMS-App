from flask import Flask, render_template, request, redirect, url_for
from models import db, Employee

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db.init_app(app)

@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    role = request.form['role']
    new_emp = Employee(name=name, role=role)
    db.session.add(new_emp)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_employee(id):
    emp = Employee.query.get(id)
    db.session.delete(emp)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
