from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/nuclear")
def render_nuclear():
    return render_template('Nuclear.html')
    
if __name__=="__main__":
    app.run(debug=True)
