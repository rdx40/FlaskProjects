from flask import Flask,request, make_response

app=Flask(__name__)



@app.route('/')
def index():
    return "<h1>Base Page</h1>"

@app.route('/hello')
def hello():
    response = make_response("Hello World\n")
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    #return "<h1>Hello World</h1>"
    return response

# @app.route('/xyz',methods=['GET','POST'])
# def hello():
#     if request.method == 'GET':
#         return "Thanks for the GET request\n"
#     elif request.method == 'POST':
#         return "You just sent a POST request\n"
#     else:
#         return "You will never see me unless I add you to the methods permiited \n"


@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1} + {number2} = {number1 + number2}'

@app.route('/handle_url_params')
def handle_params():
    #return str(request.args)
    ##http://127.0.0.1:5555/handle_url_params?name=omar&greeting=kys
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        #or this either works greeting = request.args.get['greeting']
        name = request.args.get('name')
        return f"{greeting}, {name}"
    else:
        return "Some params are missing"



if __name__=='__main__':
    app.run(host='0.0.0.0', port=6969, debug=True)