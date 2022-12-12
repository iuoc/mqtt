#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =========================================================================== #
# IUOC - REDS Institute, HEIG-VD, Yverdon-les-Bains (CH) - 2022               #
# =========================================================================== #
""" subscribe - this script subscribes to 'iuoc/debug' topic

"""
# =========================================================================== #
__author__ = "Jean-Pierre Miceli <jean-pierre.miceli@heig-vd.ch"
# =========================================================================== #

import paho.mqtt.client as mqtt
import time

client = mqtt.Client("Subscriber")

broker_addr='127.0.0.1'

def on_message(client, userdata, message):
    print("message received: " , str(message.payload.decode("utf-8")))

client.on_message = on_message

client.connect(broker_addr)
client.subscribe("iuoc/debug")

client.loop_start()
time.sleep(10)
client.loop_stop()
