import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    # def write_mail(self, job, links,language):
    #     language_instruction = f"Write an email in {language}."
    #     prompt_email = PromptTemplate.from_template(
    #         """
    #         ### JOB DESCRIPTION:
    #         {job_description}

    #         ### INSTRUCTION:
    #         You are Mohan, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
    #         the seamless integration of business processes through automated tools. 
    #         Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
    #         process optimization, cost reduction, and heightened overall efficiency. 
    #         Your job is to {language_instruction} to the client regarding the job mentioned above describing the capability of AtliQ 
    #         in fulfilling their needs.
    #         Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
    #         Remember you are Mohan, BDE at AtliQ. 
    #         Do not provide a preamble.
    #         ### EMAIL (NO PREAMBLE):

    #         """
    #     )
    #     chain_email = prompt_email | self.llm
    #     res = chain_email.invoke({"job_description": str(job), "link_list": links})
    #     return res.content


    # def write_mail(self, job, links, language):
    # # Use the language parameter to instruct the model to write the email in the specified language
    #     language_instruction = f"Write an email in {language}."

    # # Directly include language_instruction in the prompt as a string, not as a variable
    #     prompt_email = PromptTemplate.from_template(
    #         f"""
    #         ### JOB DESCRIPTION:
    #         {{job_description}}

    #         ### INSTRUCTION:
    #         You are Mohan, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
    #         the seamless integration of business processes through automated tools.
    #         Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability,
    #         process optimization, cost reduction, and heightened overall efficiency.
    #         Your job is to {language_instruction} to the client regarding the job mentioned above describing the capability of AtliQ
    #         in fulfilling their needs.
    #         Also, add the most relevant ones from the following links to showcase AtliQ's portfolio: {{link_list}}
    #         Remember you are Mohan, BDE at AtliQ.
    #         Do not provide a preamble.
    #         ### EMAIL (NO PREAMBLE):

    #         """
    #     )
    #     chain_email = prompt_email | self.llm
    #     res = chain_email.invoke({"job_description": str(job), "link_list": links})
    #     return res.content

    def write_mail(self, job, links, language, resume):
        # Use the language parameter to instruct the model to write the email in the specified language
        language_instruction = f"Write an email in {language}."

        # Include the resume in the prompt
        prompt_email = PromptTemplate.from_template(
            f"""
            ### JOB DESCRIPTION:
            {{job_description}}

            ### INSTRUCTION:
            You are Mohan, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools.
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability,
            process optimization, cost reduction, and heightened overall efficiency.
            Your job is to {language_instruction} to the client regarding the job mentioned above describing the capability of AtliQ
            in fulfilling their needs.
            Also, add the most relevant ones from the following links to showcase AtliQ's portfolio: {{link_list}}
            Additionally, include my resume: {resume}
            Remember you are Mohan, BDE at AtliQ.
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))