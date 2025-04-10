from flask import Flask

app = Flask(__name__)

@app.route('/hello',methods=['GET','POST'])  
def say_hello():
    return "Hello, world! Say hello to me."

@app.route('/deepu',methods=['GET', 'POST'])
def printing_msg():
    return  "print something about me"    

if __name__ == '__main__':
    app.run(debug=True,port=5001)
