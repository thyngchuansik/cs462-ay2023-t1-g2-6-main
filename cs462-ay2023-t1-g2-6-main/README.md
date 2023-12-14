[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11585571&assignment_repo_type=AssignmentRepo)

# AWS Architecture
![Cloud Architecture](https://github.com/sunfire-systems/cs462-ay2023-t1-g2-6/assets/85498185/a1516403-ca2a-4815-b39d-ea1b1bb1d770)


> [!IMPORTANT]
> Instructions to run code:
> 1. Install all dependencies before running. ```pip install -r requirements.txt```
> 2. Each folder is a different component of our solution. Check instructions for each folder below.


# Folders
- [rear_cam](#rear_cam)
- [front_cam](#front_cam)

## Rear Camera
1. Connect collision sensor (microbit) via USB
2. Upload ```microbit.py``` into the collision sensor
3. Navigate to terminal and enter ```python run.py COM3```
4. When collision is detected, laptop camera app will open.
5. To upload on Google Drive, create your own Google Drive API key credentials, store in ```rear_cam/config.json``` and add share access to the specified folder. 

Example of credentials: 
```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "your-private-key-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\nyour-private-key\n-----END PRIVATE KEY-----\n",
  "client_email": "your-service-account-email@your-project-id.iam.gserviceaccount.com",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account-email%40your-project-id.iam.gserviceaccount.com"
}
```
6. To receive email notifications, create your own apps password and store in ```rear_cam/apps_pw_config.json```. 

Example of apps password:
```json
{
    "email_password": "abcdefghijklmnop"
}
```
[^Go back to Top^](#folders)

## Front Camera
<ins>Pre-steps to take before using the front camera</ins>
1. Direct to "front_cam/frontend/main.html"
2. Insert your google maps API Key into the ```reversegeocoding``` function

<ins>Steps to use front camera</ins>
1. Launch the frontend from the "front_cam/frontend/main.html"
2. Click on "start" and click "allow" if chrome asked for your location and camera permission
3. Once the live video is showing, wait for the location status to change from "Loading..." to "<Your Location>"
4. Now the front camera is ready to use.

<ins>Process flow</ins>
1. Once the camera detects there is an overhanging branch, it will send an email to the Nparks with the actions required.
2. It will also send the data to the AWS cloud through the API gateway => lamda => dynamoDB
3. The data collected will then be read by a Lamnda function => queried by Amazon Athena which will be used to generate visualisations with Amazon QuickSight [dashboard]

[^Go back to Top^](#folders)