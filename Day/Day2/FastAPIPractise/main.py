from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def read_root():
    return {"message":"Hello Dinumourya","number":18,"is_fun":True}
