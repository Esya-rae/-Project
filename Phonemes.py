from IPA_to_CMUBET import c_f

class Phonemes:
    data = []

    def __init__(self, decoded):
        self.data = [seg.word for seg in decoded]
        self.form = "CMUBET"

    def delete_silence(self):
        result = []
        for ph in self.data:
            if ph != 'SIL' and ph != '+SPN+':
                result.append(ph)
        self.data = result

    def delete_repetitions(self):
        result = []
        prev = '-1'
        for ph in self.data:
            if ph != prev:
                result.append(ph)
                prev = ph
        self.data = result

    def change_format(self):
        self.data = c_f.change_format(self.form, self.data)
        if self.form == "IPA":
            self.form = "CMUBET"
        else:
            self.form = "IPA"