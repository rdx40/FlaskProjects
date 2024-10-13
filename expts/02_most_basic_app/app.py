from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get('name')  
        return render_template("display_details.html", display_name=name)
    return render_template("get_details.html")

if __name__ == '__main__':
    app.run(debug=True)

