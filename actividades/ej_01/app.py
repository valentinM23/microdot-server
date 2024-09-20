# Aplicacion del servidor
from microdot import Microdot, send_file
from machine import Pin

app = Microdot()

@app.get('/')
async def index(request):
    return send_file('/index.html')


app.run(port = 80)