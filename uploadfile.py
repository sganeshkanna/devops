from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()

def createFolderIfNotExists(drive,name):
	upload_folder  = name
	upload_folder_id = None
	file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
	for file_folder in file_list:
		if file_folder['title'] == upload_folder:
			upload_folder_id = file_folder['id'] #Get the matching folder id
			return upload_folder_id
		else:
			print('Creating Folder ....')
			file_new_folder = drive.CreateFile({'title': upload_folder,"mimeType": "application/vnd.google-apps.folder"})
			file_new_folder.Upload()
			upload_folder_id = file_new_folder['id']
			return upload_folder_id

def uploadFile(drive,folderid,filename):
	print('Uploading File ....')
	file = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folderid}]})
	file.SetContentFile(filename)
	uploaded = file.Upload()
	permission = file.InsertPermission({'type': 'anyone','value': 'anyone','role': 'reader'})
	return file['alternateLink']

def setupAuthentication():
	gauth.LoadCredentialsFile("mycreds.txt")
	if gauth.credentials is None:
		gauth.LocalWebserverAuth()
	elif gauth.access_token_expired:
		gauth.Refresh()
	else:
		gauth.Authorize()
	gauth.SaveCredentialsFile("mycreds.txt")


def listAllFiles():
	file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
	for file1 in file_list:
		print('title: %s, id: %s' % (file1['title'], file1['id']))


setupAuthentication()
drive = GoogleDrive(gauth)
folder = createFolderIfNotExists(drive,'Uploads')
url = uploadFile(drive,folder,'DriverBuddy_develop_release_V1.5.5.apk')
print(url)


