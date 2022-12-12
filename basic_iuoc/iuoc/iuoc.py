#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =========================================================================== #
# IUOC - REDS Institute, HEIG-VD, Yverdon-les-Bains (CH) - 2022               #
# =========================================================================== #
""" iuoc - contains classes to create an OC in IUOC framework

	These classes can be used as examples or to do experiments....

"""
# =========================================================================== #
__author__ = "Jean-Pierre Miceli <jean-pierre.miceli@heig-vd.ch"
# =========================================================================== #

import paho.mqtt.client as mqtt
import json

class Data(object):

	def __init__(self, name, value):
		self.name  = name
		self.value = value


class Message(object):
	""" encode / decode IUOC JSON messages """

	def __init__(self):
		pass

	def encode_data(self, data):

		data_dict = dict()

		data_dict['name']  = data.name
		data_dict['type']  = str(type(data.value))
		data_dict['value'] = data.value

		return data_dict

	def encode(self, name, cluster, location, description, data):
		message = dict()

		message['name'] = name
		message['cluster'] = cluster
		message['location'] = location
		message['description'] = description

		encoded_data = list()

		if isinstance(data, list):
			for d in data:
				single_data = self.encode_data(d)
				encoded_data.append(single_data)

		else:
			single_data = self.encode_data(data)
			encoded_data.append(single_data)

		message['data'] = encoded_data

		return json.dumps(message)

	def decode(self):
		pass

class OC(object):

	def __init__(self, name, cluster, location='', description=''):
		self.name = name
		self.cluster = cluster
		self.location = location
		self.description = description

		self.client = mqtt.Client(self.name)
		self.topic = 'iuoc/%(cluster)s/%(name)s' % { 'cluster': cluster, 'name': name }

		self.message = Message()

		print("[DEBUG] Create '%s' OC. It exports topic '%s'" % (name, self.topic))

	def name(self):
		return self.name

	def cluster(self):
		return self.cluster

	def setLocation(self, location):
		self.location = location

	def location(self):
		return self.location

	def setDescription(self, description):
		self.description = description

	def description():
		return self.description

	def connect(self, broker_addr):
		print("[DEBUG] connect to broker %s" %  broker_addr)
		self.client.connect(broker_addr)

	# def unconnect(self): TODO

	def publish(self, data):
		message = self.message.encode(self.name, self.cluster, self.location, self.description, data)
		self.client.publish(self.topic, message)
		#print("[DEBUG] publish")
		#print('   ', message)

	def subscribe(self, topic, callback):
		print("[DEBUG] subscribe")
		self.client.on_message = callback
		self.client.subscribe(topic)
		self.client.loop_start()
