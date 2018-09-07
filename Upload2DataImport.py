# Note: This code assumes you have an authorized Analytics service object.
# See the Data Import Developer Guide for details.

# This request uploads a file custom_data.csv to a particular customDataSource.
# Note that this example makes use of the MediaFileUpload Object from the
# apiclient.http module.

import argparse
from apiclient.discovery import build
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools

def get_service(api_name, api_version, scope, client_secrets_path):
  """Get a service that communicates to a Google API.
  Args:
    api_name: string The name of the api to connect to.
    api_version: string The api version to connect to.
    scope: A list of strings representing the auth scopes to authorize for the
      connection.
    client_secrets_path: string A path to a valid client secrets file.
  Returns:
    A service that is connected to the specified API.
  """
  # Parse command-line arguments.
  parser = argparse.ArgumentParser(
      formatter_class=argparse.RawDescriptionHelpFormatter,
      parents=[tools.argparser])
  flags = parser.parse_args([])
  # Set up a Flow object to be used if we need to authenticate.
  flow = client.flow_from_clientsecrets(
      client_secrets_path, scope=scope,
      message=tools.message_if_missing(client_secrets_path))
  # Prepare credentials, and authorize HTTP object with them.
  # If the credentials don't exist or are invalid run through the native client
  # flow. The Storage object will ensure that if successful the good
  # credentials will get written back to a file.
  storage = file.Storage(api_name + '.dat')
  credentials = storage.get()
  if credentials is None or credentials.invalid:
    credentials = tools.run_flow(flow, storage, flags)
  http = credentials.authorize(http=httplib2.Http())
  # Build the service object.
  service = build(api_name, api_version, http=http)
  return service
# Define the auth scopes to request.
scope = ['https://www.googleapis.com/auth/analytics']
# Authenticate and construct service.
service = get_service('analytics', 'v3', scope, 'client_secrets.json')

from apiclient.http import MediaFileUpload
media = MediaFileUpload(path_and_file,
                          mimetype='application/octet-stream',
                          resumable=False)
daily_upload = service.management().uploads().uploadData(
      accountId='000000000',
      webPropertyId='UA-00000000-1',
      customDataSourceId='a0a0a0a0a0a0a0a0a0a0',
      media_body=media).execute()
print('Fin Subida')
