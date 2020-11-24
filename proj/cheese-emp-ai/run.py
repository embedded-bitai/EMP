from main import app

app.run(host='127.0.0.1' , port='8080', debug=True)



# from flask import Flask, render_template, request
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)
 
# class Rest(Resource):
#     def get(self):
#         return {'rest': 'Good !'}
#         # return Emotion()
#     def post(self):
#         return {'rest': 'post success !'}
# api.add_resource(Rest, '/api')
 
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port='8080', debug=True)





# # main.py
# from flask import Flask
# from flask_restful import Resource, Api
# from hello import HelloWorld

# app = Flask(__name__)
# api = Api(app)

# api.add_resource(HelloWorld, '/wwo')

# if __name__=='__main__':
#     app.run(debug=True)


# # hello.py
# from flask_restful import Resource

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello':'world!'}