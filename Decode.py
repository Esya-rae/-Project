from os import environ, path, listdir
import soundfile as sf
import librosa

import pocketsphinx
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from Phonemes import Phonemes
from Word import Word

class To_phonemes():

    def __init__(self) -> None:
        DIR = "/usr/local/lib/python3.8/dist-packages/pocketsphinx/"
        MODELDIR = DIR + "model"
        DATADIR = './data'
        self.TEMP_RAW_PATH = path.join(DATADIR, 'temp.raw')

        config = Decoder.default_config()
        config.set_string('-hmm', path.join(MODELDIR, 'en-us'))
        config.set_string('-allphone', path.join(MODELDIR, 'en-us/en-us-phone.lm.dmp'))
        config.set_string('-logfn', 'nul')
        config.set_float('-lw', 2.0)
        config.set_float('-beam', 1e-20)
        config.set_float('-pbeam', 1e-20)

        # Decode streaming data.
        self.decoder = Decoder(config)
    
    def decode(self, path):
        # Convert into 16KHz mono '.raw' file
        print(path)
        y, sr = librosa.load(path, sr=16000, mono=True)
        sf.write(file=self.TEMP_RAW_PATH, data=y, samplerate=sr, subtype='PCM_16', format='RAW')
        self.decoder.start_utt()
        stream = open(self.TEMP_RAW_PATH, 'rb')
        while True:
            buf = stream.read(1024)
            if buf:
                self.decoder.process_raw(buf, False, False)
            else:
                break
        self.decoder.end_utt()
        #print('Best hypothesis segments: ', [seg.word for seg in self.decoder.seg()])
        phonemes = Phonemes(self.decoder.seg())
        phonemes.delete_silence()
        phonemes.delete_repetitions()
        phonemes.change_format()
        print(phonemes)
        return phonemes


