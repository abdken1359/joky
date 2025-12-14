from quart import Quart
from blueprints import api,a
app = Quart(__name__)

app.register_blueprint(a)
app.register_blueprint(api)


