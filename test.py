from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


mybooks=[]
myusers=[]


class BooksAPI(Resource):
    def getBooks(self):
        if len(mybooks):
            return {"books":mybooks}
        else:
            return {"books":"No books were found"}
    
class MyBook(Resource):
    """ Handle books CRUDS """
    def get(self,bookId):
        """Get single Book"""
        for i,j in enumerate(mybooks):
            if i==bookId:
                return {"book":j},200
            else:
                return {"book":"That book does not exist"},404
    def post(self):
        """ADD a book"""
        status=False
        bk=request.get_json()
        if mybooks:
            for i,j in mybooks:
                if i==bk['bookId']:
                    status=True
                    break
            if status:
                return {"message":"That book already exists"},201                
            mybooks.append(bk)
            return {"book":bk},200
        else:
            return {"message":"That book could not be found"},404 
        
    def delete(self,bookId):
        if mybooks:
            mybooks.remove(bookId)
            return {"message":"That book has been deleted"},201
        else:
             return {"message":"That book could not be deleted"},404 
    
    def put(self,bookId):
        book=request.get_json()
        if book is None:
            return {"message":"Please specify a book attributes"}
        else:
            mybooks.append({"bookId":bookId,"title":book['title']})
            return book,200