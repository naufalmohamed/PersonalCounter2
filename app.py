from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Get the 'date' and 'target' from the query parameters, with default values.
    date_one = request.args.get('date', '12/28/2022')  # Default to '12/28/2022' if no date is provided
    target = request.args.get('target', 100)
    
    # Get the 'counter_name' from the query parameters, with a default value.
    counter_name = request.args.get('counter_name', 'Retention Counter')
    
    return render_template('index.html', date_one=date_one, target=target, counter_name=counter_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
