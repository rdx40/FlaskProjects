from flask import Flask,render_template,redirect,url_for

app=Flask(__name__, template_folder='templates')



@app.route('/')
def index():
    myvalue = 'ramo' 
    myresult = 'Omars Coming\n'*5
    myList = [10, 20, 30, 40]
    return render_template('index.html', mylist=myList)


@app.route('/other')
def other():
    some_text = "Learning Filters I Figure"
    return render_template('other.html', some_text=some_text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))
    

@app.template_filter('reverseString')
def reverse_string(s):
    return s[::-1]


@app.template_filter('repeat')
def repeat(s,times=2): 
    return s*times

@app.template_filter('alternate_case')
def alternate_case(s):
     return ''.join(c.upper() if i%2==0 else c.lower() for i,c in enumerate(s))  

if __name__ == '__main__':
    app.run(debug=True,port=6969,host='0.0.0.0')
