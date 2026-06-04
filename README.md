# Hero-Image-Background-Removal-API
Hero-Image Background Removal API

Start the server:
Run the following command in your terminal. The first time you run this, it will download the U^2-Net AI model weights automatically (about ~170MB).
Bash

uvicorn main:app --reload

Test the endpoint:
FastAPI automatically generates a beautiful, interactive testing UI.

    Open your browser and navigate to: http://localhost:8000/docs

    Click on the POST /extract-hero/ endpoint.

    Click "Try it out".

    Upload an image containing a clear hero subject.

    Click "Execute".

The API will process the image and output a downloadable PNG with a perfectly transparent background.
