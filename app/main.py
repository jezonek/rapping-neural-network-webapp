from fastapi import FastAPI

from serve_done_text import serve_done_text as done_text
from starlette.responses import Response

app = FastAPI()


@app.get("/")
def read_root():
    text = done_text()
    if text:
        data = """
    <html>    
    <body>
        {}
    </body>
    </html>
    """.format("<br>\n".join(text))
        return Response(content=data, media_type="text/html")
    else:
        return 'Generating text... Refresh after some time'
