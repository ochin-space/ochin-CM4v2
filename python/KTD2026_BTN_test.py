#sudo apt-get install python3-smbus
#dtparam=i2c_arm=on,i2c_arm_baudrate=400000
from smbus import SMBus
from RPi import GPIO
import time
#CPU Ref Number
GPIO.setmode(GPIO.BCM)
#set the GPIO4, pin 54 as input
GPIO.setup(4, GPIO.IN)
def main():
    # Define registers values from datasheet
    ENRST = 0x00  # 
    FlashPer1 = 0x01  # 
    FlashOn1 = 0x02  #
    FlashOn2 = 0x03  #
    ChCTRL = 0x04  #
    RampRate = 0x05  #ramp-up/down transitions from 0% to 100%
    Led1Iout = 0x06  #1 led brightness
    Led2Iout = 0x07  #2 led brightness
    Led3Iout = 0x08  #3 led brightness
    Led4Iout = 0x09  #4 led brightness(for KTD2027)
    i2cbus = SMBus(1)  # Create a new I2C bus
    time.sleep(1)
    i2caddress = 0x32  # Address of KTD2026 device
    try:
        #ENRSTstat = i2cbus.read_byte_data(i2caddress, ENRST)  # Read ENRST
        #print(ENRSTstat) # print the value ENRST
        ENRSTstat = i2cbus.write_byte_data(i2caddress, ENRST, 0x07)  # chip reset  
        print("chip reset done") 
    except:
        print("chip reset failed")  
        time.sleep(0.5)
        i2cbus.write_byte_data(i2caddress, ChCTRL, 0x15) #led 1,2,3 ON  
        print("LEDs 1,2,3 always on") 
    print("Blue") 
    i2cbus.write_byte_data(i2caddress, Led1Iout, 0xff)
    i2cbus.write_byte_data(i2caddress, Led2Iout, 0x00)
    i2cbus.write_byte_data(i2caddress, Led3Iout, 0x00)
    time.sleep(2)
    print("Green") 
    i2cbus.write_byte_data(i2caddress, Led1Iout, 0x00)
    i2cbus.write_byte_data(i2caddress, Led2Iout, 0xff)
    i2cbus.write_byte_data(i2caddress, Led3Iout, 0x00)
    time.sleep(2)
    print("Red") 
    i2cbus.write_byte_data(i2caddress, Led1Iout, 0x00)
    i2cbus.write_byte_data(i2caddress, Led2Iout, 0x00)
    i2cbus.write_byte_data(i2caddress, Led3Iout, 0xff)
    time.sleep(2)
    
    while (True):
        if GPIO.input(4) == 0:
            print("Blue") 
            i2cbus.write_byte_data(i2caddress, Led1Iout, 0xff)
            i2cbus.write_byte_data(i2caddress, Led2Iout, 0x00)
            i2cbus.write_byte_data(i2caddress, Led3Iout, 0x00)
        else:
            print("Green") 
            i2cbus.write_byte_data(i2caddress, Led1Iout, 0x00)
            i2cbus.write_byte_data(i2caddress, Led2Iout, 0xff)
            i2cbus.write_byte_data(i2caddress, Led3Iout, 0x00)


if __name__ == "__main__":
    main()