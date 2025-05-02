#sudo apt-get install python3-smbus
#dtparam=i2c_arm=on,i2c_arm_baudrate=400000
from smbus import SMBus
import time

i2cbus = SMBus(1)  # Create a new I2C bus
EMC2301_ADDRESS = 0x2f
Fan1Setting = 0x30
TACH_LSB_REG = 0x3E  # Reg LSB
TACH_MSB_REG = 0x3F  # Reg MSB

def count2RPM(count):
    EDGES_PER_REV = 2
    rpm = 3932160*2/count
    return rpm

def readTacho():
    lsb = i2cbus.read_byte_data(EMC2301_ADDRESS, TACH_LSB_REG)
    msb = i2cbus.read_byte_data(EMC2301_ADDRESS, TACH_MSB_REG)
    tach_count = (msb << 8) | lsb
    return count2RPM(tach_count)

def main():
    
    i2cbus.write_byte_data(EMC2301_ADDRESS, Fan1Setting, 0x00)
    time.sleep(4)   
    print("tacho: "+"%.2f" % readTacho())
    i2cbus.write_byte_data(EMC2301_ADDRESS, Fan1Setting, 0x64)
    time.sleep(4)
    print("tacho: "+"%.2f" % readTacho())
    i2cbus.write_byte_data(EMC2301_ADDRESS, Fan1Setting, 0xff)
    time.sleep(4)
    print("tacho: "+"%.2f" % readTacho())
    i2cbus.write_byte_data(EMC2301_ADDRESS, Fan1Setting, 0x64)
    time.sleep(4)
    print("tacho: "+"%.2f" % readTacho())


if __name__ == "__main__":
    main()