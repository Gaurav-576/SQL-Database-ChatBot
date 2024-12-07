# SQL Query Generator using LangChain and Google-Gemini-Pro

## Project Overview

This project is a web-based application built using **Google-Gemini-Pro** and **LangChain** to generate SQL queries based on user input and retrieve results from a connected database. The system uses Google's **Gemini-Pro-AI** model via **LangChain** to generate SQL queries dynamically based on natural language questions. The user can also view the results of the SQL query from the database in a user-friendly interface.

### Key Features
- **Natural Language to SQL**: Convert user queries (in natural language) into valid SQL queries.
- **Database Connectivity**: Execute the generated SQL queries on a connected MySQL database.
- **Results Display**: Show the database query results in a responsive and interactive format.
- **Responsive Design**: The interface is designed to be user-friendly and responsive, making it easy for users to interact with the application.
- **Real-Time Query Execution**: SQL queries are executed in real-time and the results are displayed immediately after the query is processed.

---

## How it Works

1. **Input a Question**: The user enters a question related to the database in the input box. 
   - Example: "What are the top-selling products?"
   
2. **Generate SQL Query**: Upon clicking the "Generate SQL Query" button, the system uses **LangChain** with Google's **Generative AI** model to convert the natural language query into a valid SQL query.
   cr
   
4. **Display Results**: The results from the database are shown on the right side of the interface in a structured and readable format.

---

## Installation

### Prerequisites
- Python 3.x
- A MySQL Database (You can use a local or remote database)

### Install Required Libraries
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sql-query-generator.git
   cd sql-query-generator
   ```

2. Create and activate a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
   ```

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Set up the `.env` File
Create a `.env` file in the root of the project and add the following environment variables to connect to your MySQL database:

```ini
db_user=your_db_user
db_password=your_db_password
db_host=your_db_host
db_name=your_db_name
GOOGLE_API_KEY=your_google_api_key
```

- **db_user**: Your MySQL username.
- **db_password**: Your MySQL password.
- **db_host**: The host address of your MySQL database (e.g., localhost).
- **db_name**: The name of the database you want to query.
- **GOOGLE_API_KEY**: Your API key for Google Generative AI.

---

## Running the Application

To run the application, use the following command:

```bash
streamlit run app.py
```

This will start the Streamlit server and you can access the web interface in your browser at `http://localhost:8501`.

---

## Project Structure

- **app.py**: The main Python file that runs the Streamlit application.
- **.env**: A file to store environment variables like database credentials and Google API key.
- **requirements.txt**: List of all the required dependencies for the project.
- **README.md**: The readme file you're currently reading.

---

## Technologies Used

- **Streamlit**: A framework for building interactive, web-based applications using Python.
- **LangChain**: A library that simplifies the creation of LLM-powered applications like this one. It's used to convert natural language into SQL queries.
- **Google Generative AI**: Google's generative AI model used to create SQL queries from natural language input.
- **SQLAlchemy**: A Python library for interacting with relational databases like MySQL.
- **MySQL**: The database system where the queries are executed.
- **Pandas**: A data manipulation library (used to handle query results).
- **dotenv**: A library to manage environment variables from a `.env` file.

---

## Usage

1. **Enter a Question**: Type a question related to your database in the input box. Example questions could be:
   - "What is the total sales for last year?"
   - "List the most popular categories of products."

2. **Generate SQL Query**: Press the "Generate SQL Query" button to see the SQL query generated from your question.

3. **Fetch Results**: After the query is generated, click the "Fetch Results" button to retrieve the results from the database. The results will be displayed on the right side of the interface.

4. **View Query and Results**: The SQL query and its results are displayed in two separate columns for easy comparison.

---

## Known Issues and Limitations
- The app currently only supports MySQL as the database engine.
- The generated SQL queries are basic and may need further optimization depending on the complexity of the input question.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or issues, feel free to reach out at [your-email@example.com](mailto:your-email@example.com).
