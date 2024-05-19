
# Citation Extractor

## Introduction
This is a Python program designed to extract citations from a paginated API response. It identifies whether the response for each pair of response-sources came from any of the sources and lists down the sources from which the response was formed.

## Features
- Fetches data from a paginated API endpoint.
- Identifies citations for each response from the provided sources.
- Utilizes Sentence Transformers for similarity computation.
- Presents the results through a user-friendly web UI.

## Technologies Used
- Python
- Flask (for the web UI)
- Requests (for making HTTP requests)
- Sentence Transformers (for computing similarity)
- HTML/CSS (for the UI layout)

## Setup and Execution
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/pratham123kr/beyond_chats.git
   ```
2. Navigate to the project directory.
   ```bash
   cd beyond_chats
   ```
3. Install the required dependencies.
   ```bash
   pip install Flask==2.1.0 requests==2.26.0 sentence-transformers==2.1.0

   ```
4. Run the Flask application.
   ```bash
   python app.py
   ```
5. Access the application in your web browser at `http://localhost:5000`.

## Usage
- Upon accessing the web interface, the program automatically fetches data from the provided API endpoint.
- It then computes citations for each response based on the provided sources.
- The results are displayed on the web page, showing the original response text along with the corresponding citations.

## Collaborators
- Add collaborator access to the GitHub repository for the user `Pankaj-Baranwal`.

