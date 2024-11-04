# import streamlit as st

# st.title("Cold Mail Generator")
# url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-33460")
# submit_button = st.button("Submit")

# if submit_button:
#     st.code ("hello, i am Rishi", language = 'markdown')


# import langchain_community.document_loaders
# print(dir(langchain_community.document_loaders))

# Replace this line:
# from langchain.document_loaders import WebBaseLoader

# With this line:
# from langchain_community.document_loaders import WebBaseLoader

# print(WebBaseLoader)
# import os
# from langchain_community.document_loaders import WebBaseLoader

# # Set the USER_AGENT environment variable
# os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# # Example usage of WebBaseLoader
# url = "https://example.com"
# loader = WebBaseLoader(url)
# documents = loader.load()

# # Print the loaded documents
# for doc in documents:
#     print(doc.page_content)

import os
from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup

# Set the USER_AGENT environment variable
os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# Load the web page
url = "https://example.com"
loader = WebBaseLoader(url)
documents = loader.load()

# Assuming the loader returns the HTML content
for doc in documents:
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(doc.page_content, 'html.parser')
    
    # Extract and print the title of the page
    title = soup.title.string if soup.title else 'HI'
    print("Title of the page:", title)
    print(soup.prettify())
    # Extract and print all paragraph texts
    # paragraphs = soup.find_all('p')
    # for p in paragraphs:
    #     print(p.get_text())
    # Extract and print all headings (h1, h2, h3, etc.)
    for i in range(1, 4):  # For h1, h2, h3
        headings = soup.find_all(f'h{i}')
        for heading in headings:
            print(f"{heading.name}: {heading.get_text()}")

# Extract and print all paragraph texts
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print("Paragraph:", p.get_text())