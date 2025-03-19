from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'Hare_Krishna08'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(70), nullable=False)
    
class RegisterForm (FlaskForm): 
    
    def validate_user(self, username):
        existing_user_name = User.query.filter_by(
            username = username.data).first()
        if existing_user_name:
            raise ValidationError(
                "This <span style='color:blue'>username</span> is already taken, try a different name"
            )
    username = StringField(
        "Username", 
        validators=[InputRequired(), Length(min=4, max=20), validate_user],
        render_kw={"placeholder": "Username"}
    )
    password = PasswordField(
        "Password", 
        validators=[InputRequired(), Length(min=4, max=20)], 
        render_kw={"placeholder": "Password"}
    )
    submit = SubmitField("Register")
            
class LoginForm (FlaskForm): 
    username = StringField(validators=[ InputRequired(), Length( 
        min=4, max=20)], render_kw={"placeholder": "Username"}) 
    password = PasswordField(validators=[ InputRequired(), Length( 
        min=4, max=20)], render_kw={"placeholder": "Password"}) 
    submit = SubmitField("Login")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form = form)

@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
    form  = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('sign_up.html', form = form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout', methods = ['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)