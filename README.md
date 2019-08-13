# rovercontrol  

A simple tkinter python app to control [APP4MC rovers](https://app4mc-rover.github.io/rover-docs/) 
via [HONO](https://eclipse.org/hono) using AMQPS.

# Requirements

Requires `python3` to run.

See requirements.txt for python library dependencies. The requirements should be satisfied 
by the installation steps below.

# Installation

* Install TK for Python 3 using `sudo apt install python3-tk` (or similar commands 
  on non-Debian/Ubuntu systems)
* Install [cli-proton-python](https://cli-proton-python.readthedocs.io/en/latest/) using `sudo 
  pip3 install cli-proton-python`
* If you get SSL errors when running the script, rebuild `python-qpid-proton` (used 
  by `cli-proton-python`) with SSL support from OpenSSL. Building with OpenSSL requires 
  `python-pkgconfig` to find OpenSSL - `python-pkgconfig` might be missing. Below script 
  makes sure it is present.
  * Uninstall the packages without SSL first `sudo pip3 uninstall python-qpid-proton cli-proton-python`
  * Make sure `python-pkgconfig` is available: `sudo apt install python-pkgconfig`
  * Rebuild with verbose output: `sudo pip3 -v install cli-proton-python` should show 
    `Using openssl version 1.0.2n (found via pkg-config)` if you still get `Warning: OpenSSL not installed - disabling SSL support!` 
    SSL will keep failing.

# Use

* Adapt the following constants in the `Rover_Control.py` script
  * `password` the password Hono's `consumer@HONO` user
  * `hostAndPort` the host name and the AMQPS port of the Hono dispatch router in the format 
    `<hostname>:<port>`
  * `tenant` the Hono tenant that contains the rover to control
  * `device` the Hono device ID of the device to control
  * `trustStore` a trust store (i.e. a certificate) in PEM format that contains either the
    certificate presented by the host to connect to or the certificate of the CA that
    issued the certificate.
* Start using `python3 Rover_Control.py`