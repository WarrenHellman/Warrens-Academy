from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def varName():
    return render_template("index.html", name="Warren")

app.run(debug=True)