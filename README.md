# MLTE


This is finetuned on LLaMA2 7B Chat model. Get details at this [Hugging face](https://huggingface.co/sainv/MLTE_llama2_multilingual_T2I_prompt_gen).
when input prompt is in non-english language many Text-to-Image generation models fail to generate relevent images.
To solve this we finetuned Llama2 model in Indian languages (telugu and hindi).
Our target was to achieve 4 things.To handle
1. Multilingual prompts
2. Mispelled prompts
3. Enhancing insufficient prompt
4. To summarize and keyword extraction for lengthy prompts


## Model Details

### Model Description

MLTE - Multilingual Text Enhancer, a text enhancement model developed primarily to enrich input text for
text-to-image generation models. Existing text encoders in image generation models often have limited reach.
The quality of image generation depends on the prompt. If the prompt includes misspelled words, the encoder
will create an irrelevant image. Most encoders are primarily English-based. MLTE effectively addresses 
multilingual prompts, misspelled words, overly verbose prompts, and creatively enhances the prompt to get 
improved results. MLTE utilizes advanced natural language processing techniques to connect raw text input 
with the generation of highly accurate images. MLTE is based on LLaMA2 it has ability to handle numerous 
languages enables for simple incorporation of content from diverse linguistic origins. Additionally, its 
spell checking and correction functions ensure the quality and coherence of the prompt. Moreover, MLTE's 
scene and text augmentation features strengthen the visual richness and coherence of generated photos, 
enhancing their overall quality and realism. Its summarizing capability condenses large paragraphs into 
concise yet helpful summaries, assisting the image creation process by delivering more focused input. 
MLTE can be used with any text to image generating models.


![Architecture](https://github.com/sai1027/MLTE/blob/main/img/Architecture.png?raw=true)





### Model Sources

<!-- Provide the basic links for the model. -->

- **Hugging Face Repository:**[Hugging face](https://huggingface.co/sainv/MLTE_llama2_multilingual_T2I_prompt_gen)
- **Paper :** under review
- **Demo :**    


### Direct Use

Do not give any descriptions like "Act as this .."
Just give prompt.

### Alert

As of 31/3/2024 it is giving better results for Hindi language and for Telugu it is under performing. 
We are trying to improve it.
![Wrong translation](https://github.com/sai1027/MLTE/blob/main/img/Sample%20Error%20.png?raw=true)

<!--

## How to Get Started with the Model

Use the code below to get started with the model.

[More Information Needed]

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->



### Evaluation

![Evaluation](https://github.com/sai1027/MLTE/blob/main/img/Evaluation%20method%20.png?raw=true)


![Performance](https://github.com/sai1027/MLTE/blob/main/img/Performance%20Table.png?raw=true)


### Results

![output 1 ](https://github.com/sai1027/MLTE/blob/main/img/Output%20sample%201.png?raw=true)
![output 2 ](https://github.com/sai1027/MLTE/blob/main/img/Output%20sample%202.png?raw=true)
