# My Games (games.anikethchavare.com) - server.py

'''
Copyright 2025 Aniketh Chavare <aniketh@anikethchavare.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

# Imports
import os
import secrets

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

# Initializing the "App" Server
app = FastAPI(docs_url=None, redoc_url=None)

# Configuring Middleware
app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"], allow_headers=["*"])

# Mounting Assets
app.mount("/css", StaticFiles(directory="templates/css"), name="/css")
app.mount("/fonts", StaticFiles(directory="templates/fonts"), name="/fonts")
app.mount("/images", StaticFiles(directory="templates/images"), name="/images")
app.mount("/js", StaticFiles(directory="templates/js"), name="/js")

# Favicon (App)
@app.get("/favicon.ico")
async def app_favicon(request: Request):
    # Returning the File
    return FileResponse(os.getcwd().replace(os.sep, "/") + "/media/favicon.png", status_code=200)

# Robots (App)
@app.get("/robots.txt")
async def app_robots(request: Request):
    # Returning the File
    return FileResponse(os.getcwd().replace(os.sep, "/") + "/robots.txt", status_code=200)

# Sitemap (App)
@app.get("/sitemap.xml")
async def app_sitemap(request: Request):
    # Returning the File
    return FileResponse(os.getcwd().replace(os.sep, "/") + "/sitemap.xml", status_code=200)

# Index (App)
@app.get("/")
async def app_index(request: Request):
    # Fetching the HTML Template
    response = Jinja2Templates(directory="templates").TemplateResponse("index.html", {"request": request})

    # Modifying the HTTP Headers
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"

    # Returning the HTML Template
    return response

# About (App)
@app.get("/about")
async def app_index(request: Request):
    # Fetching the HTML Template
    response = Jinja2Templates(directory="templates").TemplateResponse("about.html", {"request": request})

    # Modifying the HTTP Headers
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"

    # Returning the HTML Template
    return response

# Tennis (App)
@app.get("/tennis")
async def app_tennis(request: Request):
    # Fetching the HTML Template
    response = Jinja2Templates(directory="templates").TemplateResponse("tennis.html", {"request": request, "css_nonce": secrets.token_urlsafe(32), "js_nonce": secrets.token_urlsafe(32)})

    # Modifying the HTTP Headers
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"

    # Returning the HTML Template
    return response

# Rock Paper Scissors (App)
@app.get("/rps")
async def app_rockpaperscissors(request: Request):
    # Fetching the HTML Template
    response = Jinja2Templates(directory="templates").TemplateResponse("rock-paper-scissors.html", {"request": request, "css_nonce": secrets.token_urlsafe(32), "js_nonce": secrets.token_urlsafe(32)})

    # Modifying the HTTP Headers
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"

    # Returning the HTML Template
    return response

# Error 404 (App)
@app.exception_handler(404)
async def app_error404(request: Request, exec: HTTPException):
    # Fetching the HTML Template
    response = Jinja2Templates(directory="templates").TemplateResponse("error-404.html", {"request": request, "css_nonce": secrets.token_urlsafe(32)})

    # Modifying the HTTP Headers
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"

    # Returning the HTML Template
    return response