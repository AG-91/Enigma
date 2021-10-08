from itertools import combinations
from itertools import permutations
import string
from enigma import *

plugboard = Plugboard()

# Code1:
plugboard.add(PlugLead("KI"))
plugboard.add(PlugLead("XN"))
plugboard.add(PlugLead("FL"))
for r in ("A", "B", "C"):
    enigma1 = Enigma(rotors=["Beta", "Gamma", "V"], reflector=r,
                     text="DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ",
                     initial_pos="MJM", \
                     ring_settings=(3, 1, 13), plugleads=plugboard.leads_coll)
    out = enigma1.run()
    if "SECRETS" in out:
        print("Code 1 breaking solution:")
        print("Decoded string: " + out)
        print("Reflector: " + r)
        print(""
              ""
              "")

# Code 2:
plugboard2 = Plugboard()
plugboard2.add(PlugLead("VH"))
plugboard2.add(PlugLead("PT"))
plugboard2.add(PlugLead("ZG"))
plugboard2.add(PlugLead("BJ"))
plugboard2.add(PlugLead("EY"))
plugboard2.add(PlugLead("FS"))
s = string.ascii_uppercase
p = permutations(s, 3)
y = ["".join(i) for i in p]
for x in y:
    enigma2 = Enigma(rotors=["Beta", "I", "III"], reflector="B",
                     text="CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH", initial_pos=x, \
                     ring_settings=(22, 1, 9), plugleads=plugboard2.leads_coll)
    out = enigma2.run()
    if "UNIVERSITY" in out:
        print("Code 2 breaking solution:")
        print("Decoded string: " + out)
        print("Starting Positions: " + x)
        print(""
              ""
              "")

# Code 4 attempt
# not successful

plugboard = Plugboard()
print("Code 4 attempt: "
      ""
      ""
      "")
r = ["V", "III", "IV"]
ref = "A"
pos_i = "SWU"
text_ = "SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW"
rings = (23, 11, 9)
list_I = ["ID", "IE", "IK", "IL", "IM", "IO", "IQ", "IT", "IU", "IX", "IY", "IZ"]
list_A = ["AD", "AE", "AK", "AL", "AM", "AO", "AQ", "AT", "AU", "AX", "AY", "AZ"]
leads_collection = ["WP", "RJ", "HN", "CG", "BS", "VF"]
for a in list_A:
    for i in list_I:
        if len(leads_collection) > 8:
            leads_collection.pop(-1)
            leads_collection.pop(-1)
        leads_collection.append(a)
        leads_collection.append(i)

    for d in leads_collection:
        plugboard.add(PlugLead(d))

        enigma4 = Enigma(rotors=["V", "III", "IV"], reflector="A",
                     text="SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW",
                     initial_pos="SWU", \
                     ring_settings=(23, 11, 9), plugleads=plugboard.leads_coll)
        out = enigma4.run()

    if "TUTOR" in out:
        print(plugboard.leads_coll)
        print(out)
    else:
        plugboard.leads_coll.popitem()
        plugboard.leads_coll.popitem()
        plugboard.leads_coll.popitem()
        plugboard.leads_coll.popitem()
        leads_collection.pop(-1)
        leads_collection.pop(-1)
        enigma = Enigma(rotors=r, reflector=ref, text=text_, \
                        initial_pos=pos_i, ring_settings=rings, plugleads={})