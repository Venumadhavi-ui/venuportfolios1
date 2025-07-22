import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB limit
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Store submitted form data
submitted_data = {}

# Portfolio list (20 portfolios)
portfolios = [
    {
        "id": i,
        "name": f"Person {i}",
        "role": f"Role {i}",
        "image": f"images/portfolio{i}.jpg",
        "resume": f"resumes/resume{i}.pdf",
        "email": f"person{i}@example.com",
        "phone": f"+91-90000000{i:02}",
        "location": f"City {i}, India",
        "bg_class": f"bg{i % 5}",  # 5 background styles
        "gender": "Female",  # default gender
        "bio": "Passionate full-stack developer.",
        "age": 28
    }
    for i in range(1, 21)
]

# Allowed image file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html', portfolios=portfolios)


@app.route('/portfolio/<int:portfolio_id>', methods=['GET', 'POST'])
def portfolio(portfolio_id):
    portfolio = next((p for p in portfolios if p['id'] == portfolio_id), None)
    if not portfolio:
        return "Portfolio not found", 404

    if request.method == 'POST':
        # Save uploaded profile image
        if 'profile_image' in request.files:
            file = request.files['profile_image']
            if file and allowed_file(file.filename):
                filename = secure_filename(f"portfolio{portfolio_id}.jpg")
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                portfolio['image'] = f"images/{filename}"

        # Save gender, bio, and interests
        submitted_data[portfolio_id] = {
            "gender": request.form.get("gender"),
            "interests": request.form.getlist("interests"),
            "bio": request.form.get("bio")
        }

    return render_template(
        f'portfolio{portfolio_id}.html',
        portfolio=portfolio,
        data=submitted_data.get(portfolio_id)
    )


@app.route('/portfolio/<int:portfolio_id>/details', methods=['GET', 'POST'])
def portfolio_details(portfolio_id):
    portfolio = next((p for p in portfolios if p["id"] == portfolio_id), None)
    if not portfolio:
        return "Portfolio not found", 404

    if request.method == "POST":
        submitted_data[portfolio_id] = {
            "gender": request.form.get("gender"),
            "interests": request.form.getlist("interests"),
            "bio": request.form.get("bio")
        }
        return redirect(url_for('portfolio_details', portfolio_id=portfolio_id))

    return render_template(
        f"portfolio{portfolio_id}_details.html",
        portfolio=portfolio,
        data=submitted_data.get(portfolio_id)
    )


if __name__ == '__main__':
    app.run(debug=True)
