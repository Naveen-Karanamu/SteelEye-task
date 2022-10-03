
# Working on the xml file

Here the xml file is been converted into the csv file formate and is been uploaded to thte AWS s3 Bucket. Currently use Postman API for doing the same.

# Functions:
* xml_to_csv - This is the function to convert the xml file to the csv

# Error Handling:
* Handled for the file's path and csv file name

# Run the code: 

* In IDE Terminal
```bash
python -u main.py {xml file's path} {csv file name with .csv extension}
```
* CMD

```bash
python3 main.py {xml file's path} {csv file name with .csv extension}
```

# Working with AWS s3 Bucket

Pre-requisites:
- Create a .env file for parsing your AWS Key & AWS Secret Key and create 2 environment variables, in the given formate below -
```console
AWS_ACCESS_KEY_ID = {your personal Access key ID}
AWS_SECRET_ACCESS_KEY = {your personal Secret Access Key}
```

# Installing Packages
It will install all the used packages for the backend part of AWS
 ```bash
 npm install
 ```

 # Starting the Server
 ```bash
 npm dev
 ```

 # Server Configurations
 * Listen to the http://localhost:3001 server in the postman to push the files
 * Use /file/up route to push the files from the postman API