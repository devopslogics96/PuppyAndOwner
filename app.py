from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///puppypal.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ----------------------
# MODELS
# ----------------------

class Puppy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100))

    owners = db.relationship("Owner", backref="puppy", lazy=True)

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    puppy_id = db.Column(db.Integer, db.ForeignKey("puppy.id"), nullable=False)

# ----------------------
# FORMS
# ----------------------

class PuppyForm(FlaskForm):
    name = StringField("Puppy Name", validators=[DataRequired()])
    breed = StringField("Breed")
    submit = SubmitField("Add Puppy")

class OwnerForm(FlaskForm):
    name = StringField("Owner Name", validators=[DataRequired()])
    email = StringField("Email")
    puppy = SelectField("Select Puppy", coerce=int)
    submit = SubmitField("Register Owner")

# ----------------------
# ROUTES
# ----------------------

@app.route("/")
def index():
    puppies = Puppy.query.all()
    return render_template("index.html", puppies=puppies)

@app.route("/add-puppy", methods=["GET", "POST"])
def add_puppy():
    form = PuppyForm()
    if form.validate_on_submit():
        puppy = Puppy(
            name=form.name.data,
            breed=form.breed.data
        )
        db.session.add(puppy)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_puppy.html", form=form)

@app.route("/add-owner", methods=["GET", "POST"])
def add_owner():
    form = OwnerForm()
    form.puppy.choices = [(p.id, p.name) for p in Puppy.query.all()]

    if form.validate_on_submit():
        owner = Owner(
            name=form.name.data,
            email=form.email.data,
            puppy_id=form.puppy.data
        )
        db.session.add(owner)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("add_owner.html", form=form)

@app.route("/puppy/<int:puppy_id>")
def puppy_detail(puppy_id):
    puppy = Puppy.query.get_or_404(puppy_id)
    return render_template("puppy_detail.html", puppy=puppy)

# ----------------------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
