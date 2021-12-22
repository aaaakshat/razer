# Smart LED

Have a cheap LED strip that's controlled by a suspicious 1 star app?

Smeld is a lightweight RGB controller that let's you scan and talk to BLE LED strips.

-----
### Notes

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
6604 (prefix) 234 (3 means on/ 4 means off) 12019 (suffix) ff2000000399 (color value)

Notifies (Hex):
660424412019ff2000000399
660423412019ff2000000399


TODO:
[ ] Half duplex BLE comms on Mac
[ ] Packet decomposition
[ ] Get signal writing format
[ ] Understand notify signals

