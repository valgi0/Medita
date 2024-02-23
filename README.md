# Medita
MEDical ITAlian Language Model


## Set up

### Install mergekit

`git clone https://github.com/cg123/mergekit.git`
`cd mergekit`
`pip install -e .`

### Install llama.cpp

this is required to create guff file

`git clone https://github.com/ggerganov/llama.cpp.git`
`cd llama.cpp`
`make`
`pip install -r requirements.txt`

### Merge the model
`cd src`
`python merge_model.py`

### Convert the model to guff
`cd llama.cpp`
`python convert.py ../src/medita-model/ --outfile ../src/medit-model.fp16.bin`
``

### Resources:

Colab with llama.cpp example: https://colab.research.google.com/github/mlabonne/llm-course/blob/main/Quantize_Llama_2_models_using_GGUF_and_llama_cpp.ipynb
llama.cpp github: https://github.com/ggerganov/llama.cpp/tree/master/examples