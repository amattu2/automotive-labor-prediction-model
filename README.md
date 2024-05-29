# Introduction

This is a machine learning Jupyter Notebook that trains a model to predict the
automotive repair order labor items based on the ticket description alone.

It's trained on a dataset with over 250,000 rows and 50,000 unique ticket descriptions.
While the dataset and model are not publicly available, you can see the results in
the [Notebook](./Notebook.ipynb).

This repository also contains a Flask API that can be used to make predictions
based on the model. You can see the API documentation below.

Feel free to build on top of this project or use it as a reference for your own.

# The Model

The model is built using a dataset with 251,000 repair line items (labor lines)
that are mapped to 55,000 ticket descriptions (overall description of the work).
The model is trained to infer the necessary line items that should be added to a
ticket based solely on the ticket description.

## Selected Regressor

As seen in the [Notebook](./Notebook.ipynb), there were five total regressors used
to compare the results. The best model was XGBRegressor based on the following
metrics in addition to the overall training time:

<table border="1">
  <thead>
    <tr>
      <th colspan="3">Model: ABC 123 TBD</th>
    </tr>
  </thead>
  <thead>
    <tr>
      <th></th>
      <th>Metric</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MSE</td>
      <td>0.00033</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MAE</td>
      <td>0.000546</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MAPE</td>
      <td>1209895899589.968262</td>
    </tr>
    <tr>
      <th>3</th>
      <td>R2</td>
      <td>0.073394</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CE</td>
      <td>3986.64</td>
    </tr>
  </tbody>
</table>

## Prediction Example

Description: `Replace engine oil and filter`
Predicted line items:

- tbd
- tbd

# Deploying the API

To deploy the local development server, run the following commands:

```bash
pip install flask flask_restful flask_cors pickle numpy
```

```bash
PORT=5000 python src/app.py
```
