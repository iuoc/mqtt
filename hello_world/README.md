Simple MQTT *Hello world* example

This example is split in two:
 * `subscribe.py`: It subscribes to `iuoc/debug` topic and print the payload of
   the received messages. It waits for new messages for 10 seconds.
 * `publish.py`: It publishes, to `iuoc/debug` topic, for 'hello world' messages
