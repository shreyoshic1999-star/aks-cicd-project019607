from flask import Flask



app = Flask(__name__)


@app.route('/')

def home():

    return """

    <!DOCTYPE html>

    <html>

    <head>

        <title>Azure Project</title>

        <style>

            body {

                background-color: #f4f8fb;

                font-family: Arial, sans-serif;

                text-align: center;

                padding-top: 100px;

            }

            h1 {

                color: #0078D4;

                font-size: 48px;

            }

            p {

                font-size: 20px;

                color: #444;

            }

        </style>

    </head>

    <body>

        <h1>Hello from Azure Project! ☁️</h1>

        <p>CI/CD Pipeline for Microservices on AKS is working successfully.</p>

    </body>

    </html>

    """


@app.route('/health')

def health():

    return "Application is Healthy", 200


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
