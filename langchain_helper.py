from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

load_dotenv()


def generate_pet_name(animal_type, pet_color):
    llm = ChatOpenAI(model_name="gpt-4-0613", temperature=0)
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="""What is a cool name for a pet of type {animal_type} and
        color {pet_color}?. suggest me 5 intersting names"""
    )
    # return llm.generate_one(prompt="What is your pet's name?").get("text")
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    response = name_chain({"animal_type": animal_type, "pet_color": pet_color})
    return response


def langchain_agent():
    llm = ChatOpenAI(model_name="gpt-4-0613", temperature=0)
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    agent = initialize_agent(
        tools, llm, AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    result = agent.run(
        """what is the  average age of  a dog? Multiply the age by 3"""
    )
    print(result)


if __name__ == "__main__":
    # print(generate_pet_name("cow", "black"))
    langchain_agent()
