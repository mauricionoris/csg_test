import uvicorn

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

import backend_mod 

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):

    github_users = backend_mod.get_github_users()

    if len(request.query_params) > 0:
        idx = int(dict(request.query_params)['idx'])

        if idx > -1:
            github_users['users'][idx]['status'] = 'U'
        else: 
            github_users['users'][len(github_users['users'])-1]['status'] = 'N'


    context = {
        "request": request,
        "github_users": github_users['users'],
    }
   
    return templates.TemplateResponse("home.html", context)

@app.get("/create")
async def add_github_user(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("create.html", context)


@app.post("/create")
async def add_github_user(
    github_username: str = Form()):
    
    usr_idx = backend_mod.upsert_github_users(github_username)
    params = "?idx={idx}".format(idx=usr_idx)


    return RedirectResponse(
        url=app.url_path_for("home") + params,
        status_code=302,
        )


if __name__ == "__main__":
    
    uvicorn.run(
        "app:app",
        host    = "0.0.0.0",
        port    = 8036, 
        reload  = True
    )