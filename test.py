from fastapi import FastAPI, Request

from client import config, tgbot

app = FastAPI(debug=True)

print("Go Injoi!")


@app.get("/")
async def test(request: Request):
    return {"hello": "world"}


@app.get("/omk")
async def fuck(request: Request):
    om = await tgbot.send_message(-1001237141420, "TEST")
    print(om)
    return {"msg": "MC"}


PORT = config("PORT")