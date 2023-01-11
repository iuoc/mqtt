from flask import Flask
from flask import send_file
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import paho.mqtt.client as mqtt
from threading import Thread

# initialize the camera and grab a reference to the raw camera capture
# allow the camera to warmup
time.sleep(0.1)

# grab an image from the camera


app = Flask(__name__)

broker_addr='10.192.91.138'
#port = 1883

client = mqtt.Client("Publisher")
client.connect(broker_addr)


def mqttThread():
    while True:
        client.publish("iuoc/insit/camera/photo","http://10.192.91.139:5000/image")
        time.sleep(3)        
        
mt = Thread(target=mqttThread)
mt.start()


path = "/home/iot/Desktop/iot.jpg"
@app.route('/image', methods=['GET'])
def downloadFile ():
    camera = PiCamera()
    camera.resolution = (1920,1080)
    camera.start_preview()
    camera.capture('/home/iot/Desktop/iot.jpg')
    camera.stop_preview()
    
    
    return send_file(path, as_attachment=True)



if __name__ == '__main__':
    app.run(host='10.192.91.139', port=5000,debug=True) 


