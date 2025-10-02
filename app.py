from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    print(f"New Contact -> Name: {name}, Email: {email}, Message: {message}")
    return render_template('index.html', success=True)

if __name__ == '__main__':
    app.run(debug=True)
