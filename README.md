# Linode_objectstorage_watchfolder
This is script functions as a watch folder for Linode object storage. 
USECASE: Typically when a new file or a folder is added to the object storage bucket and a corresponding event needs to be triggered access logs or event logs on the bucket is used to trigger these events. This script automates the process of triggering events when new objects are added to the storage. The script consists of a function that regularly scans the object storage and when a new object is added a message is displayed. 
Prerequisite: A nanode or any exisitng VM to host the script. The script will inturn read/list the object to check for new files. 
Steps to follow: 
1. Setup s3cmd on the VM and ensure it can read/list objects on the bucket you want to track through watch folder. Refer this link to setup s3cmd on your VM: https://techdocs.akamai.com/cloud-computing/docs/using-s3cmd-with-object-storage#linux. (Ensure you follow steps for Linux OS only)
2. Once s3cmd is setup, run the script on the VM.
3. When you add a new object a notification will be visible on your terminal window stating "New object added: "Object_name"
4. This notification can be further added to any necessary pipeline to trigger a consequent function. 
