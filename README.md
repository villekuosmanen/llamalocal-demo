# llamalocal-demo

Works on M1 MacBooks.

If using conda/mamba, create an env using such as `mamba create -n llamalocal-demo` and `conda activate`.

`pip install llama-cpp-python`

Download a model for example from [TheBloke @ HuggingFace](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML). Only GGML format models work, so FAIR AI downloads do not work for this use case.

Place your model into the `models` folder and import it in test.py.
