import os
import sys
import subprocess
import shutil
from fastapi import FastAPI
from fastapi.logger import logger
from pyngrok import ngrok
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


# Get the dev server port (defaults to 8000 for Uvicorn, can be overridden with `--port`
# when starting the server
port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else "8000"

# Open a ngrok tunnel to the dev server
public_url = ngrok.connect(port).public_url
logger.info("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))
print(public_url)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/print_image/")
async def print(file: UploadFile = File(...)):
    try:
        # Save the uploaded file to a temporary location
        file_path = f"/tmp/{file.filename}"
        with open(file_path, "wb") as temp_file:
            shutil.copyfileobj(file.file, temp_file)

        # Send the file to the default printer
        print_command = f"lp {file_path}"
        subprocess.run(print_command, shell=True)

        return JSONResponse(content={"message": "File sent to the printer"}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Cleanup: Remove the temporary file
        os.remove(file_path)