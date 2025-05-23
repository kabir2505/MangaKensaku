from fastapi import FastAPI,Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from fastapi import Request
from infer import faiss_search_engine
import uvicorn
import os

app=FastAPI() # Fastapi instance


current_dir = os.path.dirname(os.path.abspath(__file__))  # app/
templates_path = os.path.join(current_dir, "templates")
templates=Jinja2Templates(directory=templates_path)
general_pages_router=APIRouter()

# app.mount("/static")

@app.get("/") #path operation decorator
def root(request: Request): #function
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/search",response_class=HTMLResponse)
def search_index(request: Request,query:str=Form(...)):
    urls=faiss_search_engine.retrieve_similar_images(query)
    return templates.TemplateResponse("search_result.html",{"request":request,"query":query,"urls":urls})
 
        
    
    
if __name__=="__main__":
    
    uvicorn.run(app,host="0.0.0.0",port=8000)