from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', data=["1","2","3"])

@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]