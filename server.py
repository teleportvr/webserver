from flask import Flask, request, render_template
import requests

app = Flask(__name__)

cameraheadsetdict = {}

frameslist = {}

@app.route("/")
def test():
	return render_template("index.html")

@app.route("/link", methods = ["POST"])
def link():
	print(request.form)
	cameraheadsetdict[int(request.form['camID'])] = int(request.form['headSetID'])
	frameslist[request.form['headSetID']] = []
	return "200"

@app.route("/uploadframes")
def upload():
	frameslist[1] = []
	print("ok")
	#print(type(requests.get('http://192.168.43.32:5000/video_feed')))
	for i in range(0,10):
		print("oh")
		frameslist[1].append(requests.get('http://192.168.43.32:5000/video_feed'))
	return "200"
	#yield requests.get('http://192.168.43.32:5000/video_feed')

@app.route("/yeet")
def yeet():
	print(len(frameslist[1]))
	return "200"

@app.route("/test")
def tester():
	print(cameraheadsetdict)
	return "200"