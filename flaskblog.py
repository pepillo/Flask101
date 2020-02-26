from flask import Flask, escape, request

#Python Flask Tutorial: Full-Featured Web App Part 1 - Getting Started
##https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2&t=1s

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
    #return "Hello World!"

@app.route('/about')
def about():
    return "About Page"

if __name__ == '__main__':
    app.run(debug=True)