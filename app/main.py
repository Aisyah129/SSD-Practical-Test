from flask import Flask, request, render_template, redirect, url_for
import re

app = Flask(__name__)

def is_xss(payload):
    return bool(re.search(r'(<script|on\w+=|javascript:)', payload, re.IGNORECASE))

def is_sql_injection(payload):
    return bool(re.search(r"(?:')|(?:--)|(/\*)|(\*/)|(\b(select|union|insert|delete|update|drop|where)\b)", payload, re.IGNORECASE))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        term = request.form.get('search_term', '')
        if is_xss(term) or is_sql_injection(term):
            return redirect(url_for('index'))
        return render_template('result.html', term=term)
    return render_template('index.html')

@app.route('/result')
def result():
    return redirect(url_for('index'))  # fallback

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
