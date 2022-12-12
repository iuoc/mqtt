#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =========================================================================== #
# IUOC - REDS Institute, HEIG-VD, Yverdon-les-Bains (CH) - 2022               #
# =========================================================================== #
""" publish - This script publishes "hello world" message to 'iuoc/debug' topic

"""
# =========================================================================== #
__author__ = "Jean-Pierre Miceli <jean-pierre.miceli@heig-vd.ch"
# =========================================================================== #

import paho.mqtt.client as mqtt
import time

broker_addr='127.0.0.1'

client = mqtt.Client("Publisher")
client.connect(broker_addr)

for _ in range(4):
	client.publish("iuoc/debug","Hello world")
	time.sleep(1)
