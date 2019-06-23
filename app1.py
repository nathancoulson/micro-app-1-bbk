from flask import Flask, url_for, request, render_template, abort, redirect
import requests
import os

app = Flask(__name__)

app_urls = {
	1: "app_1",
    2: "app_2",
    3: "app_3",
    4: "app_4"
}

@app.route('/')
def hello_world():
    return 'Hello world! from app_1, host: ' +  str(os.uname()[1])

@app.route('/<int:num>', methods=['GET', 'POST'])
def ret_num(num):
    return 'Number: {0}, Apps: {1}'.format(*(num, 1))

@app.route('/<int:init_app>/<app_path>/<int:num>', methods=['GET', 'POST'])
def post_to_micro(init_app, app_path, num):
    route = "http://" + app_urls[init_app] + ":5000" +"/" + app_path + "/" + str(num)
    resp = requests.get(route)
    return resp.text + "\n->1via1"


if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0', port=5000)
