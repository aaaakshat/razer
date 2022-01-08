#!/usr/bin/env python3

from gattlib import DiscoveryService, GATTRequester as gr

DEVICE_ID = "21:03:44:00:02:60"

def rgb_to_bytes(r, g, b):
    return bytes(bytearray([0x56, hex(r), hex(g), hex(b), 0x00, 0xf0, 0xaa]))


def main():
    serve = DiscoveryService()
    devices = serve.discover(2)

    for name, address in devices.items():
        print("name: {}, address: {}".format(name, address))

    print("-----")
    print("Is {} available? (y/N)".format(DEVICE_ID))
    safe = input() == "y"

    if safe:
        req = gr(DEVICE_ID)
        flag = True
        while flag:
            r = int(input("R: "))
            g = int(input("G: "))
            b = int(input("B: "))
            req.write_by_handle(0x0009, rgb_to_bytes(r, g, b))

            flag = input("wanna put values again? (y/n)") == "y"


if __name__ == "__main__":
    main()
