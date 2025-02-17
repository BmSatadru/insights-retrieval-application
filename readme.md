# CFO Buddy

CFO Buddy is a web application designed to assist Chief Financial Officers and financial professionals with various tasks and analyses.

## Project Overview

This project aims to provide a comprehensive tool for financial management, leveraging modern web technologies and cloud deployment.

## Features

- Financial data analysis
- Reporting tools
- API integration for real-time financial information
- User-friendly interface for CFOs and financial teams

## Technology Stack

- Backend: Python
- Frontend: HTML, CSS, JavaScript
- Deployment: Vercel

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/BmSatadru/cfo-buddy-vercel.git
   cd cfo-buddy-vercel
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables (if any) as specified in `config.py`.

## Usage

To run the application locally:

1. Start the Python server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` (or the port specified in your configuration).

## Project Structure

- `app.py`: Main application file
- `config.py`: Configuration settings
- `api/`: API-related functionality
- `static/`: CSS, JavaScript, and other static assets
- `templates/`: HTML templates
- `services/`: Various service modules

## Deployment

This project is configured for deployment on Vercel. The `vercel.json` file in the repository root contains the necessary configuration for deployment.
