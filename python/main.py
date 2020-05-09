from bottle import Bottle, request, route, run, static_file

STATIC_PATH = '/home/peter/projects/homeserver/website'

app = Bottle()

@app.route('/api')
def surprise():
    return 'Some data...'

@app.route('/')
@app.route('/<filename>')
def server_static(filename='index.html'):
    return static_file(filename, root=STATIC_PATH)

app.run(host="localhost", port=8080, debug=True)
