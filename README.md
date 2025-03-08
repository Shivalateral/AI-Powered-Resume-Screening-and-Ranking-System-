# AI-Powered Resume Screening and Ranking System

## Overview
This project aims to develop an AI-powered resume screening and ranking system using Natural Language Processing (NLP) and Machine Learning (ML) techniques. The system allows users to upload their resumes (in PDF or TXT format) and job descriptions (in TXT format). It then provides a ranking score based on how well the resume matches the job description.

## Features
- **Resume Upload**: Users can upload their resumes in PDF or TXT format.
- **Job Description Upload**: Users can submit job descriptions in TXT format.
- **AI Ranking**: The system uses NLP and ML models to evaluate and rank resumes based on relevance to the provided job description.
- **Frontend Interface**: Built with Streamlit for a user-friendly web interface.

## Technologies Used
- **Backend**: Python, Flask
- **Frontend**: Streamlit
- **NLP**: spaCy, NLTK, or other NLP libraries
- **Machine Learning**: Scikit-learn, TensorFlow, or PyTorch
- **Other Libraries**: pandas, numpy, matplotlib
- **Database**: SQLite (Optional for storing resumes and job descriptions)

 AI-Powered Resume Screening and Ranking System/
│
├── backend/                   
│   ├── app.py               # Flask API to handle user requests and resume processing
│   ├── model.py             # ML Model for resume ranking based on job description
│   ├── nlp_processing.py    # NLP-based feature extraction and text processing
│   ├── utils.py             # Helper functions for data processing and model usage
│   ├── requirements.txt     # List of Python dependencies for the backend
│
├── frontend/                 
│   ├── src/                 
│   │   ├── components/      # UI components for the frontend (e.g., file upload forms)
│   │   ├── pages/           # Streamlit app pages (main user interface)
│   │   ├── App.js           # Main app entry point (for frontend logic)
│   │   ├── index.js         # Initial file for frontend routing and setup
│   ├── package.json         # Frontend dependencies for the project (Streamlit)
│
├── models/                  # Folder containing trained ML models for resume ranking
│   ├── ranking_model.pkl    # Pickled model for ranking resumes based on the job description
│
├── dataset/                 # Folder to store sample resumes and job descriptions for testing
│   ├── resumes/             # Sample resume files (PDF/TXT)
│   ├── job_descriptions/    # Sample job description files (TXT)
│
├── README.md                # Project documentation and instructions
└── .gitignore               # Git ignore file for unnecessary files

#!/bin/bash

# Clone the repository (if not done already)
git clone <repository_url>
cd AI-Powered-Resume-Screening-and-Ranking-System

# Set up backend (Python/Flask)
echo "Setting up Backend..."

# Navigate to backend directory
cd backend

# (Optional) Set up a virtual environment
echo "Setting up virtual environment..."
python3 -m venv venv

# Activate virtual environment (Mac/Linux)
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Run the Flask backend server
echo "Starting Flask server..."
python app.py &

# Go back to the main project directory
cd ..

# Set up frontend (Streamlit)
echo "Setting up Frontend..."

# Navigate to frontend directory
cd frontend

# Install frontend dependencies
echo "Installing frontend dependencies..."
npm install

# Run the Streamlit app
echo "Starting Streamlit app..."
streamlit run src/App.py

# All services are now up and running
echo "Backend and Frontend are set up and running!"
How to Use:


Save the above script into a file, e.g., setup.sh.
Open a terminal and make the script executable:
 
chmod +x setup.sh
 
 
./setup.sh


