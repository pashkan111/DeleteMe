from flask_restful import Api
from api import CheckUser, UserRegister, CheckKeyWords, Result, UserData, Test
from __init__ import create_app
from flask_restful import Api


app = create_app()
# app = Flask(__name__)
# app.secret_key = 'qwppqpje34jeejejejje12hdhd'

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@0.0.0.0:5432/deleteme"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

# from db import db
# migrate = Migrate(app, db)


api.add_resource(UserRegister, '/register')
api.add_resource(CheckUser, '/check-user')
api.add_resource(CheckKeyWords, '/check-keywords')
api.add_resource(Result, '/result')
api.add_resource(UserData, '/user-data')
api.add_resource(Test, '/test')
# db.init_app(app)
# db.create_all()

if __name__ == '__main__':
    app.run(host='172.21.0.3', port=8200, debug=True)
