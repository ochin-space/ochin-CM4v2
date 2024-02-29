#sudo apt-get install python3-smbus
#dtparam=i2c_arm=on,i2c_arm_baudrate=400000
from smbus import SMBus
import time

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
    
	#i2cbus.write_byte_data(i2caddress, FlashPer1, 0x8e) #Flash period 1.92sec, linear rate
	#i2cbus.write_byte_data(i2caddress, FlashOn1, 0x50) #ON Timer1 %
	#i2cbus.write_byte_data(i2caddress, FlashOn2, 0x32) #ON Timer2 %
	#i2cbus.write_byte_data(i2caddress, ChCTRL, 0x2a) #led 1,2,3 Tim1 
	#i2cbus.write_byte_data(i2caddress, RampRate, 0x11) #ramp rate 1x, 128ms rise/fall time
    
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
        for b in range(0,50,5):
            for g in range(0,50,5):
                for r in range(0,50,5):
                    i2cbus.write_block_data(i2caddress, Led1Iout, [b, g, r])
                    time.sleep(0.001)
        for b in range(0,50,5):
            for g in range(0,50,5):
                for r in range(0,50,5):
                    i2cbus.write_block_data(i2caddress, Led1Iout, [50-b, 50-g, 50-r])
                    time.sleep(0.001)
                    
if __name__ == "__main__":
    main()