from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse, Response
from starlette.status import HTTP_200_OK

app = FastAPI()
true = True
false = False

points = {"code":2,"latestVer":7,"data":{"mapLibVer":7,"data":[{"mapId":1,"version":1,"name":"SXCT1","icon":"😅","desc":"山西工学院 路线1","isPublic":true,"points":[{"lon":112.448653,"lat":39.37391},{"lon":112.450337,"lat":39.373869},{"lon":112.450343,"lat":39.372981},{"lon":112.448449,"lat":39.373048},{"lon":112.446652,"lat":39.373438},{"lon":112.446969,"lat":39.375287},{"lon":112.44728,"lat":39.374192},{"lon":112.45119,"lat":39.374715}]},{"mapId":2,"version":1,"name":"SXCT2","icon":"🤔","desc":"山西工学院 路线2","isPublic":true,"points":[{"lon":112.446097,"lat":39.376205},{"lon":112.447931,"lat":39.376089},{"lon":112.447813,"lat":39.375202},{"lon":112.446912,"lat":39.375094},{"lon":112.44659,"lat":39.374928},{"lon":112.446719,"lat":39.373394},{"lon":112.448436,"lat":39.373103},{"lon":112.450238,"lat":39.372962},{"lon":112.450431,"lat":39.373982},{"lon":112.451182,"lat":39.374422},{"lon":112.448886,"lat":39.37448},{"lon":112.448296,"lat":39.374181}]},{"mapId":3,"version":1,"name":"CD","icon":"🤔","desc":"经纬度0","isPublic":true,"points":[{"lon":0,"lat":0},{"lon":0,"lat":1}]}]}}
default = {"code": 0}

@app.get("/")
async def root():
    return JSONResponse(content=default)

@app.get("/updateMapData.php")
async def get_data(curr_map_ver: int = Query(None)):
    if curr_map_ver == points["latestVer"]:
        return JSONResponse(content=default)
    else:
        return JSONResponse(content=points)
        
@app.get("/checkUpdate.php")
async def check_update(version: str = Query(None)):
    return Response(content='1')

@app.get("/auth.php")
async def auth(keycode: str = Query(None)):
    return Response(content='1' if keycode == '密码' else '-12')
