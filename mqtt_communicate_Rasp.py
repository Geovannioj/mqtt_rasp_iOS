#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import os
import time


def gpioSetup():

        gpio.setmode(gpio.BCM)

        #set pin 40 as output pin

        gpio.setup(21, gpio.OUT)
        gpio.setup(20, gpio.OUT)

def connectionStatus(client, userdata, flags, rc):
        client.username_pw_set(username="ioqvlgfd",password="xL0pD1ldNz9u")
        mqttClient.subscribe("sensors")
        print("Entrou no connect")
         
def messageDecoder(client, userdat, msg):
        messge = msg.payload.decode(encoding='UTF-8')
        print(messge)    
        
        if messge == "on": 
                gpio.output(21, gpio.HIGH)
                print("Sensors ACTIVATE")
                while(!gpio.output(21)):
                        time.sleep(1)
        #call script to start the sensors
                os.system("./init_laser") 
                os.system("./init_GPS")
        elif messge == "off": 
                gpio.output(21, gpio.LOW)
                print("Sensors DEACTIVATE!")
                os.system("./../../sensors.sh")

        elif messge == "calib":
                print("Entrou para calibrar 1/2")
                gpio.output(20, gpio.HIGH)
                time.sleep(10)
                print("Sensors CALIBRATE! 2/2")
                gpio.output(20, gpio.LOW)
        else:
                print("Unkown message!") 

#set up the RPI GPIO pins
gpioSetup()

clientName = "RPI3B"
serverAddress ="postman.cloudmqtt.com" #"172.16.1.220"# "169.254.201.69"
mqttClient = mqtt.Client(clientName)
mqttClient.on_connect = connectionStatus
mqttClient.on_message = messageDecoder

mqttClient.connect(serverAddress,13504)
mqttClient.loop_forever()
                              