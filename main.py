from sanic import Sanic
from sanic.response import redirect 
from sanic_jinja2 import SanicJinja2



app = Sanic("Hej")
app.static("/static", "./static")
jinja = SanicJinja2(app)


#opret en dict der hedder global_vars
#jeres dict skal indeholde en key "number" og en værdi 0
globals_vars = { "number": 0     
        
        }

#Dette endpoint giver en respons ved en http GET request der peger på "localhost:8080/"
#Responsen svarer til indholdet af index.html og pga. at index.html er et jinja template, 
#vil jeres dicts variable kunne bruges i html-filen. 
@app.get("/")
@jinja.template("index.html")
async def index(request):
    
    return globals_vars

#Denne funktion skal tilføje 1 til nummeret i jeres dict
@app.post("/add")
async def add_number(request):
     globals_vars["number"] +=1
     return redirect(f"/")

#Denne funktion skal trække 1 fra nummeret i jeres dict
@app.post("/subtract")
async def sub_number(request):
    globals_vars["number"] -=1
    return redirect(f"/")

if __name__ == "__main__":
    app.run(host="localhost", port=8080)