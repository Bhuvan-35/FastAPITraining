from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"page":"Home"}

@app.get("/about")
def about():
    return {"page":"About","author":"Bhuvan"}

@app.get("/health")
def health():
    return {"status":"ok"}

#POST request
@app.post("/create")
def creat_something():
    return {"message":"Created"}

@app.get("/student/(usn)")
def get_result(usn):
    return {"Result":"Distinction","usn":5678}

#path parameters with Type Hint
@app.get("/candidate/(rollno)")
def get_candidate(rollno:int):
    return {"Result":"Distinction","rollno":rollno,"type":str(type(rollno))}

