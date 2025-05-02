![Alt text](images/logo.png?raw=true&=200x "ochin_CM4")
# ochin_CM4 v2.0.1
The öchìn CM4 it’s a tiny carrier board for the Raspberry Pi Compute Module  It is designed for applications where a powerful machine with low consumption and small dimensions is required. The small form factor makes it interesting for all those applications where the space available is not much and containing the weight is important, such as in robotics, home automation and IOT.

![Alt text](images/ochin_CM4_topDoc.png?raw=true "ochin_CM4")

![Alt text](images/ochin_CM4_botDoc.png?raw=true "ochin_CM4 back")

![Alt text](images/ochin_CM4_USBext_topDoc.png?raw=true "ochin_CM4extUSB")

![Alt text](images/ochin_CM4_USBext_botDoc.png?raw=true "ochin_CM4extUSB")


The board is compatible with all Raspberry Pi CM4 modules equipped with eMMC. Depending on your needs, you can select a CM4 module with an SDRAM starting from 1GB up to 8GB and the eMMC from 8GB up to 32GB, with or without the Wi-Fi/BT module.

Key features of the Raspberry Pi CM4 available on öchìn are as follows:
* Broadcom BCM2711, Quad core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5GHz
* Small Footprint 55mm × 40mm × 4.7mm module
* H.265 (HEVC) (up to 4Kp60 decode), H.264 (up to 1080p60 decode, 1080p30 encode)
* OpenGL ES 3.0 graphics
* Options for 1GB, 2GB, 4GB or 8GB LPDDR4-3200 SDRAM with ECC
* Options for 8GB, 16GB, or 32GB eMMC Flash
o Peak eMMC bandwidth 100MBytes/s
o 2.4 GHz, 5.0 GHz IEEE 802.11 b/g/n/ac wireless
o Bluetooth 5.0, BLE
o On board electronic switch to select between PCB trace or external antenna
* 1×USB 2.0 port (highspeed)

The öchìn CM4v2 board provides the following interfaces:

*	4x USB 2.0 480Mbps (4x SM04B-GHS-TB(LF)(SN) connectors)
*	1x USB Type-C (for flashing eMMC)
*	2x CSI camera (2x FH12-22S-0.5SH (55) connectors)
*	I2C1 (SM04B-GHS-TB(LF)(SN) connector)
*	SPI1 / 6 (SM06B-GHS-TB(LF)(SN) connector)
*	UART0 / 1 + Video Out (SM06B-GHS-TB(LF)(SN) connector)
*	UART4 / UART5 (SM06B-GHS-TB(LF)(SN) connector)
*	1x Ethernet transformerless 100Base-T
*	1x microHDMI
*	2x general purpose LEDs
*	1x RGB LED on external tiny board
*	1x general purpose button on external tiny board

The ochin_CM4v2 card introduces several new features compared to v1, some of which are very interesting and which considerably broaden its range of use. 

Below is a table in which it is possible to see which are the new fetures and which has been removed.

![Alt text](images/ochin_comparison_table.png?raw=true "ochin_CM4 comparison table")

In this repository you can find the [manual](öchìnCM4v2-Manual.pdf) of the board, a quick start guide for flashing the CM4 module and a guide with some tips on how to make the connections to the ochin board. 

It is important to read them both before turning on the ochin_CM4v2 board, to know its characteristics and above all the sequence in which the signals are present on the connectors.

# Where to buy the ochin_CM4 boards
The ochin_CM4 boards are manufactured and sold by Seeedstudio. You can purchase ochin_CM4 boards from Seeedstudio's marketplace, https://www.seeedstudio.com or from Seeedstudio's business partners (Digikey, Mouser, RS components and many others).

# License Notice for This GitHub Repository

This GitHub repository contains various resources that are subject to specific licenses. Please note the following information regarding the applicable licenses:

* Documentation, Manuals, PDF Schematics, scripts and Other Textual Content: All textual documents present in this repository, including manuals, schematics, and documentation, are released under the GNU Free Documentation License (GFDL).

* Hardware (KiCad Sources, Gerber Files, Assembly Files, etc.): The hardware-related items, including but not limited to KiCad sources, Gerber files, and assembly files, are subject to a proprietary license. This means that these resources are not released as open source and their use is governed by the terms specified in the accompanying documentation or separate terms of use provided.

Please respect the conditions of both licenses when using and distributing the materials in this repository.

For any questions or clarifications regarding the [LICENSE](LICENSE), feel free to contact us.

# Important!!!

Print and use the extractor for the CM4 module if you don't want to break the mezzanines, you can find the [ochin_mount-extractor.stl](3d/CoversTurretsAndExtractors/ochin_mount-extractor.stl) in the "3d/CoversTurretsAndExtractors" section of this repository.

Take a look at the [öchìnCM4v2-WiringAndSuggestions.pdf](öchìnCM4v2-WiringAndSuggestions.pdf) before power the board on, it may save your time and your devices.

Never trust the color code of the GHS cables, the sequence in which commercial GHS cables are assembled is often random and does not reflect the sequence of the signals present in the connectors of the ochin_CM4 board.

Please refer to the file [öchìnCM4v2-HW-bugs.pdf](öchìnCM4v2-HW-bugs.pdf) for details regarding known issues on the board and the respective version in which they were resolved