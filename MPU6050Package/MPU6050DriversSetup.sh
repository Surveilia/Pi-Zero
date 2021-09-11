#!/bin/bash

#This is a script from https://www.raspberrypistarterkits.com/guide/raspberry-pi-accelerometer-gyroscope/
#Script is run immediately after working through the configuration UI
#in part one of the tutorial (Step-2)

#Script fills in the /etc/modules file with I2C commands. MPU6050 uses I2C
#communication, which requires activation on the PI. Wiring diagram can be
#found in the package provided in this file set.

echo "Filling in /etc/modules"

cat >> /etc/modules << EOF

i2c-bcm2708

i2c-dev

EOF

reboot
