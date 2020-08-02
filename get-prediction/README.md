# **Amazon Fraud Detector - Sample Code**

This repository contains sample code for interacting with the Amazon Fraud Detector API. This was built using the AWS Python SDK [https://amzn.to/31efZjJ](https://amzn.to/31efZjJ).
This requires python v2.7.x. Sample data was gotten from AWS [https://amzn.to/39WeavO](https://amzn.to/39WeavO)

**get_prediction-sample-code.py:** Contains same code for getting event predictions from the API.

**get-prediction.py:** This allows you to get event predictions from the API. It prompts you for an email address and IP Address then outputs the results of the prediction. You will need to manually add the information for the following items.

* **detectorId:** The name of the detector to be used.
* **detectorVersionId:** The version number of the detector. e.g: 1 (for version 1.0)
* **eventTypeName:** The event type name.
* **entityTypeName:** The entity type name.
* **entityId:** This can be any random number. e.g. 1234

**Setting up the environment**

The get-prediction.py file is under the get-prediction folder and has an accompanying requirements.txt file. To run the code perform the following steps.

* `[Install Virtualenv](https://bit.ly/33il9hh)`
* `git clone <repo_url> <DIR>`
* `cd <DIR>/get-prediction`
* `virtualenv .`
* `source bin/activate`
* `pip install -r requirements.txt`
* `python get-prediction.py`













