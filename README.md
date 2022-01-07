# Razer 

Have a cheap LED strip that's controlled by a suspicious 1 star app?

Razer is a lightweight RGB controller that let's you scan and talk to BLE LED strips.

-----
### Reverse Engineering My Roomate's LED Strip

Received?: 660423412019ff2000000399

Device: AP-210344000260(-60)
ID: KlbkewgR8K5rzExy3mfyQw==

identifier:     251385E1-E5B1-A22A-70C1-BC056642B5B9 
MAC:       - 
Local Name:   AP-210344000260

Services:
1. FFD5 
    - FFDA (empty?)
    - FFD9 (writing)
2. FFD0 
    - FFD4 (reading)
    - FFD1 (empty?)

Current understanding:
660423412019ff2000000399
6604 (prefix) 234 (3 means on/ 4 means off) 12019 (infix) ff2000 (color values) 000399 (suffix)

Notifies (Hex):
Red on: 660424412019E50000000399
Red off: 660423412019E50000000399
white on: 660423412019E50000000399
white off: 660423412019E50000000399

660423412019ff2000000399


**Update:**
It seems that I can't rebroadcast incoming signals as there is some obfuscation happening. However it seems this BLE controller is the same as the one used in [this nice reverse engineering project](https://urish.medium.com/reverse-engineering-a-bluetooth-lightbulb-56580fcb7546#.puoo705sd) so the signals he's sending should work on our LED strips as well

RGB Format: 56 RR GG BB 00 f0 aa
E.g. violet: 0x56ff085a00f0aa

White Color Format: 56 00 00 00 WW 0f aa
WW is intensity

Fade format: bb II SS 44
E.g. all color fade 1 second delay: 0xbb250544
Where II is the index of lighting mode (25 - 38)
SS is the speed each unit is 200ms so 05 is 1 second


TODO:
- [ ] Half duplex BLE comms on Mac
- [ ] Packet decomposition
- [ ] Get signal writing format
- [ ] Understand notify signals

