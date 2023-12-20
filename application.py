from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "<b><font color=blue>Hello, world from FLASK!</font></b>"

@application.route("/admin")
def index_admin():
    return "This will Admin panel"


@application.route("/user")
def index_users():
    return "User pages"

@application.route("/user/<username>")
def show_user(username):
    return "Hello " + username.upper()

@application.route("/path/<path:subpath>")
def show_subpath(subpath):
    return "Subpath is " + subpath

@application.route("/calc/<int:x>")
def show_calc(x):
    return  "Kvadrat ot chisla " + str(x) + " =  " + str(x*x)

@application.route("/htmlpage")
def show_htmlpage():
    myfile = open("mypage.html", mode="r")
    page   = myfile.read()
    myfile.close()
    return page

#----------------------------------------------------------------

if __name__ == "__main__":
#    application.debug = True
#    application.env = "Working environment"
    application.run()

