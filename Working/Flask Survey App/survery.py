from flask import Flask, render_template , request, redirect, url_for
import os
from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/Special_invi'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    number_=db.Column(db.Integer, unique=True)
    name_ = db.Column(db.String(120))
    def __init__(self, email_, name_,number_):
        self.email_=email_
        self.name_=name_
        self.number_ = number_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/thanks", methods = ['POST', "GET"])
def thanks():
    if request.method == "POST":
        email, name, number =  request.form.get("email"), request.form.get("users_name"), request.form.get("u_number")
        if db.session.query(Data).filter(Data.email_ == email).count()== 0:
            data=Data(email,name,number)
            db.session.add(data)
            db.session.commit()
            send_email(email,name,number)
            print(number)
            return render_template("thanks.html")
        return render_template('index.html', text="Seems like we got something from that email once!")
    else:
        return redirect(url_for('home'))

def main():
    app.debug = True
    app.run(port = 7894)

if __name__ == '__main__':
    main()