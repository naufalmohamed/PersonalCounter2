from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    date_one = request.args.get('date', '12/28/2022')  # Default to '12/28/2022' if no date is provided
    target = request.args.get('target', 100)
    return render_template('index.html', date_one=date_one, target=target)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
