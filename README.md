# A brief introduction to Nvidia free NeMo extension pack  

---

Conversational AI mainly has 3 parts

1. automatic speech recognition (ASR)
2. natural language processing (NLP)
3. and speech synthesis(TTS)

NVIDIA NeMo (**Ne**ural **mo**dules) helps to quickly build , train and fine-tune conversational AI models.
Common collections found on NeMo are as follows 

1. [NeMo speech collection (nemo_asr)](https://nvda.ws/36bgfEd)
2. [Nemo NLP collection(nemo_nlp)](https://nvda.ws/36eHEFh)
3. [Nemo speech synthesis(nemo_tts)](https://nvda.ws/3396Tqr)

## Installation

---

nemo is available as docker container and its the easiest way \
more information is linked here [Nvidia/nemo in github](https://github.com/NVIDIA/NeMo)\
pytorch medium article about NeMo and sample codes : [Medium/nemo](https://medium.com/@samfarahzad/nvidia-nemo-neural-modules-and-models-for-conversational-ai-ea041e4cd4)\
NeMo analytics india magazine article link : [Analytics india magazine](https://analyticsindiamag.com/nvidia-just-gave-a-pytorch-based-conversational-ai-model-for-free/)

NeMo Docker contatiner [NeMo's container](https://ngc.nvidia.com/catalog/containers/nvidia:nemo)

## Getting sound

---

For recording sound and playing it back we have many options as listed in this Real python post : [Real python playing and recording sound](https://realpython.com/playing-and-recording-sound-python/)

Here i am using **sounddevice** python module , because it is not as complex as pyaudio and at the same time provide enough functionalities for recording and playing back wav file.

## My implementation

---

For simplicity i chose to go with docker . For alpha projects docker is the best option as it inherently provides with the required versions of all modules and we don't want to hunt for it . It saves a lot of time .

But one of the main drawback of a windows implementation is the lack of GPU support .But luckily windows provided a new solution know as WSL 2 (WIndows subsystem for linux). This allows/
for using docker for linux thus allowing for using gpu in our applications .

WSL 2 helps in running linux runtime without using virtual machine thus helping to implement the required GPU support for machine learning applications.

WIndows 10 WSL 2 installation guide [windows subsystem for linux on windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

Nvidia coda on WSL [CUDA on WSL guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)