from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    languages=[]
    return render_template("form.html",languages=languages)

@app.route("/<string:name>")
def helloda(name):
    return f"Hello, {name}"

@app.route("/hello",methods=["POST"])
def hello():
    name=request.form.get("name")
    lastname=request.form.get("lastname")
    occupation=request.form.get("occupation")
    number=request.form.get("number")
    email=request.form.get("email")
    date=request.form.get("date")
    nationality=request.form.get("nationality")
    n_ingles=request.form.get("n_ingles")
    languages = request.form.getlist('languages')
    habilidades = request.form.getlist('habilidades')
    perfil=request.form.get("perfil")
    return render_template("index.html"
    ,nombre=name
    ,apellido=lastname
    ,ocupacion=occupation
    ,numero=number
    ,email=email
    ,date=date
    ,nacionalidad=nationality
    ,n_ingles=n_ingles
    ,lenguajes=languages
    ,lenl=len(languages)
    ,habilidades=habilidades
    ,lenh=len(habilidades)
    ,perfil=perfil
    )