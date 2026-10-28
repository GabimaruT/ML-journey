# Batch Machine Learning

On this day we are going to learn about batch machine learning.

Batch learning trains models using a fixed dataset all at once.

Key ideas:
- The model is trained on the entire dataset before use.
- Training happens in one or a few passes over the data.
- The model does not update until it is retrained.

Example methods:
- Batch gradient descent
- Traditional neural network training
- Support vector machines

Benefits:
- Stable training on full datasets.
- Often easier to optimize and evaluate.
- Good for static data with no rapid changes.

Challenges:
- Requires access to the complete dataset.
- Can be slow or memory-intensive for large data.
- Needs retraining when new data arrives.

Summary: batch learning is best when data is available upfront and the problem does not need continuous model updates.
