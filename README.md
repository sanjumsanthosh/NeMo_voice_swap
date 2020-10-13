# A brief intoduction to Nvidia free NeMo extension pack  

---

Conversational AI mainly has 3 parts

1. automatic speech recogonition (ASR)
2. natural language processing (NLP)
3. and speech synthesis(TTS)

NVIDIA NeMo (**Ne**ural **mo**dules) helps to quickly build , train and fine-tune conerdational AI models.
Comman collections found on NeMo are as follows 

1. [NeMo speech collection (nemo_asr)](https://nvda.ws/36bgfEd)
2. [Nemo NLP collection(nemo_nlp)](https://nvda.ws/36eHEFh)
3. [Nemo speach synthesis(nemo_tts)](https://nvda.ws/3396Tqr)

## Instrallation

---

nemo is available as docker container and its the easiest way \
more infomation is linked here [Nvidia/nemo in github](https://github.com/NVIDIA/NeMo)\
pythorch medium article abour NeMo and sample codes : [Medium/nemo](https://medium.com/@samfarahzad/nvidia-nemo-neural-modules-and-models-for-conversational-ai-ea041e4cd4)\
NeMo analytics india magazine article link : [Analytics india magazine](https://analyticsindiamag.com/nvidia-just-gave-a-pytorch-based-conversational-ai-model-for-free/)

## Getting sound 

---

For recording sound and playing it back we have many opions as listed in this Real python post : [Real python playing and recording sound](https://realpython.com/playing-and-recording-sound-python/)

Here i am using **sounddevice** python module , because it is not as complex as pyaudio and at the same time provide enough funtionalities for recording and playing back wav file.
