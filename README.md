# -RPM-Monitor
A very simple python program to monitor a motor's cycle count and RPM/RPH. Theoretically will work for any two-pin motor with a switch connected with a "switch to ground" or "active low" setup.

Please be advised that any potential damage incurred to your devices, be it caused by the code presented herein or resulting from electrical issues, shall be solely the responsibility of the user. Kindly exercise caution and ensure proper understanding of the code and hardware connections before implementation, as I, the author, absolve myself from any liabilities arising from such occurrences.

This project was created as an accessory to [Keekeen's MX Switch Break-in Machine](https://github.com/keekeen/MX-Switch-Break-In-Machine).

# Materials needed
1. Raspberry Pi (with access to GPIO)
2. Raspbian OS (pre-loaded with Python and RPi.GPIO library)

# How to use

1. Install flask, numpy, and pandas using pip
2. Connect your motor(s) to GND and GPIO pin 7, 11, etc. (Default is 7 and 11). [Raspberry Pi Zero Pinout](https://images.theengineeringprojects.com/image/webp/2021/03/raspberry-pi-zero-5.png.webp?ssl=1)
3. Run `counter.py` and verify that the stream is recording inputs. You can also `cat count0.csv` to verify that the csv is being written to.
4. Run `server.py` in a different terminal; [screen](https://linuxize.com/post/how-to-use-linux-screen/) can be used to keep things tidy.
5. On another device, use a web browser to visit the Pi's IP address followed by port 5000 (TCP via UPnP).
