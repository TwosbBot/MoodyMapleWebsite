from flask import Flask, render_template, send_file, send_from_directory,jsonify, make_response

app = Flask(__name__)
@app.route("/")
def index():
    return "hi~" \
           "主页还没做好,不过我猜你想要这些?" \
           ""

# https://blog.csdn.net/xw_2_xh/article/details/96175571
@app.route('/download/mr-fastbuilder/', methods=["GET"])
def get_fastbuilder():
    fbdir = "./resource/download/fastbuilder/"
    try:
        response = make_response(
            send_from_directory(fbdir, "mr-fastbuilder", as_attachment=True)
        )
        return response
    except Exception as e:
        return jsonify({"code": 500, "message": f"啊咧? 好像出错了呢qaq\nError: {e}\n尝试联系管理员吧: qq1758489207 qq614286773"})

@app.route('/download/plugin/<file_name>', methods=["GET"])
def get_plugin(file_name):
    file_name += ".so"
    plugindir = "./resource/download/plugins"
    try:
        response = make_response(
            send_from_directory(plugindir, file_name, as_attachment=True)
        )
        return response
    except Exception as e:
        return jsonify({"code": 500, "message": f"啊咧? 好像出错了呢qaq\nError: {e}\n尝试联系管理员吧: qq1758489207 qq614286773"})

@app.route("/help/fastbuilder")
def get_fastbuilder_doc():
    doc_path = "./resource/templates/mrfb.html"
    try:
        response = make_response(
            render_template(doc_path)
        )
        return response
    except Exception as e:
        return jsonify({"code": 500, "message": f"啊咧? 好像出错了呢qaq\nError: {e}\n尝试联系管理员吧: qq1758489207 qq614286773"})


#  记得filename要加文件后缀!
@app.route("/help/plugins/<filename>")
def get_fastbuilder_doc(filename):
    doc_path = "./resource/templates/plugins/"
    try:
        response = make_response(
            render_template(doc_path+filename)
        )
        return response
    except Exception as e:
        return jsonify({"code": 500, "message": f"啊咧? 好像出错了呢qaq\nError: {e}\n尝试联系管理员吧: qq1758489207 qq614286773"})


if __name__ == "__main__":
    # flask run --host=0.0.0.0
    # or using `python -m flask`
    app.run(debug=False, port=80, host="0,0,0,0")