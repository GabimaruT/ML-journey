# Online Machine Learning

On this day we are going to learn about online machine learning.

Online machine learning trains models incrementally as new data arrives instead of using a fixed dataset.

Key ideas:
- Data is processed one instance or batch at a time.
- The model updates continuously with new information.
- It is useful for streaming data, changing environments, and low-latency systems.

Example methods:
- Online gradient descent
- Incremental decision trees
- Adaptive filters

Benefits:
- Can adapt to new trends quickly.
- Uses less memory than batch training.
- Works well when data arrives over time.

Challenges:
- Can be sensitive to noisy data.
- Needs careful tuning of learning rate and update rules.
- May forget older patterns if not managed properly.

Summary: online learning is a fast, flexible way to train models on data streams, especially when the data distribution evolves over time.
