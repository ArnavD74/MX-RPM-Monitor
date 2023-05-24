# MX-RPM-Monitor
A very simple python program to monitor a motor's cycle count and RPM/RPH and POST it to a Web UI. Theoretically will work for any two-pin motor with a switch connected in a "switch to ground" or "active low" setup. This has been tested on a Raspberry Pi 0W Rev 1.1 running 32-bit Raspbian OS with Desktop.

Please be advised that any potential damage incurred to your devices, be it caused by the code presented herein or resulting from electrical issues, shall be solely the responsibility of the user. Kindly exercise caution and ensure proper understanding of the code and hardware connections before implementation, as I, the author, absolve myself from any liabilities arising from such occurrences.

This project was created as an accessory to [Keekeen's MX Switch Break-in Machine](https://github.com/keekeen/MX-Switch-Break-In-Machine).

# Materials needed
1. Raspberry Pi (with access to GPIO pins)
2. Raspbian OS (which is pre-loaded with Python and the RPi.GPIO library)

If you're here from [this video](https://www.youtube.com/watch?v=KD2p3KXpSlM) then you will need to wire one switch per machine to a GPIO pin (and GND) to count actuations. The following materials will be needed:
1. [Amoeba Royale PCB](https://www.etsy.com/listing/1382786180/amoeba-royale-v20-single-switch-pcb), which can be found on Etsy and other similar marketplaces. 
2. One [hotswap socket](https://www.amazon.com/Hot-swappable-Socket-CPG151101S11-Mechanical-Keyboard/dp/B07K8CCMQZ) per PCB. These are found cheapest on AliExpress and similar marketplaces. 

# How to use

1. Install flask, numpy, and pandas using pip (`sudo pip install <package>`)
2. Connect your motor(s) to GND and GPIO pin 7, 11, etc. [Raspberry Pi Zero Pinout](https://images.theengineeringprojects.com/image/webp/2021/03/raspberry-pi-zero-5.png.webp?ssl=1)
3. Run `counter.py` and verify that the stream is recording inputs. You can also `cat count0.csv` to verify that the csv is being written to.
4. Run `server.py` in a different terminal.
5. [`screen`](https://linuxize.com/post/how-to-use-linux-screen/) can be used to keep things tidy without extra sessions.
6. On another device, use a web browser to visit the Pi's IP address followed by port 5000 (TCP via UPnP).
