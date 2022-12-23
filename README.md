This repository contains different examples / experiments around MQTT protocol.

These examples are made on python using [Paho](https://www.eclipse.org/paho/index.php?page=clients/python/index.php)
MQTT Client. As broker, [mosquitto](https://mosquitto.org/) has been used.

They can be run on a local PC and/or Raspberry PI.

The current project are:

* **hello_world**: *hello_world* mqtt example
* **basic_iuoc**: Basic example of an IUOC
* **json_schema**: IUOC mqtt payload JSON schema

# Installation

*Mosquitto* broker and *Paho* client have to be installed to use these examples.

## Mosquitto broker

```shell
	$ sudo apt install mosquitto
	$ (optional) sudo apt install mosquitto-clients
```

The `mosquitto-clients` install some cli tools. See blow example on how to subscribe
or publish to a topic.

* Subscribe: `$ mosquitto_sub -d -t testTopic`
* Publish: ` $mosquitto_pub -d -t testTopic -m "Hello world!"`

