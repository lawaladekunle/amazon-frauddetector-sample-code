# Amazon Fraud Detector Sample Code - Test the prediction API
# Adekunle Lawal - lawaladekunle@gmail.com
# 

from email_validator import validate_email, EmailNotValidError
import boto3, json, ipaddress, socket, time, uuid
from datetime import datetime


# Functions


# Variables

# timestamp
now = datetime.now()
timeStamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")


    # variables for frauddetector
detectorId = 'Detector_Name'
detectorVersionId = 'Detector_Version_As_Integer'
eventTypeName = 'Event_Type_Name'
entityTypeName = 'Entity_Type_Name' # Entity Type Name
entityId = 'Set_An_Entity_ID' # This can be any random number e.g. 1234
eventId = str(uuid.uuid4()) # Automatically generated


# Validate the Email Address Format

emailAddress = raw_input("Enter the email address:")

try:
      # validate.
        valid = validate_email(emailAddress)

          # update with the normalized form.
        emailAddress = valid.email
        print("The email format is valid", str(emailAddress))
except EmailNotValidError as err:
      # email is not valid, exception message is human-readable
        print(str(err))
        raise SystemExit




# Validate the IP Address Format
ipAddress = raw_input("Enter the IP address:")

try:
     #validate
    socket.inet_aton(ipAddress)
    print("The IP address format is valid", ipAddress)
except ValueError('Check the format of the IP Address!'):
    print("The IP address format is invaild, try again")



# Query the Amazon Fraud Detector Prediction API

fraudDetector = boto3.client('frauddetector')

response = fraudDetector.get_event_prediction(
detectorId = detectorId,
detectorVersionId = detectorVersionId,
eventId = eventId,
eventTypeName = eventTypeName,
eventTimestamp = timeStamp,
entities = [{'entityType': entityTypeName, 'entityId': entityId}],
eventVariables = {
    'email_address' : emailAddress,
    'ip_address' : ipAddress
}
)


# Parsing Json Output

initalJson = json.dumps(response)
jsonFeed = json.loads(initalJson)

modelType = jsonFeed["modelScores"][0]["modelVersion"]["modelType"]
modelNumber = jsonFeed["modelScores"][0]["modelVersion"]["modelVersionNumber"]
modelName = jsonFeed["modelScores"][0]["modelVersion"]["modelId"]

httpStatusCode = jsonFeed["ResponseMetadata"]["HTTPStatusCode"]
modelOutputPrediction = json.dumps(jsonFeed["modelScores"][0]["scores"])
modelRuleOutcome = jsonFeed["ruleResults"][0]["outcomes"][0]

# Outputs

print('\n************* Details ********************\n')
print('You are using the model type: ', str(modelType))
print('You are using the model: ', str(modelName))

print('The Model version number is: ', str(modelNumber))
print('The HTTP Status Code is: ', str(httpStatusCode))

print('\n************ Results ****************\n')
print('The model output variable and model score are: ', str(modelOutputPrediction))
print('Next step for the user: ', str(modelRuleOutcome))
print('\n*************************************')






