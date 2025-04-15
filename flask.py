from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    email = request.form.get('email')
    return f"Registered {first_name} {last_name} with email {email}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)