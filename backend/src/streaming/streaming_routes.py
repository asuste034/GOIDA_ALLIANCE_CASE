from fastapi import FastAPI, File, UploadFile
import uvicorn
from pydantic import BaseModel
from fastapi_frame_stream import FrameStreamer

app = FastAPI()
fs = FrameStreamer()

class InputImg(BaseModel):
    img_base64str : str


@app.post("/send_frame_from_string/{stream_id}")
async def send_frame_from_string(stream_id: str, d:InputImg):
    await fs.send_frame(stream_id, d.img_base64str)


@app.post("/send_frame_from_file/{stream_id}")
async def send_frame_from_file(stream_id: str, file: UploadFile = File(...)):
    await fs.send_frame(stream_id, file)


@app.get("/video_feed/{stream_id}")
async def video_feed(stream_id: str):
    return fs.get_stream(stream_id)