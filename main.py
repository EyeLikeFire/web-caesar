from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="/" method="post">
      <label for="rot"><b>Rotate by:</b> 
        <input type="text" id="rot" name="rot" value = "0"/>
        <textarea name="text">{0}
        </textarea>
        </label>
        <input type="submit" value="Submit Query"/>
      </form>
    </body>
</html>

"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']

    try:
        rot = int(rot)
    except ValueError:
     #Handle the exception.
        rot = 0


    string = request.form['text']
    encrypted = rotate_string(string, rot)
    rot = str(rot)
    return form.format(encrypted)

@app.route("/")
def index():
    return form.format("Enter your message here...")

app.run()