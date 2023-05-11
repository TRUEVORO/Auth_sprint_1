from flask import Flask

from api.v1 import admin_routes, auth_routes
from extensions import db, init_db, init_jwt, init_migrate, init_swagger

app = Flask(__name__)

app.register_blueprint(admin_routes)
app.register_blueprint(auth_routes)

init_db(app)
init_jwt(app)
init_migrate(app, db)
init_swagger(app)

if __name__ == '__main__':
    app.run(debug=True)
