from flask import Flask,jsonify,request
from flask_restful import Resource, Api

from source import users

app=Flask(__name__)
api=Api(app)

"""----------users---------"""

api.add_resource(users.Adduser, '/users/adduser')
api.add_resource(users.Login, '/users/login')
api.add_resource(users.ChangePass, '/users/changepass')


"""--------Ideas----------"""




if __name__=='__main__':
	app.run(debug=True)