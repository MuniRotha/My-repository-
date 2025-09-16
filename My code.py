import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import roc_curve, auc
# Assuming 'results' is a DataFrame containing the performance metrics
# with columns: 'Model', 'Accuracy', 'Precision', 'Recall', 'F1_Score', 'AUC'

# Set the figure size
plt.figure(figsize=(12, 8))

# Create subplots for each metric
metrics = ['Accuracy', 'Precision', 'Recall', 'F1_Score', 'AUC']
for i, metric in enumerate(metrics, 1):
    plt.subplot(2, 3, i)
    sns.barplot(x='Model', y=metric, data=results)
    plt.title(f'{metric} Comparison')
    plt.ylim(0, 1)

# Adjust layout
plt.tight_layout()
plt.show()

# Assuming 'y_true' and 'y_pred' are the true labels and predicted probabilities
fpr, tpr, _ = roc_curve(y_true, y_pred)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc='lower right')
plt.show()

