from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import Response
from rembg import remove, new_session
from PIL import Image
import io

app = FastAPI(title="Hero Image Extractor API")

# Initialize the model session globally so it loads once on startup
# u2net is the standard model, excellent for general hero images.
session = new_session("u2net")

@app.post("/extract-hero/")
async def extract_hero(file: UploadFile = File(...)):
    # Validate the file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File provided is not an image.")
    
    try:
        # Read the image file into memory
        contents = await file.read()
        input_image = Image.open(io.BytesIO(contents))
        
        # Apply the background removal
        # post_process=True helps clean up the edges of the mask
        output_image = remove(input_image, session=session, post_process=True)
        
        # Save the result to a byte array as a PNG (to preserve transparency)
        img_byte_arr = io.BytesIO()
        output_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        # Return the image directly to the client
        return Response(content=img_byte_arr.getvalue(), media_type="image/png")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

