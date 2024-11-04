# import streamlit as st
# from langchain_community.document_loaders import WebBaseLoader

# from chains import Chain
# from portfolio import Portfolio
# from utils import clean_text

# def create_streamlit_app(llm, portfolio, clean_text):
#     st.title("📧 Rishi's Mail Generator")

#     language_options = ["English","Hindi", "Spanish", "French", "German"]
#     selected_language = st.multiselect("Select Language:", language_options)


#     url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-33460")
#     submit_button = st.button("Submit")

#     if submit_button:
#         try:
#             loader = WebBaseLoader([url_input])
#             data = clean_text(loader.load().pop().page_content)
#             portfolio.load_portfolio()
#             jobs = llm.extract_jobs(data)
#             for job in jobs:
#                 skills = job.get('skills', [])
#                 links = portfolio.query_links(skills)

                
#                 for language in selected_languages:
#                     email = llm.write_mail(job, links, language=language)  # Pass the selected language
#                     st.subheader(f"Email in {language}:")
#                     st.code(email, language='markdown')
#                 # email = llm.write_mail(job, links)
#                 # st.code(email, language='markdown')
#         except Exception as e:
#             st.error(f"An Error Occurred: {e}")


# if __name__ == "__main__":
#     chain = Chain()
#     portfolio = Portfolio()
#     st.set_page_config(layout="wide", page_title="Rishi's Email Generator", page_icon="📧")
#     create_streamlit_app(chain, portfolio, clean_text)

# import streamlit as st
# from langchain_community.document_loaders import WebBaseLoader

# from chains import Chain
# from portfolio import Portfolio
# from utils import clean_text

# def create_streamlit_app(llm, portfolio, clean_text):
#     st.title("📧 Cold Mail Generator")
    
#     # Language selection multi-select
#     language_options = ["English","Gujarati", "Hindi","Spanish", "French", "German"]
#     selected_languages = st.multiselect("Select Languages:", language_options)
    
#     url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-33460")
#     submit_button = st.button("Submit")

#     if submit_button:
#         # Check if any language is selected
#         if not selected_languages:
#             st.warning("Please select at least one language.")
#             return  # Exit early if no languages are selected

#         try:
#             # Load the data from the URL
#             loader = WebBaseLoader([url_input])
#             data = clean_text(loader.load().pop().page_content)
#             portfolio.load_portfolio()
#             jobs = llm.extract_jobs(data)
            
#             # Generate email for each selected language
#             for job in jobs:
#                 skills = job.get('skills', [])
#                 links = portfolio.query_links(skills)
                
#                 for language in selected_languages:
#                     email = llm.write_mail(job, links, language=language)  # Pass the selected language
#                     st.subheader(f"Email in {language}:")
#                     st.code(email, language='markdown')
                    
#         except Exception as e:
#             st.error(f"An Error Occurred: {e}")

# if __name__ == "__main__":
#     chain = Chain()
#     portfolio = Portfolio()
#     st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
#     create_streamlit_app(chain, portfolio, clean_text)

# import streamlit as st
# from langchain_community.document_loaders import WebBaseLoader

# from chains import Chain
# from portfolio import Portfolio
# from utils import clean_text

# def create_streamlit_app(llm, portfolio, clean_text):
#     st.title("📧 Cold Mail Generator")
    
#     # Language selection multi-select
#     language_options = ["English", "Gujarati", "Hindi", "Spanish", "French", "German"]
#     selected_languages = st.multiselect("Select Languages:", language_options)
    
#     # Allow for multiple URLs
#     url_input = st.text_area("Enter URLs (one per line):", value="https://jobs.nike.com/job/R-33460")
#     submit_button = st.button("Submit")

#     if submit_button:
#         # Check if any language is selected
#         if not selected_languages:
#             st.warning("Please select at least one language.")
#             return  # Exit early if no languages are selected

#         # Split input into individual URLs
#         urls = [url.strip() for url in url_input.splitlines() if url.strip()]
#         if not urls:
#             st.warning("Please enter at least one valid URL.")
#             return

#         for url in urls:
#             try:
#                 # Load the data from the URL
#                 loader = WebBaseLoader([url])
#                 data = clean_text(loader.load().pop().page_content)
#                 portfolio.load_portfolio()
#                 jobs = llm.extract_jobs(data)

#                 if not jobs:
#                     st.warning(f"No jobs found at {url}.")
#                     continue  # Skip to the next URL if no jobs are found

#                 # Generate email for each selected language
#                 for job in jobs:
#                     skills = job.get('skills', [])
#                     links = portfolio.query_links(skills)
                    
#                     for language in selected_languages:
#                         email = llm.write_mail(job, links, language=language)  # Pass the selected language
#                         st.subheader(f"Email for job at {url} in {language}:")
#                         st.code(email, language='markdown')
                        
#             except Exception as e:
#                 st.error(f"An error occurred while processing {url}: {e}")

# if __name__ == "__main__":
#     chain = Chain()
#     portfolio = Portfolio()
#     st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
#     create_streamlit_app(chain, portfolio, clean_text)



# import streamlit as st
# from langchain_community.document_loaders import WebBaseLoader
# from chains import Chain
# from portfolio import Portfolio
# from utils import clean_text

# def create_streamlit_app(llm, portfolio, clean_text):
#     st.title("📧 Rishi's Mail Generator")
    
#     # Language selection multi-select
#     language_options = ["English", "Gujarati", "Hindi", "Spanish", "French", "German"]
#     selected_languages = st.multiselect("Select Languages:", language_options)
    
#     # Allow for multiple URLs
#     url_input = st.text_area("Enter URLs (one per line):", value="https://jobs.nike.com/job/R-33460")
    
#     # Allow users to upload their resume
#     resume_file = st.file_uploader("Upload your resume (PDF format):", type=["pdf"])
    
#     submit_button = st.button("Submit")

#     if submit_button:
#         # Check if any language is selected
#         if not selected_languages:
#             st.warning("Please select at least one language.")
#             return  # Exit early if no languages are selected

#         # Split input into individual URLs
#         urls = [url.strip() for url in url_input.splitlines() if url.strip()]
#         if not urls:
#             st.warning("Please enter at least one valid URL.")
#             return

#         for url in urls:
#             try:
#                 # Load the data from the URL
#                 loader = WebBaseLoader([url])
#                 data = clean_text(loader.load().pop().page_content)
#                 portfolio.load_portfolio()
#                 jobs = llm.extract_jobs(data)

#                 if not jobs:
#                     st.warning(f"No jobs found at {url}.")
#                     continue  # Skip to the next URL if no jobs are found

#                 # Generate email for each selected language
#                 for job in jobs:
#                     skills = job.get('skills', [])
#                     links = portfolio.query_links(skills)
                    
#                     for language in selected_languages:
#                         email = llm.write_mail(job, links, language=language)  # Pass the selected language
                        
#                         # Mention the resume in the email
#                         if resume_file is not None:
#                             email += f"\n\nPlease find my resume attached: {resume_file.name}"

#                         st.subheader(f"Email for job at {url} in {language}:")
#                         st.code(email, language='markdown')
                        
#             except Exception as e:
#                 st.error(f"An error occurred while processing {url}: {e}")

# if __name__ == "__main__":
#     chain = Chain()
#     portfolio = Portfolio()
#     st.set_page_config(layout="wide", page_title="Rishi's Email Generator", page_icon="📧")
#     create_streamlit_app(chain, portfolio, clean_text)

import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Rishi's Mail Generator")
    
    # Language selection multi-select
    language_options = ["English", "Gujarati", "Hindi", "Spanish", "French", "German"]
    selected_languages = st.multiselect("Select Languages:", language_options)
    
    # Allow for multiple URLs
    url_input = st.text_area("Enter URLs (one per line):", value="https://jobs.nike.com/job/R-33460")
    
    # File uploader for resume
    resume_file = st.file_uploader("Upload your Resume:", type=["pdf", "doc", "docx"])

    submit_button = st.button("Submit")

    if submit_button:
        # Check if any language is selected
        if not selected_languages:
            st.warning("Please select at least one language.")
            return  # Exit early if no languages are selected

        # Split input into individual URLs
        urls = [url.strip() for url in url_input.splitlines() if url.strip()]
        if not urls:
            st.warning("Please enter at least one valid URL.")
            return

        if resume_file is None:
            st.warning("Please upload your resume.")
            return

        for url in urls:
            try:
                # Load the data from the URL
                loader = WebBaseLoader([url])
                data = clean_text(loader.load().pop().page_content)
                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)

                if not jobs:
                    st.warning(f"No jobs found at {url}.")
                    continue  # Skip to the next URL if no jobs are found

                # Generate email for each selected language
                for job in jobs:
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    
                    for language in selected_languages:
                        email = llm.write_mail(job, links, language=language, resume = resume_file )  # Pass the selected language
                        # st.subheader(f"Email for job at {url} in {language}:")
                        st.code(email, language='markdown')
                        
            except Exception as e:
                st.error(f"An error occurred while processing {url}: {e}")

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Rishi's Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)


