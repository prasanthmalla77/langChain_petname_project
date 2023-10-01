from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()


def generate_pet_name(role, months):
    llm = ChatOpenAI(model_name="gpt-4-0613", temperature=0)
    prompt_template_name = PromptTemplate(
        input_variables=['role', 'months'],
        template="""give me the preparation plan to become
        a {role} in {months} months"""
    )
    # return llm.generate_one(prompt="What is your pet's name?").get("text")
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    response = name_chain({"role": role, "months": months})
    return response


if __name__ == "__main__":
    print(generate_pet_name("cow", "black"))
