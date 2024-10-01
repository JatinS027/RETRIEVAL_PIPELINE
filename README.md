# RETRIEVAL_PIPELINE

# Multi-Stage Text Retrieval Pipeline for Q&A Systems

## Overview

This project implements a multi-stage text retrieval pipeline designed for Question-Answering (Q&A) tasks. 
The pipeline utilizes embedding models to retrieve candidate passages and ranking models to reorder these passages based on relevance.
The goal is to enhance retrieval accuracy while maintaining efficiency.

## Achievements

- Achieved **NDCG@10 score of 1.0**, indicating perfect retrieval of relevant passages for the tested queries.

## Project Structure

my-retrieval-pipeline/ │ 
├── data/ # Data loading and preprocessing scripts │ └── dataset_loader.py │ ├── src/ # Source code for the retrieval pipeline │ ├── embedding_retrieval.py # Embedding model candidate retrieval │ ├── ranking_model.py # Reranking using ranking models │ └── evaluation.py # Evaluation scripts for NDCG@10 │ ├── requirements.txt # Dependencies for the project └── README.md # Project documentation

## Setup

To run this project, you need to install the required dependencies. You can do this using `pip`:
pip install -r requirements.txt

## Usage
Download Datasets: The project uses publicly available datasets from the BEIR benchmark (Natural Questions, HotpotQA, FiQA). Ensure you have access to these datasets.

## Run the Retrieval Pipeline:

Execute the embedding_retrieval.py script to perform candidate retrieval using embedding models.
Execute the ranking_model.py script to rerank the retrieved passages using ranking models.
Finally, use evaluation.py to evaluate the performance of the pipeline and obtain NDCG@10 scores.

## Results
The pipeline achieved an NDCG@10 score of 1.0 for the test queries, showcasing the effectiveness of the model combination and retrieval strategies.

