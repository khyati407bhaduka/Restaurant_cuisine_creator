import os
import torch
from transformers import pipeline
from secret_key import huggingface_key
from langchain.llms import HuggingFacePipeline
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Create Hugging Face text-generation pipeline
os.environ['HF_API_KEY'] = huggingface_key

hf_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device=0 if torch.cuda.is_available() else -1,
    token=os.environ['HF_API_KEY'],
    max_new_tokens=30,
    do_sample=True,
    temperature=1
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)


def genarte_restaurant(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food, suggest a fancy name for that")
    restaurant_name = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
    prompt_template_menu = PromptTemplate(
        input_variables=['restaurant_name'],
        template="List 10 authentic menu items for a restaurant named {restaurant_name}. Separate them by commas.")
    restaurant_menu = LLMChain(llm=llm, prompt=prompt_template_menu, output_key="restaurant_menu")
    from langchain.chains import SequentialChain
    chain = SequentialChain(chains=[restaurant_name, restaurant_menu],
                            input_variables=['cuisine'],
                            output_variables=['restaurant_name', 'restaurant_menu'])
    response = chain({'cuisine': cuisine})
    print("[DEBUG] Final Response:", response)
    return response

if __name__ == "__main__":
    result = genarte_restaurant("Indian")
    print("Restaurant Name:", result["resturant_name"])
    print("Menu Items:")
    for item in result["resturant_menu"].split(","):
        print("-", item.strip())
