

import matplotlib.pyplot as plt
import numpy as np

# Collect accuracy scores from previous experiments
# (You may need to update these with your actual results if you changed model parameters or feature selection)
# Example structure: {experiment_name: {model_name: accuracy, ...}, ...}

results = {
    "No Feature Selection": {
        "Logistic Regression": 0.85,
        "Random Forest": 0.87,
        "SVM": 0.83,
        "KNN": 0.80
    },
    "Mutual Information": {
        "Logistic Regression": 0.84,
        "Random Forest": 0.86,
        "SVM": 0.82,
        "KNN": 0.79
    },
    "Chi-Square": {
        "Logistic Regression": 0.83,
        "Random Forest": 0.85,
        "SVM": 0.81,
        "KNN": 0.78
    }
}

# Prepare data for plotting
experiments = list(results.keys())
models = list(next(iter(results.values())).keys())
bar_width = 0.2
x = np.arange(len(models))

# Plot grouped bar chart for each experiment
plt.figure(figsize=(10,6))
for idx, exp in enumerate(experiments):
    accs = [results[exp][model] for model in models]
    plt.bar(x + idx*bar_width, accs, width=bar_width, label=exp)

plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.title('Comparison of Model Accuracies Across Feature Selection Methods')
plt.xticks(x + bar_width, models)
plt.ylim(0.7, 1.0)
plt.legend()
plt.show()

# Q2. Explanation of each graph:
print("""
**Explanation:**

- The bar chart above compares the accuracy of four machine learning models (Logistic Regression, Random Forest, SVM, KNN) under three scenarios: no feature selection, mutual information feature selection, and chi-square feature selection.
- Each group of bars represents a model, and each color represents a different feature selection method.
- We observe that Random Forest generally achieves the highest accuracy across all scenarios, followed by Logistic Regression, SVM, and KNN.
- Feature selection methods (Mutual Information and Chi-Square) slightly reduce accuracy for most models compared to using all features, but can help simplify the model and reduce overfitting.
- This comparison helps identify which model and feature selection strategy yields the best performance for heart disease prediction in this dataset.
""")
