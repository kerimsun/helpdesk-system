from flask import Flask, render_template_string

app = Flask(__name__)

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>IT Help Desk</title>
</head>
<body>

<h1>IT Help Desk System</h1>

<p>Flask is running successfully!</p>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(LOGIN_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
