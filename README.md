#   get-papers-list

##   Overview

This project is designed to identify and filter research papers from PubMed search results, focusing on those with industry affiliations. It retrieves scientific articles based on a user-specified query, extracts metadata, and classifies papers based on author affiliations. The primary goal is to provide a tool that can separate research originating from or involving pharmaceutical and biotech companies from purely academic publications.

##   Features

*  Fetches research papers from PubMed using the Entrez API.
*   Supports PubMed's full query syntax for flexible searches.
*   Extracts key metadata:
    * PubMed ID 
    * Title.
    * Publication Date 
    * Author Names.
    * Author Affiliations.
    * Corresponding Author Email.
*   Identifies papers with at least one author affiliated with a pharmaceutical or biotech company using a heuristic approach.
*   Saves the filtered results to a structured CSV file.
*   Provides a command-line interface with options for:
    * Specifying the query.
    * Displaying help/usage instructions.
    * Enabling debug mode. 
    * Saving output to a file or console. 

##   How It Works

1.  **Fetch Papers:** The script queries the PubMed database via the Entrez API using a user-provided query and retrieves relevant article IDs.
2.  **Extract Metadata:** Detailed information, including title, authors, affiliations, and publication date, is fetched for each retrieved paper ID.
3.  **Filter Papers:** Author affiliations are analyzed to identify papers with authors from pharmaceutical or biotech companies. This involves a heuristic-based approach using keywords.
4.  **Save Results:** The filtered data is stored in a CSV file (or printed to the console) with the following columns:
    * PubmedID: Unique identifier for the paper.
    * Title: Title of the paper. 
    * Publication Date: Date the paper was published. [cite: 5]
    * Non-academic Author(s): Names of authors affiliated with non-academic institutions. 
    * Company Affiliation(s): Names of pharmaceutical/biotech companies.
    * Corresponding Author Email: Email address of the corresponding author.

##   Code Organization

The project is structured as follows:

* `get_papers_module/`: Contains the core logic of the application.
    * `__init__.py`: Initializes the module and simplifies imports.
    * `paper_fetcher.py`: Handles fetching data from the PubMed API.
    * `paper_processor.py`: Implements the filtering logic and data extraction.
    * `output_formatter.py`:  Formats the output into a CSV string.
    * `utils.py`: Provides utility functions (e.g., date formatting).
* `get_papers_cli.py`: Provides the command-line interface. 
* `tests/`: Contains unit tests.
* `poetry.toml`: Manages dependencies and project configuration. 
* `README.md`: Documentation for the project.

##   Installation and Execution

1.  **Prerequisites:** Python 3.8 or later.
2.  **Install Poetry:** Follow the instructions on the [official Poetry website](https://python-poetry.org/) to install Poetry. 
3.  **Clone the repository:** Clone the Git repository containing the project code (hosted on GitHub). 
4.  **Install dependencies:** Navigate to the project directory in your terminal and run:

    ```bash
    poetry install
    ```

    This command will create a virtual environment and install all project dependencies.

    ```bash
    poetry run get-papers-list "<your_pubmed_query>" [-f <output_filename.csv>] [-d] [-h]
    ```

    * `<your_pubmed_query>`: The PubMed query string (required). [cite: 7, 29]
    * `-f <output_filename.csv>` or `--file <output_filename.csv>`:  Specify the filename for the CSV output. If omitted, output is printed to the console.
    * `-d` or `--debug`:  Enable debug mode for verbose output.
    * `-h` or `--help`: Display help message and exit.

##   Heuristic for Identifying Non-Academic Authors

The program employs a heuristic approach to identify non-academic authors based on keywords found in the author's affiliation string.

The following keywords are used:

* pharmaceutical, pharma 
* biotech(nology) 
* corp(oration) 
* ltd, limited
* inc(orporated)
* company
* industry 
* labs? 

**Important Note:** This method is heuristic and may not be entirely accurate.

##   Tools Used

* **PubMed API:** The primary source for fetching research paper data.
* **Biopython:** A Python library used to interact with the Entrez API.
* **Poetry:** A tool for dependency management and packaging. ([https://python-poetry.org/](https://python-poetry.org/))
* **Python's `csv` module:** For handling CSV file operations.
* **Python's `argparse` module:** For parsing command-line arguments.
* **Python's `unittest` and `unittest.mock`:** For unit testing.
* **LLM (This Gemini model):** Used to assist in code generation, documentation, and problem-solving. 

##   Evaluation Criteria

The program will be evaluated based on the following criteria: 

* **Functional Requirements:**
    * Adherence to the problem statement.
    * Correctness of fetching and filtering.
* **Non-functional Requirements:**
    * Typed Python:  Use of type hints.
    * Performance: Efficiency of the program.
    * Readability: Code clarity and maintainability.
    * Organization: Modular design and code structure. 
    * Robustness: Error handling and resilience. 

##   Bonus Features

* The program is separated into a module and a command-line program. 
* (Optional) The module can be published to test-pypi.

##   Future Improvements

The following enhancements could be considered for future development:

* Improve the accuracy of affiliation filtering, potentially using more sophisticated techniques like Named Entity Recognition or external databases.
* Implement asynchronous API calls to improve performance.
* Add more robust error handling and logging.
* Incorporate data validation to ensure data integrity.
* Expand the functionality with a web-based interface.
* Explore alternative data storage and retrieval methods.

##   License

📜Rajnish Chaube – Free to use and modify
