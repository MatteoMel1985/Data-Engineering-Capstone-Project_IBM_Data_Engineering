![Skills_Network](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/images/image.png)  

<h1 align="center">Prediction Algorithms and Model Evaluation in Apache Spark</h1>  

Apache Spark provides machine learning tools through Spark MLlib, a library designed to build scalable machine learning models on large datasets.

In machine learning, a prediction algorithm is a mathematical method that learns patterns from existing data and uses those patterns to make predictions on new data.

A prediction algorithm usually receives:  

* Input variables, also called features.
* A target variable, also called the label.
* A mathematical method for learning the relationship between the features and the label.

Depending on the type of target variable, prediction problems are usually divided into two main categories:

* Regression, where the target is a continuous numerical value.
* Classification, where the target is a category or class.

For example, predicting a product price is a regression problem, while predicting whether a customer will buy or not buy a product is a classification problem.

<h1 align="center"><i>Prediction Algorithms</i></h1>  

# ***Linear Regression***  

Linear Regression is a supervised learning algorithm used to predict a continuous numerical value.

It assumes that there is an approximately linear relationship between the input features and the target variable. In other words, the model tries to represent the target value as a weighted combination of the input variables.

From a mathematical standpoint, a simple linear regression model can be represented as:

y = b0 + b1x1 + b2x2 + ... + bnxn

Where:  

* `y` is the predicted value.
* `x1, x2, ..., xn` are the input features.
* `b0` is the intercept.
* `b1, b2, ..., bn` are the coefficients learned by the model.

The purpose of training a Linear Regression model is to find the coefficients that minimise the difference between the real values and the predicted values.

In simple terms, Linear Regression tries to answer the question:

> Given these input values, what numerical value should I expect as the output?

It is commonly used for predicting prices, sales, demand, measurements, trends, or any continuous quantity.  

# ***Logistic Regression***  

Logistic Regression is a supervised learning algorithm mainly used for classification problems.

Despite the word “regression” in its name, Logistic Regression is not usually used to predict continuous values. Instead, it predicts the probability that a record belongs to a specific class.

For binary classification, the output is usually a probability between 0 and 1.

For example:

0.87 = high probability that the record belongs to class 1
0.12 = low probability that the record belongs to class 1

The algorithm uses a mathematical function called the sigmoid function, which converts numerical values into probabilities.

In simple terms, Logistic Regression tries to answer the question:  

> What is the probability that this record belongs to a certain category?

It can be used to predict whether a customer will buy a product, whether an email is spam, whether a transaction is suspicious, or whether an event belongs to a particular class.

Spark also supports multinomial Logistic Regression, which can be used when there are more than two possible classes.  

# ***Decision Trees***  

A Decision Tree is a supervised learning algorithm that makes predictions by splitting the data into a sequence of decision rules.

The structure of the model resembles a tree:

* The root node is the starting point.
* The internal nodes represent decision conditions.
* The branches represent the possible outcomes of those conditions.
* The leaf nodes represent the final prediction.

For example, a Decision Tree may ask questions such as:  

Is the product price greater than 100?
Is the customer located in a specific country?
Is the number of visits greater than 5?

Based on the answers, the model follows different branches until it reaches a final prediction.

Decision Trees can be used for both:  

* Regression, where the final output is a numerical value.
* Classification, where the final output is a category.

In simple terms, a Decision Tree works like a structured set of logical rules:

> If this condition is true, go this way; otherwise, go another way.

Decision Trees are easy to understand and interpret, but they can sometimes overfit the training data if they become too complex.  

# ***Random Forest***  

A Random Forest is an ensemble learning algorithm based on many Decision Trees.

Instead of training only one tree, a Random Forest trains several trees and combines their predictions. This usually produces a more stable and reliable model.

The word forest refers to the fact that the algorithm is made of many trees.

For regression problems, the final prediction is usually calculated as the average of the predictions produced by all the trees.

For classification problems, the final prediction is usually based on majority voting.

For example, if five trees predict the following classes:

Tree 1: Yes
Tree 2: Yes
Tree 3: No
Tree 4: Yes
Tree 5: No

The Random Forest would predict:

Yes

Because most trees voted for that class.

Random Forest models are usually more accurate than individual Decision Trees because they reduce the risk of overfitting. Each tree sees a slightly different version of the data, and the final result is obtained by combining several independent predictions.

In simple terms, Random Forest works by asking many Decision Trees for their opinion and then combining their answers.  

# ***Gradient-Boosted Trees***  

Gradient-Boosted Trees are another ensemble learning method based on Decision Trees.

However, they work differently from Random Forests.

A Random Forest builds many trees independently, while Gradient-Boosted Trees build trees sequentially. Each new tree tries to correct the mistakes made by the previous trees.

The basic idea is:

First tree: makes an initial prediction.
Second tree: focuses on the errors of the first tree.
Third tree: focuses on the remaining errors.
And so on.

This process is called boosting because the model gradually improves by learning from its previous mistakes.

Gradient-Boosted Trees can be used for both regression and classification problems. They are often powerful models, especially when the relationship between the features and the target variable is complex and non-linear.

In simple terms, Gradient-Boosted Trees work by building a sequence of models, where each new model improves the weaknesses of the previous one.  

# ***Clustering Algorithms***  

Clustering algorithms are different from the previous algorithms because they are usually unsupervised learning methods.

This means that they do not require a known target variable. Instead, they try to discover hidden groups or patterns inside the data.

One common clustering algorithm is K-Means.

K-Means groups records into a fixed number of clusters based on similarity. Records inside the same cluster should be more similar to each other than to records in other clusters.

For example, clustering can be used to group:  

* Customers with similar purchasing behaviour.
* Products with similar characteristics.
* Search terms with similar patterns.
* Users with similar activity levels.

From a mathematical standpoint, K-Means tries to minimise the distance between each data point and the centre of its assigned cluster.

In simple terms, clustering tries to answer the question:

> Which records are naturally similar to each other?

Although clustering is not prediction in the strict supervised-learning sense, it is still an important machine learning technique because it helps discover structure inside the data.  

# ***Machine Learning Pipelines***  

A Machine Learning Pipeline is a sequence of steps used to prepare data, train a model, and generate predictions.

Instead of treating each operation separately, a pipeline connects them into one organised workflow.

A typical Spark ML pipeline may include:  

1. Selecting the input columns.
2. Combining multiple input columns into a single features column.
3. Scaling or transforming the features.
4. Training a machine learning algorithm.
5. Applying the trained model to new data.
6. Evaluating the predictions.

In Spark, pipelines are useful because they make the machine learning process cleaner, more reusable, and easier to maintain.

For example, a pipeline may combine `VectorAssembler`, `StandardScaler`, and `LinearRegression` into one complete workflow.

In simple terms, a pipeline is the full path followed by the data, from raw input to final prediction.  

<h1 align="center"><i>Model Evaluation</i></h1>  

After a model has been trained and used to generate predictions, it is necessary to evaluate how good those predictions are.

Model evaluation is the process of measuring the performance of a machine learning model.

The purpose of model evaluation is to answer questions such as:

> How close are the predictions to the real values?

> Is the model reliable?

> Is the model accurate enough to be useful?

> Is the model learning meaningful patterns, or is it making poor predictions?

Different types of machine learning problems require different evaluation metrics. For regression problems, where the target variable is numerical, common metrics include Mean Squared Error, Mean Absolute Error, and R-Squared.  

# ***Mean Squared Error***  

Mean Squared Error, or MSE, measures the average squared difference between the real values and the predicted values.

The formula is:

MSE = average of (actual value - predicted value)²

The error is squared, which means that larger errors are penalised more heavily than smaller errors.

For example, an error of `10` becomes `100`, while an error of `2` becomes `4`.

This makes MSE useful when large prediction errors are especially undesirable.

A lower MSE means that the model is performing better.

In simple terms, Mean Squared Error tells us:  

> How large are the model’s errors on average, with large errors receiving extra penalty?

# ***Mean Absolute Error***  

Mean Absolute Error, or MAE, measures the average absolute difference between the real values and the predicted values.

The formula is:

MAE = average of |actual value - predicted value|

Unlike MSE, MAE does not square the errors. This means it is easier to interpret because it remains in the same unit as the original target variable.

For example, if the model is predicting prices in dollars, the MAE is also expressed in dollars.
If the model is predicting sound levels in decibels, the MAE is also expressed in decibels.

A lower MAE means that the model’s predictions are closer to the real values.

In simple terms, Mean Absolute Error tells us:  

> On average, how far are the predictions from the real values?

# ***R-Squared***  

R-Squared, also written as R², measures how much of the variation in the target variable is explained by the model.  

Its value is usually between `0` and `1`.

A value close to `1` means that the model explains a large part of the variation in the data.
A value close to `0` means that the model explains very little of the variation.

For example:

R² = 0.90

Means that the model explains about 90% of the variation in the target variable.

R² = 0.20

Means that the model explains only about 20% of the variation.

In simple terms, R-Squared tells us:

> How well does the model explain the behaviour of the target variable?

However, R-Squared should not be used alone. A high R-Squared does not always mean that the model is perfect, and it should usually be interpreted together with other metrics such as MSE and MAE.  

<h1 align="center"><i>Final Notes</i></h1>  

Prediction algorithms allow a machine learning model to learn relationships and patterns from data.

Model evaluation allows us to measure whether those predictions are accurate and reliable.

In Apache Spark, these concepts can be applied at scale through Spark MLlib, making it possible to build machine learning workflows for large datasets using distributed computing.

In this module, these ideas are introduced through a practical Spark ML pipeline, where the data is prepared, transformed, used to train a Linear Regression model, evaluated with regression metrics, and saved for future use.  

# Author
# ***[Matteo Meloni](https://www.linkedin.com/in/matteo-meloni-40a357154/)***
