from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    names = ["Miscar", "Steampunk", "Orbit", "Joker"]
    return render_template(
        "index.html",
        names=names,
        no_names = False)

if __name__ == '__main__':
   app.run(debug = True)