from flask import Flask, render_template, request

app = Flask(__name__)

"""
@app.route('/', method="GET")
def home():
    return render_template('index.html')

@app.route('/meeting-details', method="GET")
def meetingdetails():
    return render_template('meeting-details.html')

@app.route('/meetings', method="GET")
def meetings():
    return render_template('meetings.html')
"""
@app.route('/', methods=['GET', 'POST'])
def meetings():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # Handle POST request here
        name = request.form['name']
        email = request.form['email']
        # Do something with the data, e.g., save to a database
        return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
