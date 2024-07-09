from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        message = request.form['message']

        # Process the data (e.g., print it)
        print(f"Received data: First Name: {first_name}, Last Name: {last_name}, Email: {email}, Message: {message}")

        return redirect(url_for('success'))
    else:
        return "Invalid request"

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
