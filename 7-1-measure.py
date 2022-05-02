import RPi.GPIO as GPIO
import time

import numpy as np
import matplotlib.pyplot as plt

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21,20,16,12,7,8,25,24]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule=17
comparator = 4

def decimal2binary(decimal):
    return[int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    return signal

def adc():
    left = 0
    right = 256
    while right-left > 0:
        mid = (right + left) // 2
        num2dac(middle)
        time.sleep(0.007)
        if GPIO.input(comp) == 1:
            left = mid
        else:
            right = mid
    i = int(left / levels * len(leds))
    GPIO.output(leds[i % len(leds):], 1)
    return left / levels * maxVoltage

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troykaModule, GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(comparator, GPIO.IN)

try:
    measurements = []
    start = time.time()
    GPIO.out(troykaModule, 1)
    voltage = adc()
    while voltage < 0.97 * 3.3:
        measurements.append(voltage)
        voltage = adc()
    GPIO.output(troyka, 0)
    voltage = adc()
    while voltage >= 0.02 * 3.3:
        measurements.append(voltage)
        voltage = adc()
    finish = time.time()
    total_time = finish - start
    plt.plot(measurements)
    file = open("data.txt", "w")
    file.write("\n".join(map(str, measurements)))
    samp = (total_time / len(measurements))
    quant = (max(measurements) - min (measurements)) / len(measurements)
    file1 = open("settings.txt", "w")
    file1.write(samp, quant)
    print("time of experiment: {:.2f}, period of measurement: {:.2f}, sampling frequancy: {:.2f}, quantization step = {:.2f}".format(total_time, 1/samp, samp, quant))

    plt.show()

finally:
    GPIO.output(leds,GPIO.LOW)
    GPIO.cleanup(leds)
    GPIO.output(troykaModule,GPIO.LOW)
    GPIO.cleanup(troykaModule)
    print("GPIO cleanup completed")
