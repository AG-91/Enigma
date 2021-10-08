class PlugLead:
    import string
    alphabet = dict(zip(string.ascii_uppercase, string.ascii_uppercase))

    def __init__(self, mapping):
        self.mapping = mapping
        self.alphabet.update({self.mapping[0]: self.mapping[1], self.mapping[1]: self.mapping[0]})

    def encode(self, character):
        character = str(character)
        encoded = self.alphabet.get(character)
        return encoded


class Plugboard:

    def __init__(self):
        self.leads_coll = {}  # collection of leads

    def add(self, lead):
        if len(self.leads_coll) < 20:
            self.leads_coll.update({lead.mapping[0]: lead.mapping[1], lead.mapping[1]: lead.mapping[0]})

    def encode(self, character):
        if character in self.leads_coll:
            character = str(character)
            encoded = self.leads_coll.get(character)
            return encoded
        else:
            return character


class Rotor:

    # Rotor class supports 3 or 4 rotors and a reflector
    # Arguments are:
    #   1- rotor_label: a string of I, II, III, IV, V, Beta, or Gamma
    #   2- ring_setting: a set of integers ranging between 0 and 25. In my code I need
    #       to subtract 1 from the Notebook ring settings
    #   3- initial_positions: string of three capital alphabetical letters. No spaces.
    #   4- n: an indicator of notches on previous rotors. 1 = previous rotor on notch
    #         0 = previous rotor not on notch. 2 = previous rotor is notchless
    #   5- leads: collection of leads up to 10 pairs
    def __init__(self, rotor_label, ring_setting=0, initial_position=0, n=0, leads=()):

        self.ring_setting = ring_setting
        self.initial_position = initial_position
        self.n = n
        self.notch = self.notch
        self.leads = leads

        import string

        self.beta_ = ["L", "E", "Y", "J", "V", "C", "N", "I", "X", "W", "P", "B", "Q", "M", "D", "R", "T", "A", "K",
                      "Z",
                      "G", "F", "U", "H", "O", "S"]

        self.gamma_ = ["F", "S", "O", "K", "A", "N", "U", "E", "R", "H", "M", "B", "T", "I", "Y", "C", "W", "L", "Q",
                       "P",
                       "Z", "X", "V", "G", "J", "D"]

        self.i_ = ["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P",
                   "A", "I", "B", "R", "C", "J"]

        self.ii_ = ["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N",
                    "P", "Y", "F", "V", "O", "E"]

        self.iii_ = ["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A",
                     "K", "M", "U", "S", "Q", "O"]

        self.iv_ = ["E", "S", "O", "V", "P", "Z", "J", "A", "Y", "Q", "U", "I", "R", "H", "X", "L", "N", "F", "T", "G",
                    "K", "D", "C", "M", "W", "B"]

        self.v_ = ["V", "Z", "B", "R", "G", "I", "T", "Y", "U", "P", "S", "D", "N", "H", "L", "X", "A", "W", "M", "J",
                   "Q", "O", "F", "E", "C", "K"]
        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                         "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.rotor_label = rotor_label
        self.I = dict(zip(string.ascii_uppercase, self.i_))
        self.II = dict(zip(string.ascii_uppercase, self.ii_))
        self.III = dict(zip(string.ascii_uppercase, self.iii_))
        self.IV = dict(zip(string.ascii_uppercase, self.iv_))
        self.V = dict(zip(string.ascii_uppercase, self.v_))
        self.Beta = dict(zip(string.ascii_uppercase, self.beta_))
        self.Gamma = dict(zip(string.ascii_uppercase, self.gamma_))
        self.rotor_dic = {}

    def encode_right_to_left(self, character):
        n = 0
        # This method utilized by middle rotors from right to left

        if self.rotor_label == "I":
            self.rotor_dic = self.I

            self.notch = 16

            # signal if previous rotor was notchless
            if self.n == 2:
                self.initial_position = self.initial_position

            # rotate if rotor on its notch or previous rotor on notch
            if (
                    self.initial_position == self.notch or self.n == 1) and self.n != 2:
                self.initial_position += 1

            # sends a signal to next rotor if this rotor on its notch
            if self.initial_position == self.notch:
                n = 1

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]
            return char_out, n, final_position

        if self.rotor_label == "II":
            self.rotor_dic = self.II

            self.notch = 4

            # signal if previous rotor was notchless
            if self.n == 2:
                self.initial_position = self.initial_position

            # rotate if rotor on its notch or previous rotor on notch
            if (
                    self.initial_position == self.notch or self.n == 1) and self.n != 2:
                self.initial_position += 1

            # sends a signal to next rotor if this rotor on its notch
            if self.initial_position == self.notch:
                n = 1

            final_position = self.initial_position
            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]
            return char_out, n, final_position

        if self.rotor_label == "III":
            self.rotor_dic = self.III

            self.notch = 21

            # signal if previous rotor was notchless
            if self.n == 2:
                self.initial_position = self.initial_position

            # rotate if rotor on its notch or previous rotor on notch
            if (
                    self.initial_position == self.notch or self.n == 1) and self.n != 2:
                self.initial_position += 1

            # sends a signal to next rotor if this rotor on its notch
            if self.initial_position == self.notch:
                n = 1
            final_position = self.initial_position
            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]
            return char_out, n, final_position

        if self.rotor_label == "IV":
            self.rotor_dic = self.IV

            self.notch = 9

            # signal if previous rotor was notchless
            if self.n == 2:
                self.initial_position = self.initial_position

            # rotate if rotor on its notch or previous rotor on notch
            if (
                    self.initial_position == self.notch or self.n == 1) and self.n != 2:
                self.initial_position += 1

            # sends a signal to next rotor if this rotor on its notch
            if self.initial_position == self.notch:
                n = 1

            final_position = self.initial_position
            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]
            return char_out, n, final_position

        if self.rotor_label == "V":
            self.rotor_dic = self.V
            self.notch = 25

            # signal if previous rotor was notchless
            if self.n == 2:
                self.initial_position = self.initial_position

            # rotate if rotor on its notch or previous rotor on notch
            if (self.initial_position == self.notch or self.n == 1) and self.n != 2:
                # print("Rotor V on ots notch or previous rotor on notch")
                self.initial_position += 1

            # sends a signal to next rotor if this rotor on its notch
            if self.initial_position == self.notch:
                n = 1

            final_position = self.initial_position
            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]  # convert to F
            value1 = self.rotor_dic[char_alphabet]  # map to L
            index_value1 = self.alphabet.index(value1)  # L index = 11
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]
            return char_out, n, final_position

        if self.rotor_label == "Beta":
            self.rotor_dic = self.Beta

            if self.n == 1:
                self.initial_position += 1
            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]

            # sends signal that its notchless
            n = 2
            return char_out, n, final_position
        if self.rotor_label == "Gamma":
            self.rotor_dic = self.Gamma

            if self.n == 1:
                self.initial_position += 1
            final_position = self.initial_position
            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]

            # sends signal that it's notchless
            n = 2
            return char_out, n, final_position

    def rt_encode_right_to_left(self, character):
        n = 0
        # This method utilized by most right rotor to rotate with every keypress from right to left

        # Right most rotor will have the character in replaced if in plugboard
        # before entering
        if character in self.leads:
            encoded = self.leads.get(character)
            character = encoded

        if self.rotor_label == "I":
            self.rotor_dic = self.I

            self.notch = 16
            if self.initial_position == self.notch:
                n = 1

            index = self.alphabet.index(character)

            # rotation by 1

            index += 1

            final_position = self.initial_position + 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            index_out -= 1

            char_out = self.alphabet[index_out % 26]
            return char_out, n, final_position

        if self.rotor_label == "II":
            self.rotor_dic = self.II

            self.notch = 4
            if self.initial_position == self.notch:
                n = 1
            index = self.alphabet.index(character)
            # rotation by 1
            index += 1
            final_position = self.initial_position + 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            index_out -= 1
            char_out = self.alphabet[index_out % 26]
            return char_out, n, final_position

        if self.rotor_label == "III":
            self.rotor_dic = self.III

            self.notch = 21
            if self.initial_position == self.notch:
                n = 1

            index = self.alphabet.index(character)
            # rotation by 1
            index += 1
            final_position = self.initial_position + 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26

            index_out -= 1

            char_out = self.alphabet[index_out % 26]
            return char_out, n, final_position

        if self.rotor_label == "IV":
            self.rotor_dic = self.IV

            self.notch = 9
            if self.initial_position == self.notch:
                n = 1
            index = self.alphabet.index(character)
            # rotation by 1
            index += 1
            final_position = self.initial_position + 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26

            index_out -= 1

            char_out = self.alphabet[index_out % 26]
            return char_out, n, final_position

        if self.rotor_label == "V":
            self.rotor_dic = self.V

            self.notch = 25
            if self.initial_position == self.notch:
                n = 1

            index = self.alphabet.index(character)
            # rotation by 1
            index += 1
            final_position = self.initial_position + 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26

            index_out -= 1

            char_out = self.alphabet[index_out % 26]
            return char_out, n, final_position
        if self.rotor_label == "Beta":
            self.rotor_dic = self.Beta

            index = self.alphabet.index(character)
            # rotation by 1
            index += 1
            final_position = self.initial_position + 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26

            index_out -= 1

            char_out = self.alphabet[index_out % 26]
            # sends signal that it's notchless
            n = 2
            return char_out, n, final_position

        if self.rotor_label == "Gamma":
            self.rotor_dic = self.Gamma

            index = self.alphabet.index(character)
            # rotation by 1
            index += 1
            final_position = self.initial_position + 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26

            index_out -= 1

            char_out = self.alphabet[index_out % 26]
            # sends a signal that it's notchless
            n = 2
            return char_out, n, final_position

    def encode_left_to_right(self, character):
        n = 0
        # This method utilized by middle rotors from left to right

        if self.rotor_label == "I":
            self.rotor_dic = self.I

            self.notch = 16

            # signal if previous rotor was notchless
            if self.n == 2:
                self.initial_position = self.initial_position

            # rotate if rotor on its notch or previous rotor on notch
            if (
                    self.initial_position == self.notch or self.n == 1) and self.n != 2:
                self.initial_position += 1

            # sends a signal to next rotor if this rotor on its notch
            if self.initial_position == self.notch:
                n = 1

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.i_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            return char_alphabet, n, final_position

        if self.rotor_label == "II":
            self.rotor_dic = self.II

            self.notch = 4

            # signal if previous rotor was notchless
            if self.n == 2:
                self.initial_position = self.initial_position

            # rotate if rotor on its notch or previous rotor on notch
            if (
                    self.initial_position == self.notch or self.n == 1) and self.n != 2:
                self.initial_position += 1

            # sends a signal to next rotor if this rotor on its notch
            if self.initial_position == self.notch:
                n = 1

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.ii_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            return char_alphabet, n, final_position

        if self.rotor_label == "III":
            self.rotor_dic = self.III

            self.notch = 21

            # signal if previous rotor was notchless
            if self.n == 2:
                self.initial_position = self.initial_position

            # rotate if rotor on its notch or previous rotor on notch
            if (
                    self.initial_position == self.notch or self.n == 1) and self.n != 2:
                self.initial_position += 1

            # sends a signal to next rotor if this rotor on its notch
            if self.initial_position == self.notch:
                n = 1
            final_position = self.initial_position
            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.iii_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            return char_alphabet, n, final_position

        if self.rotor_label == "IV":
            self.rotor_dic = self.IV

            self.notch = 9

            # signal if previous rotor was notchless
            if self.n == 2:
                self.initial_position = self.initial_position

            # rotate if rotor on its notch or previous rotor on notch
            if (
                    self.initial_position == self.notch or self.n == 1) and self.n != 2:
                self.initial_position += 1

            # sends a signal to next rotor if this rotor on its notch
            if self.initial_position == self.notch:
                n = 1

            final_position = self.initial_position
            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.iv_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            return char_alphabet, n, final_position

        if self.rotor_label == "V":
            self.rotor_dic = self.V
            self.notch = 25

            # signal if previous rotor was notchless
            if self.n == 2:
                self.initial_position = self.initial_position

            # rotate if rotor on its notch or previous rotor on notch
            if (
                    self.initial_position == self.notch or self.n == 1) and self.n != 2:
                self.initial_position += 1

            # sends a signal to next rotor if this rotor on its notch
            if self.initial_position == self.notch:
                n = 1

            final_position = self.initial_position
            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.v_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            return char_alphabet, n, final_position

        if self.rotor_label == "Beta":
            self.rotor_dic = self.Beta
            if self.n == 1:
                self.initial_position += 1
            final_position = self.initial_position
            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.beta_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            n = 2
            return char_alphabet, n, final_position

        if self.rotor_label == "Gamma":
            self.rotor_dic = self.Gamma

            if self.n == 1:
                self.initial_position += 1
            final_position = self.initial_position
            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.gamma_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            n = 2
            return char_alphabet, n, final_position

    def rt_encode_left_to_right(self, character):
        n = 0
        # This method utilized by most right rotor from left to right to rotate with every keypress
        # It also swap letters if available inside plugboard before printing out final result

        if self.rotor_label == "I":
            self.rotor_dic = self.I

            self.notch = 16

            index = self.alphabet.index(character)
            index += 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.i_.index(self.alphabet[char_index_in])
            index -= 1
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            if char_alphabet in self.leads:
                encoded = self.leads.get(char_alphabet)
                char_alphabet = encoded
            return char_alphabet, n

        if self.rotor_label == "II":
            self.rotor_dic = self.II

            self.notch = 4

            index = self.alphabet.index(character)
            index += 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.ii_.index(self.alphabet[char_index_in])
            index -= 1
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            if char_alphabet in self.leads:
                encoded = self.leads.get(char_alphabet)
                char_alphabet = encoded
            return char_alphabet, n

        if self.rotor_label == "III":
            self.rotor_dic = self.III

            self.notch = 21

            index = self.alphabet.index(character)
            final_position = self.initial_position + 1
            index += 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.iii_.index(self.alphabet[char_index_in])
            index -= 1
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            if char_alphabet in self.leads:
                encoded = self.leads.get(char_alphabet)
                char_alphabet = encoded
            return char_alphabet, n

        if self.rotor_label == "IV":
            self.rotor_dic = self.IV

            self.notch = 9

            index = self.alphabet.index(character)
            index += 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.iv_.index(self.alphabet[char_index_in])
            index -= 1
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]

            if char_alphabet in self.leads:
                encoded = self.leads.get(char_alphabet)
                char_alphabet = encoded
            return char_alphabet, n

        if self.rotor_label == "V":
            self.rotor_dic = self.V

            self.notch = 25

            index = self.alphabet.index(character)
            index += 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.v_.index(self.alphabet[char_index_in])
            index -= 1
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            if char_alphabet in self.leads:
                encoded = self.leads.get(char_alphabet)
                char_alphabet = encoded
            return char_alphabet, n

        if self.rotor_label == "Beta":
            self.rotor_dic = self.Beta

            index = self.alphabet.index(character)
            index += 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.beta_.index(self.alphabet[char_index_in])
            index -= 1
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            if char_alphabet in self.leads:
                encoded = self.leads.get(char_alphabet)
                char_alphabet = encoded
            return char_alphabet, n

        if self.rotor_label == "Gamma":
            self.rotor_dic = self.Gamma

            index = self.alphabet.index(character)
            index += 1
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.gamma_.index(self.alphabet[char_index_in])
            index -= 1
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]  # convert to F
            if char_alphabet in self.leads:
                encoded = self.leads.get(char_alphabet)
                char_alphabet = encoded
            return char_alphabet, n

    def lft_encode_right_to_left(self, character):
        n = 0
        # This method is utilized by left most rotor in 4 rotors Enigmas
        # from right to left to make sure it never rotates

        if self.rotor_label == "I":
            self.rotor_dic = self.I

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]
            return char_out, n, final_position

        if self.rotor_label == "II":
            self.rotor_dic = self.II

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]
            return char_out, n, final_position

        if self.rotor_label == "III":
            self.rotor_dic = self.III

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]
            return char_out, n, final_position

        if self.rotor_label == "IV":
            self.rotor_dic = self.IV

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]
            return char_out, n, final_position

        if self.rotor_label == "V":
            self.rotor_dic = self.V

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]
            return char_out, n, final_position

        if self.rotor_label == "Beta":
            self.rotor_dic = self.Beta

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]
            return char_out, n, final_position

        if self.rotor_label == "Gamma":
            self.rotor_dic = self.Gamma

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            char_alphabet = self.alphabet[char_index_in]
            value1 = self.rotor_dic[char_alphabet]
            index_value1 = self.alphabet.index(value1)
            index_out = (index_value1 + self.ring_setting - self.initial_position) % 26
            char_out = self.alphabet[index_out]
            return char_out, n, final_position

    def lft_encode_left_to_right(self, character):
        n = 0
        # This method is utilized by left most rotor in 4 rotors Enigmas
        # from left to right to make sure it never rotates

        if self.rotor_label == "I":
            self.rotor_dic = self.I

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.i_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            return char_alphabet, n, final_position

        if self.rotor_label == "II":
            self.rotor_dic = self.II

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.ii_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            return char_alphabet, n, final_position

        if self.rotor_label == "III":
            self.rotor_dic = self.III

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.iii_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            return char_alphabet, n, final_position

        if self.rotor_label == "IV":
            self.rotor_dic = self.IV

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.iv_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            return char_alphabet, n, final_position

        if self.rotor_label == "V":
            self.rotor_dic = self.V

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.v_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            return char_alphabet, n, final_position

        if self.rotor_label == "Beta":
            self.rotor_dic = self.Beta

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.beta_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            return char_alphabet, n, final_position

        if self.rotor_label == "Gamma":
            self.rotor_dic = self.Gamma

            final_position = self.initial_position

            index = self.alphabet.index(character)
            char_index_in = (index + self.initial_position - self.ring_setting) % 26
            index = self.gamma_.index(self.alphabet[char_index_in])
            char_alphabet = self.alphabet[(index - self.initial_position + self.ring_setting) % 26]
            return char_alphabet, n, final_position

    def notch(self):
        if self.rotor_label == "I":
            notch = 16
        if self.rotor_label == "II":
            notch = 4
        if self.rotor_label == "III":
            notch = 21
        if self.rotor_label == "IV":
            notch = 9
        if self.rotor_label == "V":
            notch = 25


class Reflector:
    # Reflect the letter coming from left most rotor using pairs of letters
    # depending on the reflector type A, B, or C

    def __init__(self, ref_type):
        import string
        a_ = ["E", "J", "M", "Z", "A", "L", "Y", "X", "V", "B", "W", "F", "C", "R", "Q", "U", "O", "N", "T", "S",
              "P", "I", "K", "H", "G", "D"]

        b_ = ["Y", "R", "U", "H", "Q", "S", "L", "D", "P", "X", "N", "G", "O", "K", "M", "I", "E", "B", "F", "Z",
              "C", "W", "V", "J", "A", "T"]

        c_ = ["F", "V", "P", "J", "I", "A", "O", "Y", "E", "D", "R", "Z", "X", "W", "G", "C", "T", "K", "U", "Q",
              "S", "B", "N", "M", "H", "L"]
        self.ref_type = ref_type
        self.A = dict(zip(string.ascii_uppercase, a_))
        self.B = dict(zip(string.ascii_uppercase, b_))
        self.C = dict(zip(string.ascii_uppercase, c_))
        self.ref_dic = {}

    def reflect(self, character):
        if self.ref_type == "A":
            self.ref_dic = self.A
        if self.ref_type == "B":
            self.ref_dic = self.B
        if self.ref_type == "C":
            self.ref_dic = self.C
        char_reflect = self.ref_dic.get(character)
        return char_reflect


class Enigma:
    # Enigma class utilizes the encoding codes in Rotor class by assigning the
    # right methods based on the order and label of rotors, and correct settings accordingly
    #
    # The Enigma class takes arguments to be assigned to Rotor class and Plugboard class
    # It also initially takes the text to decode/encode

    def __init__(self, rotors, reflector, text, initial_pos=(), ring_settings=(), plugleads={}):
        self.rotors = rotors
        self.reflector = reflector
        self.plugleads = plugleads
        self.ring_settings = ring_settings
        self.initial_pos = initial_pos
        self.text = text

    def run(self):
        import string
        out_list = []

        for char in self.text:

            # 3 Rotors
            if len(self.rotors) == 3:
                # assigning rotors
                left_rotor = self.rotors[0]
                right_rotor = self.rotors[-1]
                middle_rotor = self.rotors[1]

                # initial positions
                right_initial_position = string.ascii_uppercase.index(self.initial_pos[-1])
                middle_initial_position = string.ascii_uppercase.index(self.initial_pos[1])
                left_initial_position = string.ascii_uppercase.index(self.initial_pos[0])

                # ring settings
                right_ring = self.ring_settings[-1]
                middle_ring = self.ring_settings[1]
                left_ring = self.ring_settings[0]

                # encoding right to left

                out_list1 = list(Rotor(right_rotor, ring_setting=right_ring, \
                                       initial_position=right_initial_position,
                                       leads=self.plugleads).rt_encode_right_to_left(char))

                out_char1 = out_list1[0]

                out_list2 = list(Rotor(middle_rotor, ring_setting=middle_ring, \
                                       initial_position=middle_initial_position, n=out_list1[1],
                                       leads=self.plugleads).encode_right_to_left(
                    out_char1))

                out_char2 = out_list2[0]

                out_list3 = list(Rotor(left_rotor, ring_setting=left_ring, \
                                       initial_position=left_initial_position, n=out_list2[1],
                                       leads=self.plugleads).encode_right_to_left(
                    out_char2))

                out_char3 = out_list3[0]

                # reflecting
                ref = Reflector(self.reflector)
                reflect_char = ref.reflect(out_char3)

                # encoding left to right
                out_list4 = list(Rotor(left_rotor, ring_setting=left_ring, \
                                       initial_position=left_initial_position, n=out_list2[1],
                                       leads=self.plugleads).encode_left_to_right(
                    reflect_char))
                out_char4 = out_list4[0]

                out_list5 = list(Rotor(middle_rotor, ring_setting=middle_ring, \
                                       initial_position=middle_initial_position, n=out_list1[1],
                                       leads=self.plugleads).encode_left_to_right(
                    out_char4))
                out_char5 = out_list5[0]

                out_list6 = list(Rotor(right_rotor, ring_setting=right_ring, \
                                       initial_position=right_initial_position,
                                       leads=self.plugleads).rt_encode_left_to_right(out_char5))
                out_char6 = out_list6[0]

                # assigning final positions after previous rotations
                right_final_position = out_list1[2]
                middle_final_position = out_list2[2]
                left_final_position = out_list3[2]

                final_positions = string.ascii_uppercase[left_final_position % 26] + string.ascii_uppercase[
                    middle_final_position % 26] \
                                  + string.ascii_uppercase[right_final_position % 26]
                self.initial_pos = final_positions

                # Adding the resulted character to output string
                out_list.append(out_char6)

            # 4 Rotors
            if len(self.rotors) == 4:
                # assigning rotors
                left_rotor = self.rotors[0]
                right_rotor = self.rotors[-1]
                middle_right_rotor = self.rotors[2]
                middle_left_rotor = self.rotors[1]

                # initial positions
                right_initial_position = string.ascii_uppercase.index(self.initial_pos[-1])
                middle_right_initial_position = string.ascii_uppercase.index(self.initial_pos[2])
                middle_left_initial_position = string.ascii_uppercase.index(self.initial_pos[1])
                left_initial_position = string.ascii_uppercase.index(self.initial_pos[0])

                # ring settings
                right_ring = self.ring_settings[-1]
                middle_right_ring = self.ring_settings[2]
                middle_left_ring = self.ring_settings[1]
                left_ring = self.ring_settings[0]

                # encoding right to left
                out_list1 = list(Rotor(right_rotor, ring_setting=right_ring, \
                                       initial_position=right_initial_position,
                                       leads=self.plugleads).rt_encode_right_to_left(char))

                out_char1 = out_list1[0]

                out_list2 = list(Rotor(middle_right_rotor, ring_setting=middle_right_ring, \
                                       initial_position=middle_right_initial_position, n=out_list1[1],
                                       leads=self.plugleads).encode_right_to_left(
                    out_char1))

                out_char2 = out_list2[0]

                out_list3 = list(Rotor(middle_left_rotor, ring_setting=middle_left_ring, \
                                       initial_position=middle_left_initial_position, n=out_list2[1],
                                       leads=self.plugleads).encode_right_to_left(
                    out_char2))

                out_char3 = out_list3[0]

                out_list4 = list(Rotor(left_rotor, ring_setting=left_ring, \
                                       initial_position=left_initial_position, n=out_list3[1],
                                       leads=self.plugleads).lft_encode_right_to_left(
                    out_char3))

                out_char4 = out_list4[0]

                # reflecting
                ref = Reflector(self.reflector)
                reflect_char = ref.reflect(out_char4)

                # encoding left to right
                out_list5 = list(Rotor(left_rotor, ring_setting=left_ring, \
                                       initial_position=left_initial_position,
                                       leads=self.plugleads).lft_encode_left_to_right(
                    reflect_char))

                out_char5 = out_list5[0]

                out_list6 = list(Rotor(middle_left_rotor, ring_setting=middle_left_ring, \
                                       initial_position=middle_left_initial_position, n=out_list2[1],
                                       leads=self.plugleads).encode_left_to_right(out_char5))

                out_char6 = out_list6[0]

                out_list7 = list(Rotor(middle_right_rotor, ring_setting=middle_right_ring, \
                                       initial_position=middle_right_initial_position, n=out_list1[1],
                                       leads=self.plugleads).encode_left_to_right(out_char6))

                out_char7 = out_list7[0]

                out_list8 = list(Rotor(right_rotor, ring_setting=right_ring, \
                                       initial_position=right_initial_position,
                                       leads=self.plugleads).rt_encode_left_to_right(out_char7))

                out_char8 = out_list8[0]

                # Assigning final positions of rotors after previous rotations
                right_final_position = out_list1[2]
                middle_right_final_position = out_list2[2]
                middle_left_final_position = out_list3[2]
                left_final_position = out_list4[2]

                final_positions = string.ascii_uppercase[left_final_position % 26] + string.ascii_uppercase[
                    middle_left_final_position % 26] \
                                  + string.ascii_uppercase[middle_right_final_position % 26] \
                                  + string.ascii_uppercase[right_final_position % 26]

                self.initial_pos = final_positions

                # Adding the resulted character to output string
                out_list.append(out_char8)

        # Returning the final output string
        return "".join(out_list)


if __name__ == "__main__":

    pass

