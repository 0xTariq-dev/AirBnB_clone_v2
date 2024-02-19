#!/usr/bin/python3
"""A simple Flask app with a single route."""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/', strict_slashes=False, methods=['GET'])
def hello_hbnb():
    """Return a string at the root URL."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False, methods=['GET'])
def hbnb():
    """Return a string at the /hbnb URL."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False, methods=['GET'])
def c_is_fun(text):
    """Return a string at the /c/<text> URL."""
    return 'C %s' % text.replace("_", " ")


@app.route('/python/',
           defaults={'text': 'is cool'},
           strict_slashes=False, methods=['GET'])
@app.route('/python/<text>', strict_slashes=False, methods=['GET'])
def python_is_cool(text):
    """Return a string at the /python/<text> URL."""
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False, methods=['GET'])
def number(n):
    """Return a string at the /number/<n> URL."""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False, methods=['GET'])
def number_template(n):
    """Return an HTML page at the /number_template/<n> URL."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>',
           strict_slashes=False, methods=['GET'])
def number_odd_or_even(n):
    """Return an HTML page at the /number_odd_or_even/<n> URL."""
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False, methods=['GET'])
def states_list():
    """Return an HTML page at the /states_list URL."""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states.values())


@app.route('/cities_by_states', strict_slashes=False, methods=['GET'])
def cities_by_states():
    """Return an HTML page at the /cities_by_states URL."""
    states = storage.all(State)
    cities = storage.all(City)
    return render_template('8-cities_by_states.html', states=states.values())


@app.route('/states', strict_slashes=False, methods=['GET'])
def states():
    """Return an HTML page at the /states URL."""
    states = storage.all(State)
    return render_template('9-states.html', states=states.values())


@app.route('/states/<id>', strict_slashes=False, methods=['GET'])
def states_by_id(id=None):
    """Return an HTML page at the /states/<id> URL."""
    states = storage.all(State)
    state = None
    for s in states.values():
        if s.id == id:
            state = s
            break
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
