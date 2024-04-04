<H1>**Assignment for Settyl Internship Application**</H1>

<H2>Project Overview</H2>
The objective of this project is to develop a text classification machine learning model to predict internal status based on external status descriptions based on a given dataset.

<H2>Data Preprocessing</H2>

  <li>The dataset is loaded from the provided "dataset.json" file using pandas.
  <li>Then categorical variables are encoded using LabelEncoder for further processing, I have transformed a strings to numpy arrays.
  <li>Data is split into features (X) and target/label (Y) variables.
  <li>Training and validation sets are created using the train_test_split function from sklearn.model_selection. As name suggest it splits data for training and validation</li>

<H2>Model Development</H2>

  <li>A neural network model is designed using TensorFlow's Keras.
  <li>The model architecture consists of a single Dense layer with softmax activation.
  <li>Model compilation includes defining optimizer, loss function, and evaluation metrics.
  <li>Training is conducted using the fit method, and validation is performed on the validation set.
  <li>Model accuracy and loss are assessed on the validation set.
  <li> Accuracy of different activation are given
      <ul><li>softmax activavtion accuracy = 0.4244897961616516</li>
      <li>ReLU (Rectified Linear Unit) activation accuracy = 0.2489795982837677</li>
      <li>Sigmoid activation accuracy = 0.4285714328289032</ul></li>

<H2>Model Improvisation</H2>
As accuracy of previous models are too low. I have decided to use GaussianNB model. Gaussian Naive Bayes is a simple yet effective probabilistic classifier that makes predictions based on the Bayes theorem and the assumption of conditional independence between features. It has given me accuracy of 0.7795918367346939. From this accuracy it implies that the data may have some level of separability between classes.

**As a reason I used Random forest alogorithm for classification and I got accuracy = 0.9959183673469387**
When I have seen dataset X_train and y_train, I analysed that there is only one parameter is passed, so I used logistic regression model. It have better time complexity and lower training time than Random Forest and I got exact same accuracy, which implies that decision boundary between classes is relatively simple and linear.
<h4>**Final Accuracy of Model = 0.9959183673469387**</h4>
