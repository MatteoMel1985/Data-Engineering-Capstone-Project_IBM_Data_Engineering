# ***Exercise 1 - Check the lab environment***  

To check if 'mongoimport' and 'mongoexport' are installed, run the commands below (ensuring that you are in the path `/home/project`). 

```Bash
mongoimport --version
```

And 

```Bash
mongoexport --version
```

If they are present, you will see their versions in the terminal. The one below is an example of output. 

```Bash
mongoimport version: 100.13.0
git version: 23008ff975be028544710a5da6ae749dc7e90ab7
Go version: go1.23.11
   os: linux
   arch: amd64
   compiler: gc
```

However, if the output is `command not found`, proceed to install the MongoDB database tools with the commands below.  

```Bash
sudo apt update
sudo apt install -y mongodb-database-tools
```

Finally, to download `catalog.json`, proceed by running the code below. 

```Bash
wget -O catalog.json "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json"
```

The command `-O` tells `wget` to save the file `catalog.jso`. If everything was executed correctly, the file will be downloaded on the path `/home/project`, and you will be able to see it in the Explorer pane. 

# ***Exercise 2 - Working with MongoDB***  

## ***Task 1 Import data into MongoDB***  

Before importing the file, start your MongoDB Database (as we did in the previous module with MySQL) by going on `Explorer Pane > MongoDB > Start`.  

Once ready, you can import the file by running the command below. **NOTE**: Ensure to insert the host, the user, and the password provided by your MongoDB and visible in the section `Connection Information`.  

```Bash
mongoimport --host 172.21.200.76 --port 27017 -u root -p INSERT_YOUR_PASSWORD --authenticationDatabase admin --db catalog --collection electronics --file catalog.json
```

If imported correctly, you should see a similar output in the terminal.  

```Bash
connected to: mongodb://172.21.200.76:27017/
XXX document(s) imported successfully. 0 document(s) failed to import.
```

You can now take a screenshot of the code and its output and save it as `Task1`.  

![Task 1](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Modue%202/Tasks/Task%201.png?raw=true)  

## ***Task 2 - List all databases***  

Again, to list all databases, we'll have to run the MongoDB CLI command provided by MongoDB under `Connection Information` (ensure to use your own and don't copy mine, as it won't work in your EDI). 

```Bash
mongosh mongodb://root:xvwJpkmeX6cUq4heKmIEEnDp@172.21.200.76:27017
```

Once run, your terminal will appear as follows:

```mongodb
test>
```

Then, run the command below. 

```nmongodb
show dbs
```

You can now take a screenshot of the output and save it as `Task 2`.  

![Task 2](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Modue%202/Tasks/Task%202.png?raw=true)
