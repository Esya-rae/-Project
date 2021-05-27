class CHANGE_FORMAT:

    def __init__(self):
        self.CMUBET_container = ['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'B', 'CH', 'D', 'DH', 'EH', 'ER', 'EY', 'F', 'G', 'HH', 'IH', 'IY', 'JH', 'K', 'L', 'M', 'N', 'NG', 'OW', 'OY', 'P', 'R', 'S', 'SH', 'SIL', 'T', 'TH', 'UH', 'UW', 'V', 'W', 'Y', 'Z', 'ZH']
        self.IPA_container = ['ɑ', 'æ', 'ʌ', 'ɔ', 'ɑʊ', 'ɑɪ', 'b', 'ʧ', 'd', 'ð', 'ɛ', 'ɜɹ', 'eɪ', 'f', 'ɡ', 'h', 'i', 'ɪː', 'ʤ', 'k', 'l', 'm', 'n', 'ŋ', 'oʊ', 'ɔɪ', 'p', 'ɹ', 's', 'ʃ', '.', 't', 'θ', 'ʊ', 'u', 'v', 'w', 'j', 'z', 'ʒ']
        self.CMUBET_dict = dict()
        for i in range(len(self.CMUBET_container)):
            self.CMUBET_dict[self.CMUBET_container[i]] = i
        self.IPA_dict = dict()
        for i in range(len(self.IPA_container)):
            self.IPA_dict[self.IPA_container[i]] = i

    def CMUBET_to_IPA(self, phonemes):
        result = []
        for ph in phonemes:
            result.append(self.IPA_container[self.CMUBET_dict[ph]])
        return result

    def IPA_to_CMUBET(self, phonemes):
        result = []
        for ph in phonemes:
            result.append(self.CMUBET_container[self.IPA_dict[ph]])
        return result

    def change_format(self, form, phonemes):
        if form == "IPA":
            return self.IPA_to_CMUBET(phonemes)
        else:
            return self.CMUBET_to_IPA(phonemes)


c_f = CHANGE_FORMAT()