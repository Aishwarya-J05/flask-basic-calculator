from flask import Flask, render_template, request

app = Flask(__name__)

# Define operations
def add(n1, n2): return n1 + n2
def subtract(n1, n2): return n1 - n2
def multiply(n1, n2): return n1 * n2
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "Error"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        expression = request.form.get("expression", "")
        try:
            result = f"{expression} = {eval(expression)}"
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)