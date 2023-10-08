from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse, Response
from starlette.status import HTTP_200_OK

app = FastAPI()
true = True
false = False

points = {"code":2,"latestVer":6,"data":{"mapLibVer":6,"data":[{"mapId":1,"version":1,"name":"SXCT","icon":"😅","desc":"山西工学院 路线1","isPublic":true,"points":[{"lon":112.448653,"lat":39.37391},{"lon":112.450337,"lat":39.373869},{"lon":112.450343,"lat":39.372981},{"lon":112.448449,"lat":39.373048},{"lon":112.446652,"lat":39.373438},{"lon":112.446969,"lat":39.375287},{"lon":112.44728,"lat":39.374192},{"lon":112.45119,"lat":39.374715}]},{"mapId":2,"version":1,"name":"SXCT","icon":"🤔","desc":"山西工学院 路线2","isPublic":true,"points":[{"lon":112.446097,"lat":39.376205},{"lon":112.447931,"lat":39.376089},{"lon":112.447813,"lat":39.375202},{"lon":112.446912,"lat":39.375094},{"lon":112.44659,"lat":39.374928},{"lon":112.446719,"lat":39.373394},{"lon":112.448436,"lat":39.373103},{"lon":112.450238,"lat":39.372962},{"lon":112.450431,"lat":39.373982},{"lon":112.451182,"lat":39.374422},{"lon":112.448886,"lat":39.37448},{"lon":112.448296,"lat":39.374181}]}]}}

@app.get("/")
async def get_data(curr_map_ver: int = Query(None)):
    if curr_map_ver == points["latestVer"]:
        return JSONResponse(content={"code": 0})
    else:
        return JSONResponse(content=points)
        
@app.get("/checkUpdate")
async def check_update(version: str = Query(None)):
    return Response(status_code=HTTP_200_OK)

@app.get("/auth")
async def auth():
    return Response(content='1')
