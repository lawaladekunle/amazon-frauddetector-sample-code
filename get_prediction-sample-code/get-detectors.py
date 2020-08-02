# Sample Code for Interacting with the Amazon Fraud Detector Get Detectors API

import boto3
import json

fraudDetector = boto3.client('frauddetector')
            
response = fraudDetector.get_detectors()
print(json.dumps(response))
