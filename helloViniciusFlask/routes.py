from flask import render_template, request
from helloViniciusFlask import app, forms

@app.route('/', methods=['GET', 'POST'])
def home():
    search_form = forms.LoginForm(request.form)
    if request.method == 'POST':
        name = request.form['name']
        name = name.upper()
        return render_template('result.html',name=name)
    return render_template('index.html',form=search_form)