from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

#Python Flask Tutorial: Full-Featured Web App Part 3 - Forms and User Input
##https://www.youtube.com/watch?v=UIJKdCIEXUQ&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=3

app = Flask(__name__)

#Change to env variable later
app.config['SECRET_KEY'] = 'e45e849025221566c85d306b4f45996a'

posts = [
    {
        'author': 'Larry Ullman',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018',
    },
]

@app.route('/')
@app.route('/home')
def home():
    #name = request.args.get("name", "World")
    #return f'Hello, {escape(name)}!'
    #return "Hello World!"
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'admin':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))

        else:
            flash('Login Unsuccessfull. Please check email and password', 'danger')

    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)