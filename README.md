 # GPIO-OSC

 Send OSC Messages with Raspberry Pi GPIO Triggers and WebSocket Triggers

 ## Getting Started

 This system is designed to run on a raspberry pi. The base operating system that is recommended is [DietPi](https://dietpi.com/). A 2GB or larger SD will be required.

 ### Installing

 - [Part 1 - Setting Up The Pi](/docs/Setting_Up_The_Pi.md)
 - [Part 2 - OSC Installation](/docs/OSC_Installation.md)
 - :exclamation:[Wiring Reference](/docs/#)


 ### TODO:
  - **Move Remaining TODO to Github Issues**
  - Ability to edit config
  - GPIO Integration
  - Fix Websocket disconnect error
  - Send config to WEBUI on WS.connect
  - Use config to populate WebUI
  - Create devices to commands fire to device instead of saving ip and port on every command
  - GPIO Config to assign button
  - Define buttons a WebUI display name


 ## Versioning

 This project uses [SemVer](http://semver.org/) for versioning.

 ## Acknowledgments

   - The Fine People at the Raspberry Pi Foundation [https://www.raspberrypi.org/](https://www.raspberrypi.org/)
   - The People Behind DietPi [https://dietpi.com/](https://dietpi.com/)
   - The Communities Behind These Projects:
      - [http://www.proftpd.org/](http://www.proftpd.org/)
      - [https://memcached.org/](https://memcached.org/)
      - [https://www.lighttpd.net/](https://www.lighttpd.net/)
      - [https://www.python.org/](https://www.python.org/)
      - [https://pip.pypa.io/en/stable/](https://pip.pypa.io/en/stable/)
      - [https://pypi.org/project/pymemcache/](https://pypi.org/project/pymemcache/)
      - [https://pypi.org/project/RPi.GPIO/](https://pypi.org/project/RPi.GPIO/)
      - [https://pypi.org/project/python-osc/](https://pypi.org/project/python-osc/)
      - [https://pypi.org/project/websockets/](https://pypi.org/project/websockets/)
   - And These References:
      - GPIO Button: [https://raspberrypi.stackexchange.com/questions/76342/run-a-shell-script-from-a-python-script-when-a-button-is-pressed](https://raspberrypi.stackexchange.com/questions/76342/run-a-shell-script-from-a-python-script-when-a-button-is-pressed)
      - Function Calling: [https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script](https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script)
      - Run A Script On Boot: [https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/](https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)
