# Sample Code for Interacting with the Amazon Fraud Detector Get Event Prediction API

import boto3
import json

fraudDetector = boto3.client('frauddetector')

response = fraudDetector.get_event_prediction(
detectorId = 'high_risk_signup_demo',
detectorVersionId='1',
eventId = '802454d3-f7d8-482d-97e8-c4b6db9a0771',
eventTypeName = 'high_risk_signups_demo',
eventTimestamp = '2020-07-31T20:20:48Z',
entities = [{'entityType':'store_user', 'entityId':'7654'}],
eventVariables = {
    'email_address' : 'fake_nathan47@example.org',
    'ip_address' : '89.184.149.46'
}
)

print(json.dumps(response))
