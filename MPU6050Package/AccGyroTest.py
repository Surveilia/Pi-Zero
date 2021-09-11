import smbus
from time import sleep

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

def MPU_Init():
        bus.write_byte_data(DeviceAddress, SMPLRT_DIV, 7)
        bus.write_byte_data(DeviceAddress, PWR_MGMT_1, 1)
        bus.write_byte_data(DeviceAddress, CONFIG, 0)
        bus.write_byte_data(DeviceAddress, INT_ENABLE, 1)

def read_raw_data(addr):
        #Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(DeviceAddress, addr)
        low = bus.read_byte_data(DeviceAddress, addr+1)

        #Concatenate higher and lower value
        value = ((high<<8) | low)

        #get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value

bus = smbus.SMBus(1)
DeviceAddress = 0x68

MPU_Init()

print("Reading MPU6050 Data")

while True:

        #Read accelerometer raw values
        acc_x = read_raw_data(ACCEL_XOUT_H)
        acc_y = read_raw_data(ACCEL_YOUT_H)
        acc_z = read_raw_data(ACCEL_ZOUT_H)

        #Read Gyroscope raw values
        gyro_x = read_raw_data(GYRO_XOUT_H)
        gyro_y = read_raw_data(GYRO_YOUT_H)
        gyro_z = read_raw_data(GYRO_ZOUT_H)

        #Give full scale range
        Ax = acc_x/16384.0
        Ay = acc_y/16384.0
        Az = acc_z/16384.0

        Gx = gyro_x/131.0
        Gy = gyro_y/131.0
        Gz = gyro_z/131.0

        #print("Gx = %.2f" % Gx u'\u00b0', "/s", "\tGy = %.2f" % Gy, u'\u00b0' + "/s", "\tGz = %.2f"  % Gz, u'u00b0', "/s")
        #print("Ax = %.2f" % Ax, u'u00b0', "\s", "\tAy = %.2f" % Ay, u'\u00b0' + "\s", "\tAz = %.2f" % Az, u'u00b0', "\s")
        #print("Gx = %.2f" % Gx)
        print("Ax = %.2f" % Ax, "Ay = %.2f" % Ay, "Az = %.2f" % Az)
        sleep(1)