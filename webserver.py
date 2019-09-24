from flask import Flask,request
from flask import render_template
from config import WEB_SERVER_PORT
#import pandas as pd

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        myfile = request.files['myfile']
        myfile.save('upload/'+myfile.filename)
        #uploadfile='upload/'+myfile.filename
        #a=pd.read_excel(uploadfile)
        #return a
    return render_template('index.html')

def start_web_server():
    app.debug = True
    app.run(host='localhost',port=WEB_SERVER_PORT)

if __name__ == '__main__':
    start_web_server()