from sanic import Sanic
from sanic.response import redirect 
from sanic_jinja2 import SanicJinja2

app = Sanic("Hej")
app.static("/static", "./static")
jinja = SanicJinja2(app)

#TODO: Installer de nødvendige biblioteker:
# pip install Sanic
# pip install SanicJinja2


#TODO: jeres dict "globals" skal indeholde en key "number" og en tilsvarende værdi 0

globals = {}

#Dette endpoint giver en respons ved en http GET request der peger på "localhost:8080/"
#Responsen svarer til indholdet af index.html og pga. at index.html er et jinja template, 
#vil jeres dicts værdier kunne bruges i html-filen. 
@app.get("/")
@jinja.template("index.html")
async def index(request):
    #TODO: Returner jeres dictionary til globale værdier her
    return None

#Denne funktion skal tilføje 1 til nummeret i jeres dict
@app.post("/add")
async def add_number(request):
     #TODO: Add to number here 
     return redirect(f"/")

#TODO: Opret en POST funktion der kan trække 1 fra nummeret i jeres dict

#TODO: Funktionen POST skal kaldes i en form fra jeres "index.html"

if __name__ == "__main__":
    app.run(host="localhost", port=8080)