# -*- coding: utf-8 -*-
from flask import Flask, Response, redirect
import requests
import re

app = Flask(__name__)
app.debug = False
CHUNK_SIZE = 2048

@app.route('/<path:url>')
def proxy(url):
    r = requests.get("http://"+url, stream=True)
    def generate():
        for chunk in r.iter_content(CHUNK_SIZE):
            yield chunk
    return Response(generate(), headers = r.raw.headers.items())

@app.errorhandler(404)
def page_not_found(e):
	return redirect("https://libnull.com/")

@app.errorhandler(500)
def internal_server_rror(e):
	r = requests.get("http://ww3.sinaimg.cn/large/images/default_large.gif", stream=True)
	def generate():
		for chunk in r.iter_content(CHUNK_SIZE):
			yield chunk
	return Response(generate(), headers = r.raw.headers.items())

if __name__ == '__main__':
    app.run()
