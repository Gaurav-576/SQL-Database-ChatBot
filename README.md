### 🚀 Checkout the Live Project! 🌐

Experience the magic of **QueryBot** in action right now!
Check out the live version of the app by clicking the link below:

🔗 [Visit the Live Demo]()

👉 **Interact with the app** and see how it converts your natural language prompts into SQL queries and fetches real-time results from the database!

Feel free to test it out and let us know what you think. Don't forget to star the repository if you love the project! ⭐

---

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

3. **Database Response:** Once the SQL query is generated, the user can seamlessly view the results fetched directly from the MySQL database, displaying the relevant data in an easily digestible format. This feature enables users to interact with the database and retrieve the necessary information instantly.
   
4. **Display Results**: The results from the database are shown on the right side of the interface in a structured and readable format.

---

## Installation

### Prerequisites
- Python 3.9 or above.
- A MySQL Database (local or remote database)

### Install Required Libraries
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sql-query-generator.git
   ```
   ```bash
   cd sql-query-generator
   ```

2. Create and activate a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Set up the `.env` File
Create a `.env` file in the root of the project and add the following environment variables to connect to your MySQL database:

```ini
GEMINI_API_KEY=your_google_api_key
db_user=your_db_user
db_password=your_db_password
db_host=your_db_host
db_name=your_db_name
```

- **GOOGLE_API_KEY**: Make an account and get an API key from [Google AI Studio](https://aistudio.google.com/apikey)
- **db_user**: Your MySQL username.
- **db_password**: Your MySQL password.
- **db_host**: The host address of your MySQL database (e.g., localhost).
- **db_name**: The name of the database you want to query.

---

## Running the Application

To run the application, use the following command:

```bash
streamlit run app.py
```

This will start the Streamlit server and you can access the web interface in your browser at `http://localhost:8501`.

---

## Project Structure

```bash
/QueryBot
│
├── app.py                     # The main Python file that runs the Streamlit application.
├── .env                       # A file to store environment variables like database credentials and Google-Gemini-AI API key.
├── requirements.txt           # List of all the required dependencies for the project.
├── README.md                  # The readme file you're currently reading.
├── database/                  # Folder containing the database files
│   ├── retail_sales_db.sql    # SQL script for creating and populating the database.
└── retail_sales.ipynb         # Jupyter notebook containing queries, visualizations, and insights based on the database.
```

---

## Technologies Used

## Technologies Used

- **Streamlit**: Powers the user interface, enabling users to interact with the application in real-time through a web-based platform.
- **LangChain**: Simplifies the creation of LLM-powered applications, converting natural language inputs into SQL queries.
- **Google Generative AI**: Utilizes Google's Gemini Pro model to generate SQL queries from natural language inputs with high accuracy.
- **SQLAlchemy**: Serves as the ORM for database interaction, ensuring seamless communication with the MySQL database.
- **MySQL**: The relational database system where the generated queries are executed.
- **dotenv (python-dotenv)**: Manages sensitive environment variables stored in the `.env` file.
- **PyMySQL**: Provides the necessary driver for connecting Python with the MySQL database.
- **LangChain Experimental**: Adds experimental features to enhance LangChain's core capabilities.
- **LangChain Community**: Extends LangChain with community-driven utilities and tools.
- **LangChain Core**: Core functionalities for building applications powered by language models.
- **ipykernel**: Enables the Jupyter notebook environment for working with Python kernels, used in analyzing and querying the database.

---
## Usage

1. **Enter a Question**: Type a question related to your database in the input box. Example questions could be:
   - "What is the total sales for last year?"
   - "List the most popular categories of products."

2. **Generate SQL Query**: Press the "Generate SQL Query" button to see the SQL query generated from your question.

3. **Fetch Results**: After the query is generated, click the "Fetch Results" button to retrieve the results from the database. The results will be displayed on the right side of the interface.

4. **View Query and Results**: The SQL query and its results are displayed in two separate columns for easy comparison.

---

## Use Case

This application is ideal for users who need to interact with a MySQL database but are not familiar with SQL. Whether you're an analyst, business professional, or developer, you can easily generate SQL queries from natural language and retrieve results from the database without writing SQL manually. Some potential use cases include:
- **Business Analytics**: Generate and execute queries for sales data, customer insights, and inventory management.
- **Product Managers**: Retrieve data on product performance, customer preferences, and sales trends.
- **Data Analysts**: Quickly query databases without needing to be proficient in SQL syntax.

---

## Known Issues and Limitations
- The app currently only supports MySQL as the database engine.
- The generated SQL queries are basic and may need further optimization depending on the complexity of the input question.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or issues, feel free to open an issue at [QueryBot](https://github.com/Gaurav-576/QueryBot).

---

## Support and Contribution

If you find this project useful, please give it a ⭐️ by starring the repository. Contributions are always welcome, whether it's to improve features or fix bugs!
