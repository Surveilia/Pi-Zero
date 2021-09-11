#!bin/bash

#This script is the final script for interfacing MPU6050 to the PI Zero W.
#This script installs required repos to run the python code attached
#in this package.

#

echo "Installing Python Files for MPU6050"

sudo apt-get install build-essential python-dev python-pip

sudo pip install RPi.GPIO

sudo apt-get install python-smbus

sudo apt-get install i2c-tools


#This runs a test to ensure I2C tools is properly installed. If error occurs
#view https://www.raspberrypistarterkits.com/guide/raspberry-pi-accelerometer-gyroscope/
echo "Testing i2c tools"

sudo i2cdetect -y 1

sudo pip install mpu6050-raspberrypi

echo "Creating MPU6050 directory"

mkdir home/pi/Documents/MPU6050

echo "Moving AccGyroTest.py to MPU6050 directory"

mv AccGyroTest.py home/pi/Documents/MPU6050