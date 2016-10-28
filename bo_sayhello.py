import bottle

@bottle.route('/')
def index():
    return 'Hello world, I am bottle!'

app = bottle.default_app()
