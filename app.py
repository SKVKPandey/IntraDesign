from flask import Flask, request, render_template
import openai
import requests
from PIL import Image
import io

# Set up OpenAI API key
openai.api_key = "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"

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":

        room_type = request.form["name"]
        description = request.form["message"]

        # Define the prompt
        prompt = f"hyper realistic interior design of a {room_type} that is {description}"

        # Generate image
        response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
        )

        # Get the image URL from the response
        image_url = response['data'][0]['url']

        # Download the image and display it
        image_data = requests.get(image_url).content
        image = Image.open(io.BytesIO(image_data))
        # image.save()
        image.show()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)