from flask import Flask, render_template, send_file, send_from_directory,jsonify, make_response, request

from db.database import init_db, session
import db.models as mods
from db.models import UserPlugin, UserInfo, PluginMD5, PluginInfo, FrameInfo


app = Flask(__name__)
init_db()


@app.route("/")
def index():
    response = make_response(
        render_template("index.html")
    )
    return response

# https://blog.csdn.net/xw_2_xh/article/details/96175571
@app.route('/download/fastbuilder/mr-fastbuilder', methods=["GET"])
def get_fastbuilder():
    fbdir = "./download/fastbuilder/"
    try:
        response = make_response(
            send_from_directory(fbdir, "mr-fastbuilder", as_attachment=True)
        )
        return response
    except Exception as e:
        return jsonify({"code": 500, "message": f"啊咧? 好像出错了呢qaq\nError: {e}\n尝试联系管理员吧: qq1758489207 qq614286773"})

@app.route('/download/plugins/<file_name>', methods=["GET"])
def get_plugin(file_name):
    file_name += ".so"
    plugindir = "./download/plugins"
    try:
        response = make_response(
            send_from_directory(plugindir, file_name, as_attachment=True)
        )
        return response
    except Exception as e:
        return jsonify({"code": 500, "message": f"啊咧? 好像出错了呢qaq\nError: {e}\n尝试联系管理员吧: qq1758489207 qq614286773"})

@app.route("/help/fastbuilder", methods=["GET"])
def get_fastbuilder_doc():
    doc_path = "mrfb.html"
    # try:
    response = make_response(
        render_template(doc_path)
    )
    return response
    # except Exception as e:
    #     return jsonify({"code": 500, "message": f"啊咧? 好像出错了呢qaq\nError: {e}\n尝试联系管理员吧: qq1758489207 qq614286773"})


#  记得filename要加文件后缀!
@app.route("/help/plugins/<filename>", methods=["GET"])
def get_plugin_doc(filename):
    filename += "-readme.html"
    print(filename)
    try:
        response = make_response(
            render_template(filename)
        )
        return response
    except Exception as e:
        return jsonify({"code": 500, "message": f"啊咧? 好像出错了呢qaq\nError: {e}\n尝试联系管理员吧: qq1758489207 qq614286773"})


#
@app.route("/auth/plugin", method=["POST"])
def auth_plugin():
    server, account, plugins = request.form["server"], \
                               request.form["account"], \
                               list(request.form["plugins"])
    
    res = session.query(UserPlugin).filter(UserPlugin.account == account)
    print(res)
    return ""


@app.route("/auth/account", method=["POST, GET"])
def auth_account():
    account = request.form["account"]
    res = session.query(UserInfo).filter(account)
    print(res)

    return jsonify({"res": bool(res)})

if __name__ == "__main__":
    app.run(debug=False, port=80, host="0.0.0.0")
