from flask_restful import Resource
from flask import Flask,jsonify,request
from flask-login import
from pymongo import MongoClient

conn=MongoClient("mongodb://localhost:27017/")
usercollection=conn["userdb"]
userdb=usercollection["users"]



class Adduser(Resource):
	def post(self):
		userdata = {
			'username':request.form['username'] ,
			'password':request.form['pass'],
			'email':request.form['email']
		}
		x1=userdb.insert_one(userdata)
		if x1:
			return jsonify({"message":"Inserted"})
		else:
			return jsonify({"message":"Something error"})


class Login(Resource):
	def post(self):
		query={
			'username':request.form['username'],
			'password':request.form['pass'],
		}
		user=userdb.find_one(query)
		if user:
			user['_id']=str(user['_id'])
			return jsonify({"message":"sucsess","username":request.form['username'],"user":user})
		else:
			return jsonify({"message":"Invalid User"})


class ChangePass(Resource):
	def post(self):
		user=userdb.update_one(
			{
				'username':request.form['old_uname'],
	 			'password':request.form['old_pass']
			},{
				'$set':{
	 			'password':request.form['new_pass']
			}})
		if user:
			return jsonify({"message":"success"})
		else:
			return jsonify({"message":"unsuccess"})