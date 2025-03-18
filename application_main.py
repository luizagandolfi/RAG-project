from app.api.server_application import ServerApplication
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.models.config import config

from pathlib import Path
import uvicorn



app = ServerApplication.get_instance()
templates = Jinja2Templates(directory=Path("./app/templates"))
app.mount("/static", StaticFiles(directory=Path("./app/static")), name="static")

# para debugar, so descomentar
# if __name__ == "__main__":
    # uvicorn.run(app, host='localhost', port=8000)
    