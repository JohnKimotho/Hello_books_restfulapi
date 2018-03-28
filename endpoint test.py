class Users(Resource):
    def post(self):
        """Register user"""
        users=request.get_json()
        myusers.append(users)
        return {"message":"Registration was successful"}

class UserLogin(Resource):
    def post(self):
        """Getuser login"""
        """x=x.append({"username":"xxx","password":"sdre"},{"username":"x2","password":"sdre"})"""
        users=request.get_json()
        if users:
            for i,j in myusers:
                if users['username'] ==j['username'] and users['password'] ==j['password']:
                    return {"message":"Login is successful"}
                else:
                    return {"message":"Login was unsuccessful.That username and passsword combination."}
        else:
            return {"message":"Login was unsuccessful."}
        

class UserLogout(Resource):
    def post(self):
        pass

class UserReset(Resource):
    def post(self):
        users=request.get_json()
        for i,j in myusers:
            if users['username'] in j['username']:
                j['password']=users['password']
       
               
                
api.add_resource(BooksAPI, '/books')
api.add_resource(MyBook, '/books/<book_id>')

api.add_resource(Users, '/register/')
api.add_resource(UserLogin, 'login/')
api.add_resource(UserReset, '/reset-password/')


app.run(port=3000, debug=1)