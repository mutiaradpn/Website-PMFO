from flask import Flask, render_template, request,redirect
from module.database import Database
app = Flask(__name__)
db = Database()

@app.route('/',methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        print(request.form)
        datalogin = db.login(request.form)
        print(datalogin)
        if(datalogin == "salah password" or datalogin == "username tidak tersedia"):
            message = datalogin 
            return render_template('login.html', message = message)
        else:
            return redirect('/home')
    else:
        return render_template('login.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register",methods = ['POST', 'GET'])
def register():
    if(request.method == 'POST'):
        print(request.form)
        datalogin = db.register(request.form)
        print(datalogin)
        if(datalogin != "kosong"):
            return render_template('login.html',username = datalogin)
        else:
            message = "error saat login"
            return render_template('register.html')
    else:
        return render_template('register.html')

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/InputBER",methods = ['POST', 'GET'])
def inputBER():
    if(request.method == "POST"):
        hasilber = db.masukin_BER(request.form)
        print(hasilber)
        return render_template('inputBER.html', hasilber = hasilber)
    else:
        return render_template('inputBER.html')

@app.route("/History")
def history():
    data = db.readhistory()
    return render_template('history.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)