#!/usr/bin/env python

import subprocess
import optparse
import re


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


def get_current_mac(interface):
    output = subprocess.check_output(["ifconfig", interface])
    result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    if result:
        return result.group(0)
    else:
        print("[-] Could not find any MAC address")
        exit()


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("[+] Current MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print("[+] MAC address is successfully changed to "+current_mac)
else:
    print("[-] MAC address is not changed")
