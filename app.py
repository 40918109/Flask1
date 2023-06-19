import configs as CONFIGS
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(CONFIGS)


@app.route("/index")
def index():
    return render_template('index.html')  # 回傳template資料夾中的index.html


if __name__ == "__main__":
    app.run()