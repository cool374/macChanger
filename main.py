#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Provide interface to change the MAC Address")
    parser.add_option("-m", "--mac_address", dest="new_mac", help="Provide new MAC address to change to")
    (option, arguments) = parser.parse_args()
    if not option.interface:
        parser.error("Please Specify an interface. Use --help for more info")
    elif not option.new_mac:
        parser.error("Please Specify new MAC Address. Use --help for more info")
    return option


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
