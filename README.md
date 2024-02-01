# MX-RPM-Monitor

A straightforward Python program designed to monitor and report the cycle count and RPM/RPH of a motor. It's compatible with any two-pin motor linked to a switch in a "switch to ground" or "active low" configuration. The application has been successfully tested on a Raspberry Pi 0W Rev 1.1 running the 32-bit Raspbian OS with Desktop.

**Disclaimer:** The user assumes full responsibility for any potential damage to devices resulting from the use of this code or related electrical issues. It is strongly recommended that users thoroughly understand the code and hardware connections before proceeding. The author is not liable for any damages or losses that may occur.

This tool is an enhancement for [Keekeen's MX Switch Break-in Machine](https://github.com/keekeen/MX-Switch-Break-In-Machine).

## Required Materials
- Raspberry Pi (with GPIO pin access)
- Raspbian OS (includes Python and RPi.GPIO library)
<br><br>

For those following [this instructional video](https://www.youtube.com/watch?v=KD2p3KXpSlM), you'll need to connect each machine's switch to a GPIO pin and GND for actuation counting. Additional required materials include:
- [Amoeba Royale PCB](https://www.etsy.com/listing/1382786180/amoeba-royale-v20-single-switch-pcb) - Available on Etsy and similar platforms.
- Hotswap socket (e.g., [Amazon Link](https://www.amazon.com/Hot-swappable-Socket-CPG151101S11-Mechanical-Keyboard/dp/B07K8CCMQZ)) - AliExpress and similar sites offer competitive prices.

## Installation and Usage

1. Install Flask, NumPy, and Pandas using pip: `sudo pip install flask numpy pandas`
2. Connect the motor(s) to GND and a GPIO pin (e.g., pin 7, 11). Refer to the [Raspberry Pi Zero Pinout](https://images.theengineeringprojects.com/image/webp/2021/03/raspberry-pi-zero-5.png.webp?ssl=1).
3. Execute `counter.py` and confirm that inputs are being recorded. To check if the CSV file is being updated, use `cat count0.csv`.
4. In a separate terminal, run `server.py`.
5. Utilize [`screen`](https://linuxize.com/post/how-to-use-linux-screen/) to manage sessions efficiently.
6. Access the Web UI by navigating to the Pi's IP address and appending port 5000 in a web browser on a different device (e.g., `http://<Pi-IP>:5000`).
