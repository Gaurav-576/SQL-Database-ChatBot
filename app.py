import os
import textwrap
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from langchain.chains import create_sql_query_chain
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase

db_host=st.secrets["database"]["db_host"]
db_user=st.secrets["database"]["db_user"]
db_password=st.secrets["database"]["db_password"]
db_name=st.secrets["database"]["db_name"]
api_key=st.secrets["gemini"]["GEMINI_API_KEY"]

engine=create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
db=SQLDatabase(engine)

llm=GoogleGenerativeAI(model="gemini-pro",google_api_key=api_key)
sql_chain=create_sql_query_chain(llm,db)

def chain(input_text):
    try:
        query=sql_chain.invoke({"question":input_text})
        clean_query=query.strip("```sql\n").strip("\n```")
        result=db.run(clean_query)
        return clean_query,result
    except ProgrammingError as e:
        return str(e)
    
st.set_page_config(page_title="SQL Query Generator", page_icon=":robot:")
st.title("🔍 SQL Query Generator")
st.markdown(
    """
    **Welcome to the SQL Query Generator!**  
    Easily convert your questions about your database into executable SQL queries.
    _Powered by Google-Gemini-AI and LangChain.
    """
)
st.markdown("---")
st.markdown("### ✏️ Ask Your Question")
question=st.text_input(
    "Enter your question here:",
    placeholder="E.g., Show me all employees who joined after 2020...",
)
def wrap_text(text,width=35):
    return '\n'.join(textwrap.wrap(text,width))
if st.button("💡 Generate SQL Query"):
    if question:
        with st.spinner("Generating SQL Query... Please wait!"):
            sql_query, db_response = chain(question)
            if sql_query:
                st.success("✅ SQL Query Generated!")
                wrapped_sql_query=wrap_text(sql_query,width=35)
                col1,col2=st.columns([1,1])
                # Left column: SQL query
                with col1:
                    st.markdown("### 🧾 Generated SQL Query")
                    st.code(wrapped_sql_query,language="sql")
                # Right column: Database response
                with col2:
                    if db_response is not None:
                        st.markdown("### 📊 Database Response")
                        st.markdown(db_response)
                    else:
                        st.markdown("### 📊 Database Response")
                        st.error("⚠️ No result obtained from the database. Please re-check your query.")
            else:
                st.error("⚠️ Failed to generate SQL query. Please re-check your question.")
    else:
        st.warning("⚠️ Please enter a question to generate the SQL query.")

st.markdown("---")
st.markdown(
    """
    **Need Help?**  
    For any issues, feel free to raise an issue at [Github](https://github.com/Gaurav-576/QueryBot).
    _Happy Querying!_
    """
)