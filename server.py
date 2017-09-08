from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
      return render_template("index.html")


@app.route('/submitform', methods=['POST'])
def submitform():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comments = request.form["comments"]

    print name, location, language, comments
    # return render_template("results.html")
    return render_template("results.html", name=name, location=location, language=language, comments=comments)

app.run(debug=True) # run our server