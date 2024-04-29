# Credit Risk Analysis Project

Welcome to the Credit Risk Analysis project! This repository contains code and resources for analyzing credit risk using machine learning techniques and data visualization. The project demonstrates how to assess credit risk using logistic regression and provides insights into the data through various visualizations.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Data Description](#data-description)
- [Methods](#methods)
- [Results](#results)
- [License](#license)

## Overview

Credit risk analysis is a critical task in the finance industry, helping institutions assess the risk of lending to individuals and businesses. This project uses a dataset loaded from Google Drive to demonstrate how to analyze credit risk using logistic regression and other machine learning techniques. The project also provides data visualization techniques to explore relationships within the dataset.

## Installation

To run the project, follow these steps:

1. **Clone this repository**:

    ```bash
    git clone https://github.com/td-02/Credit-Risk-Analysis.git
    ```

2. **Install the necessary Python packages**:

    Make sure you have Python installed, and then use pip to install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Mount Google Drive**:

    In the Colab environment, use the `drive.mount('/content/drive')` command to mount your Google Drive. This step is necessary for loading data from Google Drive.

## Usage

To use the project:

1. **Load Data**: Load the credit risk dataset from Google Drive using the specified file path.
2. **Data Preprocessing**: Handle missing values and encode categorical variables using one-hot encoding.
3. **Model Building**: Define features and target variables, and split the data into training and testing sets.
4. **Model Training**: Train a logistic regression model on the training data.
5. **Model Evaluation**: Make predictions on the test data and evaluate the model's performance using accuracy, confusion matrix, and classification report.
6. **Visualization**: Visualize relationships in the data using scatter plots, violin plots, distribution plots, and other visualizations.

## Data Description

- The dataset includes the following columns:
    - `person_age`: The age of the individual.
    - `person_income`: The income of the individual.
    - `person_home_ownership`: The home ownership status of the individual.
    - `person_emp_length`: The employment length of the individual.
    - `loan_intent`: The intent of the loan.
    - `loan_grade`: The grade of the loan.
    - `loan_amnt`: The amount of the loan.
    - `loan_int_rate`: The interest rate of the loan.
    - `loan_status`: The status of the loan (target variable).
    - `loan_percent_income`: The loan amount as a percentage of income.
    - `cb_person_default_on_file`: Whether the individual has a default on file.
    - `cb_person_cred_hist_length`: The length of the individual's credit history.

- Missing values in the dataset are handled using mean imputation.

## Methods

- **Data Loading**: Load the dataset from Google Drive and display its head and info.
- **Data Preprocessing**: Handle missing values using mean imputation and encode categorical variables using one-hot encoding.
- **Model Building**: Train a logistic regression model and evaluate its performance using accuracy, confusion matrix, and classification report.
- **Visualization**: Visualize relationships in the data using scatter plots, violin plots, distribution plots, and pair grids.

## Results

- The logistic regression model achieves an accuracy of approximately 86% on the test data.
- The code outputs a confusion matrix and classification report to evaluate the model's performance.
- Various visualizations help explore relationships in the data and understand model behavior.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Thank you for your interest in the Credit Risk Analysis project! If you have any questions or issues, feel free to open an issue in this repository.
