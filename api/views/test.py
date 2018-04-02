import paho.mqtt.publish as publish

host = "mqtt.koor.io"
topic = "5aa1171bda0970019aad7c6a.koor.io/devices/5abfbaec95392e04569ece8c"

msgs = [{'topic': topic, 'payload': "05"}, {'topic': topic, 'payload': "014"}]

publish.multiple(msgs, hostname=host)
