from flask import Flask, render_template


site = Flask(__name__)

@site.route('/') #main project page, got from base.html
def app():
    return render_template("app.html")


@site.route('/info')
def info():
    return render_template("index.html") #first info page

@site.route('/developer')
def developer():
    return render_template("info.html") # dev info, got from base.html


@site.route('/u/<string:username>/<int:id>') #admin page when site/u/admin/300403
def loginAdmin(username, id):
    if username == "admin" and id == 300403:
        return "root activated: " + username
    else:
        return "wrong username or password"

if __name__ == "__main__": #hosting and debugger mode trigger
    site.run(debug=True)
