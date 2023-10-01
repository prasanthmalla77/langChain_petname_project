from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()


def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7)
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="""What is a cool name for a pet of type {animal_type} and
        color {pet_color}?. suggest me 5 intersting names"""
    )
    # return llm.generate_one(prompt="What is your pet's name?").get("text")
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    response = name_chain({"animal_type": animal_type, "pet_color": pet_color})
    return response


if __name__ == "__main__":
    print(generate_pet_name("cow", "black"))
