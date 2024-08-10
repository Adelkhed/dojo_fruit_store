from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    
    data=dict(request.form)
    print(request.form)
    print(data)
    data['total'] =int(data['strawberry'])+int(data['raspberry'])+int(data['apple'])
    now = datetime.now()
    current_time= now.strftime("%B  %drd %Y on %I:%M:%S %p ")
    return render_template("checkout.html",data=data, current_time=current_time)

@app.route('/fruits')         
def fruits():
    
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    