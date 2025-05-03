from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fancy App Form</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(to right, #e0eafc, #cfdef3);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .container {
            margin-top: 5%;
            padding: 30px;
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        h1 {
            color: #007bff;
        }
        .result {
            padding: 20px;
            background-color: #f1f8ff;
            border-left: 5px solid #0d6efd;
            margin-top: 20px;
        }
    </style>
</head>
<body>
<div class="container">
    <h1 class="text-center">🚀 Welcome to the Fancy App Form</h1>
    <form method="post" action="/">
        <div class="mb-3">
            <label for="name" class="form-label">👤 Name:</label>
            <input type="text" class="form-control" id="name" name="name" required placeholder="Enter your name">
        </div>
        <div class="mb-3">
            <label for="email" class="form-label">📧 Email:</label>
            <input type="email" class="form-control" id="email" name="email" required placeholder="Enter your email">
        </div>
        <div class="mb-3">
            <label for="color" class="form-label">🎨 Favorite Color:</label>
            <input type="color" class="form-control form-control-color" id="color" name="color" value="#563d7c" title="Choose your color">
        </div>
        <button type="submit" class="btn btn-primary w-100">Submit 🚀</button>
    </form>

    {% if result %}
    <div class="result mt-4">
        <h4>🎉 Hello {{ result.name }}!</h4>
        <p>We've sent a confirmation to <strong>{{ result.email }}</strong>.</p>
        <p>Your favorite color is <span style="color: {{ result.color }};"><strong>{{ result.color }}</strong></span>.</p>
    </div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        result = {
            "name": request.form["name"],
            "email": request.form["email"],
            "color": request.form["color"]
        }
    return render_template_string(HTML_FORM, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
