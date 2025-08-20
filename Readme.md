# Domain Classification Challenge

This project focuses on domain classification using machine learning techniques. Two models were implemented: **Random Forest** and **XGBoost**. After evaluation, **XGBoost** demonstrated superior performance.

## Features.

- **Domain Classification**: Classifies input data into predefined categories.
- **Model Comparison**: Implements both Random Forest and XGBoost for benchmarking.
- **API Backend**: Provides a FastAPI-based backend for serving predictions.

## Tech Stack

- Python
- scikit-learn (Random Forest)
- XGBoost
- FastAPI

## Usage

1. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```

3. **Make predictions:**  
    Send POST requests to the API endpoint with your data.

## Results

- **XGBoost** outperformed Random Forest in accuracy and speed.

## License

MIT License
