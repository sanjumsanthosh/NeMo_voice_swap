import warnings
warnings.filterwarnings('ignore')

# import nemo
import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp
import nemo.collections.tts as nemo_tts

import os
# import IPython

import sounddevice as sd
from scipy.io.wavfile import write

audio_file_path = os.path.join(os.getcwd(), 'audio files','sample_audio.wav')
audio_file_path_pre = os.path.join(os.getcwd(), 'audio files','2086-149220-0033.wav')

# getting audio
x = input('enter any character to start recording.')
if(x):
    rec_time = 20
    fs = 44100

    myrecordings = sd.rec(int(rec_time * fs) , fs , channels= 1)
    sd.wait()


    # saving file as wav using soundfile
    write(audio_file_path , fs , myrecordings)

#automatic speech recogonition
quartznet = nemo_asr.models.EncDecCTCModel.from_pretrained(
    model_name="QuartzNet15x5Base-En"
    ).cuda()

files = [audio_file_path_pre]
raw_text = ''
text = ''
for fname, transcription in zip(files, quartznet.transcribe(paths2audio_files=files)):
  raw_text = transcription
  

#audioo processing automatic punctuations
punctuation = nemo_nlp.models.PunctuationCapitalizationModel.from_pretrained(
    model_name='Punctuation_Capitalization_with_DistilBERT'
    ).cuda()

res = punctuation.add_punctuation_capitalization(queries=[raw_text])


#text to audio generator
spectrogram_generator = nemo_tts.models.Tacotron2Model.from_pretrained(
    model_name="Tacotron2-22050Hz"
    ).cuda()
vocoder = nemo_tts.models.WaveGlowModel.from_pretrained(
    model_name="WaveGlow-22050Hz"
    ).cuda()



