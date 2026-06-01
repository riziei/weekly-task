# 20 Newsgroups Text Classification using Naive Bayes

## Overview

This project demonstrates text classification using the 20 Newsgroups dataset from scikit-learn.

A Naive Bayes classifier was trained to classify news articles into categories using TF-IDF vectorization.

The project also includes:
- Data preprocessing
- Text vectorization
- Classification metrics
- Confusion matrix visualization
- Additional data visualizations
- Reflection on AI-assisted coding

---

## Dataset

Dataset used:
- 20 Newsgroups Dataset (`sklearn.datasets`)

Categories used for faster execution:
- sci.space
- rec.sport.hockey

---

## Technologies Used

- Python
- scikit-learn
- pandas
- matplotlib
- NumPy

---

## Project Workflow

1. Load dataset
2. Create pandas DataFrame
3. Explore dataset
4. Split train and test data
5. Convert text into TF-IDF vectors
6. Train Naive Bayes classifier
7. Make predictions
8. Evaluate model
9. Visualize results
10. Write reflection

---

## Machine Learning Model

Model used:
- Multinomial Naive Bayes (`MultinomialNB`)

Text preprocessing:
- TF-IDF Vectorization (`TfidfVectorizer`)

---

## Evaluation Metrics

The following metrics were calculated:

- Accuracy
- Precision
- Recall
- Confusion Matrix

---

## Visualizations Included

- Category count bar chart
- Actual vs Predicted plot
- Confusion matrix

---

## Key Concepts Learned

* Natural Language Processing (NLP)
* Text Vectorization using TF-IDF
* Naive Bayes Classification
* Model Evaluation Metrics
* Confusion Matrix Interpretation

## Reflection on AI-Assisted Coding

AI tools were used to:

* Generate starter code
* Debug implementation issues
* Explain TF-IDF vectorization
* Understand Naive Bayes classification
* Improve code structure and documentation

Prompt engineering techniques such as structured prompting and iterative refinement helped improve the quality of generated code and explanations.

## Conclusion

This project demonstrates how machine learning can be applied to text classification tasks. Using TF-IDF and Naive Bayes, news articles can be effectively categorized with good performance and minimal preprocessing.
