from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()

points = {
    "code":2,
    "latestVer":20,
    "data":{
        "mapLibVer":20,
        "data":[
            {
                "mapId":1,
                "version":1,
                "name":"\u5c71\u897f\u5de5\u5b66\u9662",
                "icon":"\ud83d\ude05",
                "desc":"\u5c71\u897f\u5de5\u5b66\u9662",
                "isPublic":True,
                "points":[
                    {
                        "lon":112.448653,
                        "lat":39.37391
                    },
                    {
                        "lon":112.450337,
                        "lat":39.373869
                    },
                    {
                        "lon":112.450343,
                        "lat":39.372981
                    },
                    {
                        "lon":112.448449,
                        "lat":39.373048
                    },
                    {
                        "lon":112.446652,
                        "lat":39.373438
                    },
                    {
                        "lon":112.446969,
                        "lat":39.375287
                    },
                    {
                        "lon":112.44728,
                        "lat":39.374192
                    },
                    {
                        "lon":112.45119,
                        "lat":39.374715
                    }
                ]
            }
        ]
    }
}

@app.get("/")
async def get_data(curr_map_ver: int = Query(None)):
    if curr_map_ver == 19:
        return JSONResponse(content={"code": 0})
    else:
        return JSONResponse(content=points)
