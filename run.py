from flask import Flask, render_template, send_file, send_from_directory,jsonify

app = Flask(__name__)
@app.route("/")
def index():
    return "hi~" \
           "主页还没做好,不过我猜你想要这些?" \
           ""

# https://blog.csdn.net/xw_2_xh/article/details/96175571
@app.route('/download/mr-fastbuilder', methods=["GET"])
def get_fastbuilder(file_name):
    dir =  "./resource/mr-fastbuilder"


if __name__ == "__main__":
    # flask run --host=0.0.0.0
    # or use `python -m flask`
    app.run(debug=False, port=80)