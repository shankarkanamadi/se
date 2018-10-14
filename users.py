from flask import Flask,jsonify,request
from flask_restful import Resource, Api
from pymongo import MongoClient

app=Flask(__name__)
api=Api(app)

conn=MongoClient("mongodb://localhost:27017/")
usercollection=conn["userdb"]
userdb=usercollection["users"]


"""  User add to mongodb database """
@app.route('/adduser',methods=['post'])
def post():
	userdata = {
			'name':request.form['username'] ,
			'password':request.form['pass'],
			'email':request.form['email']
	}
	x1=userdb.insert_one(userdata)
	if x1:
		return "Inserted"
	else:
		return "something worng"


"""  User Authentication  """
@app.route('/authenticate',methods=['post'])
def check_user():
	query={
		'name':request.form['username'],
		'password':request.form['pass']
	}
	user=userdb.find_one(query)
	if user:
		user['_id']=str(user['_id'])
		return jsonify(user)
	else:
		return "Invalid user"
		
if __name__=='__main__':
	app.run(debug=True)

