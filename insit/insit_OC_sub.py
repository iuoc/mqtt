#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =========================================================================== #
# IUOC - REDS & INSIT Institute, HEIG-VD, Yverdon-les-Bains (CH) - 2022       #
# =========================================================================== #
""" server test - Test of communication with INSIT RASPI camera OC

"""
# =========================================================================== #
__author__ = "Jean-Pierre Miceli <jean-pierre.miceli@heig-vd.ch"
__author__ = "JASON BULA <jason.bula@heig-vd.ch"
# =========================================================================== #

import paho.mqtt.client as mqtt
import time


broker_addr='10.192.91.138'
TOPIC="iuoc/insit/camera/photo"

client = mqtt.Client("INISIT camera test server")
client.connect(broker_addr)

def on_message(client, userdata, message):
    print("message received: " , str(message.payload.decode("utf-8")))

client.on_message = on_message

client.connect(broker_addr)
client.subscribe(TOPIC)

client.loop_start()
time.sleep(1000)
client.loop_stop()
