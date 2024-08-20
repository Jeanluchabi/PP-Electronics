from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a real secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pnp_electronics.db'
db = SQLAlchemy(app)

# Define models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Initialize the database (Run this once to create the database)
@app.before_first_request
def create_tables():
    db.create_all()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/account', methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'login':
            email_or_phone = request.form['emailOrPhone']
            password = request.form['password']
            user = User.query.filter((User.email == email_or_phone) | (User.phone == email_or_phone)).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                flash('Login successful!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid credentials!', 'danger')
        elif action == 'register':
            full_name = request.form['fullName']
            email = request.form['email']
            phone = request.form['phone']
            dob = datetime.strptime(request.form['dob'], '%Y-%m-%d')
            gender = request.form['gender']
            password = request.form['password']
            confirm_password = request.form['confirmPassword']
            if password != confirm_password:
                flash('Passwords do not match!', 'danger')
                return redirect(url_for('account'))
            hashed_password = generate_password_hash(password, method='sha256')
            new_user = User(full_name=full_name, email=email, phone=phone, dob=dob, gender=gender, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
        elif action == 'reset_password':
            email = request.form['resetEmail']
            # Implement password reset logic here
            flash('Password reset email sent!', 'info')
        return redirect(url_for('account'))
    return render_template('account.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/product/<product_name>')
def product(product_name):
    # Ensure that the product page exists in the templates folder
    try:
        return render_template(f'{product_name}.html')
    except:
        return render_template('404.html'), 404

@app.route('/payment')
def payment():
    return render_template('payment.html')

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
