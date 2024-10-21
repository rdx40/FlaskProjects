import os
import uuid
from flask import Flask, render_template,request, Response, send_from_directory,jsonify
import pandas as pd


app=Flask(__name__,template_folder='templates')

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        username = request.form['username'] #or request.form.get('username')
        password = request.form['password']

        if username == 'omar' and password == 'password':
            return "success"
        else:
            return "failure"

@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    
    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()
    
@app.route('/convert_csv',methods=['POST'])
def convert_csv():
    file = request.files['file']
    df = pd.read_excel(file)
    response = Response(df.to_csv(),
                        mimetype='text/csv',
                        headers={
                        'Content-Disposition': 'attachment; filename=data.csv'
                    
                    }
    )
    return response


@app.route('/convert_csv_two',methods=['POST'])
def convert_csv_two():
    file  = request.files['file']
    df = pd.read_excel(file)
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads',filename))

    return render_template('download.html',filename=filename)
    
@app.route('/download/,<filename>')
def download(filename):
    return send_from_directory('downloads',filename, download_name='result.csv')

@app.route('/handle_post', methods=['POST'])
def handle_post():
    name = request.json.get('name')
    greeting = request.json.get('greeting')  # Fixed key name

    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}')

    return jsonify({'message': 'Successfully written!'})  # Ensure the response is JSON


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
