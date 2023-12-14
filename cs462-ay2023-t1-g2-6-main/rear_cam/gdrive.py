from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video_googledrive(video_name):
    # Set the path to your credentials JSON file (downloaded in step 1)
    # credentials_file = 'path/to/your/credentials.json'
    credentials_file = 'config.json'

    # Create a service object for the Google Drive API
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        credentials_file, scopes=['https://www.googleapis.com/auth/drive']
    )

    # Create a Google Drive API service object
    service = build('drive', 'v3', credentials=creds)

    # Define the file path to the video you want to upload
    video_file_path = 'video/' + video_name

    # Specify the target folder ID in Google Drive
    folder_id = '1uG5UDHv109Jeds3PAqw4FUjWJOEkRcSF'

    # Create a file metadata
    file_metadata = {
        'name': video_name,  # Name for the file in Drive
        'parents': [folder_id],  # ID of the target folder
    }

    # Upload the video file
    media = MediaFileUpload(video_file_path, mimetype='video/mp4')
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print('File ID: %s' % file.get('id'))
    return file.get('id')
