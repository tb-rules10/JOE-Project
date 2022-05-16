from flask import Flask, render_template, request, redirect, url_for, make_response
import time
import RPi.GPIO as GPIO
import camera from VideoCamera
mA1=18
mA2=23
mB1=24
mB2=25
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(mA1, GPIO.OUT)
GPIO.setup(mA2, GPIO.OUT)
GPIO.setup(mB1, GPIO.OUT)
GPIO.setup(mB2, GPIO.OUT)
GPIO.output(mA1 , 0)
GPIO.output(mA2 , 0)
GPIO.output(mB1, 0)
GPIO.output(mB2, 0)
app = Flask(_name_) #set up flask server
#when the root IP is selected, return index.html page
@app.route('/')
def index():
    return render_template('index.html')
def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    changePin = int(changepin) #cast changepin to an int
    if changePin == 2:
                print ("Left")
                GPIO.output(mA1 , 1)
                GPIO.output(mA2 , 0)
                GPIO.output(mB1 , 0)
                GPIO.output(mB2 , 0)
    elif changePin == 1:
                print ("Forward")
                GPIO.output(mA1 , 1)
                GPIO.output(mA2 , 0)
                GPIO.output(mB1 , 1)
                GPIO.output(mB2 , 0)
    elif changePin == 4:
                print ("Right")
                GPIO.output(mA1 , 0)
                GPIO.output(mA2 , 0)
                GPIO.output(mB1 , 1)
                GPIO.output(mB2 , 0)
    elif changePin == 5:
                print ("Reverse")
                GPIO.output(mA1 , 0)
                GPIO.output(mA2 , 1)
                GPIO.output(mB1 , 0)
                GPIO.output(mB2 , 1)
    elif changePin == 3:
                print("Stop")
                GPIO.output(mA1 , 0)
                GPIO.output(mA2 , 0)
                GPIO.output(mB1 , 0)
                GPIO.output(mB2 , 0)
    response = make_response(redirect(url_for('index')))
    return(response)
app.run(debug=True, host='0.0.0.0', port=8000) #set up the server in debug mode to the port 8000
