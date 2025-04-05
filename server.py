# My Games (games.anikethchavare.com) - server.py

'''
Copyright 2025 Aniketh Chavare <anikethchavare.work@protonmail.com>

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
import secrets

from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

# Initializing the "App" Server
app = FastAPI(docs_url=None, redoc_url=None)

# Configuring Middleware
app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"], allow_headers=["*"])

# Tennis (App)
@app.get("/tennis")
async def app_tennis(request: Request, response: Response):
    # Returning the HTML Template
    return Jinja2Templates(directory="one-page").TemplateResponse("tennis.html", {"request": request, "css_nonce": secrets.token_urlsafe(32), "js_nonce": secrets.token_urlsafe(32)})