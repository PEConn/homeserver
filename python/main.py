from bottle import Bottle, request, route, run, static_file
import json

from logic import model

STATIC_PATH = '/home/peter/projects/homeserver/website'

app = Bottle()

@app.route('/api')
def root():
    return 'Some data...'

@app.route('/api/mealplan')
def meal_plan():
    return json.dumps(model.getPlan())

@app.route('/')
@app.route('/<filename>')
def server_static(filename='index.html'):
    return static_file(filename, root=STATIC_PATH)

app.run(host="localhost", port=8080, debug=True)
