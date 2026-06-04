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

![Task 1](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%202/Tasks/Task%201.png?raw=true)  

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

![Task 2](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%202/Tasks/Task%202.png?raw=true)  

## ***Task 3 - List all collections in the `catalog` database***  

To list all collections in the `catalog` databas, we must first instruct MongoDB that we are using `catalog` by running this command.  

```mongodb
`catalog`
```

The terminal should respond `switched to db catalog`. Then, we can proceed by running.  

```mongodb
show collections
```

You can now take a screenshot of the output and save it as `Task 3`.

![Task 3](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%202/Tasks/Task%203.png?raw=true)  

## ***Task 4 - Create an index on the `type` field***  

Create the index by running the command below.  

```mongodb
db.electronics.createIndex({ type: 1 })
```

`type_1` means that the index is created in ascending order. You can now take a screenshot of the code and its output and save it as `Task 4`.  

![Task 4](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%202/Tasks/Task%204.png?raw=true)  

## ***Task 5 -Find the count of laptops***  

To find the number of laptops in the database, run the command below. 

```mongodb
db.electronics.countDocuments({ type: "laptop" })
```

You can take a screenshot of the output and save it as `Task 5`.

![Task 5](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%202/Tasks/Task%205.png?raw=true)  

## ***Task 6 - Count smart phones with 6-inch screen size***  

Similarly as we did in task 5, to count the smart phones with a 6-inch screen size, we can simply add the attribute `screen_size` and the value `6` to the query. 

```mongodb
db.electronics.countDocuments({ type: "smart phone", "screen size": 6 })
```

Take a screenshot of the output and save it as `Task 6`.  

![Task 6](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%202/Tasks/Task%206.png?raw=true)  

## ***Task 7 - Find average screen size of smart phones***  

To find the average screen size of smart phones, we will use the `aggregate()` method, which allows MongoDB to process documents through a sequence of stages. The first stage filters the documents in the `electronics` collection and keeps only the records where the type field is equal to `"smart phone"`. The second stage groups the remaining documents by their `type` field. Since the previous stage selected only smart phones, all documents are grouped under `"smart phone"`. The expression `avg_screen_size: { $avg: "$screen size" }` calculates the average value of the "screen size" field for all smart phone documents.

```mongodb
db.electronics.aggregate([
  { $match: { type: "smart phone" } },
  { $group: { _id: "$type", avg_screen_size: { $avg: "$screen size" } } }
])
```

You can now take a screenshot of the output and save it as `Task 7`.  

![Task 7](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%202/Tasks/Task%207.png?raw=true)  

## ***Task 8 - Export selected fields to a CSV file***  

Finally, to conclude this module, we'll have to exit the MongoDB CLI by running the command

```mongodb
exit
```

Finally, back in the termina, to export the file, we'll have to run the `mongoexport` command below. **Note**: nesure to apply the host, port, user, and password provided by your MongoDB. Do not copy mine, or else the command won't work.

```bash
mongoexport --host 172.21.200.76 --port 27017 -u root -p INSERT_YOUR_PASSOWRD --authenticationDatabase admin --db catalog --collection electronics --type=csv --fields _id,type,model --out electronics.csv
```

You can finally take a screenshot of the output and save it as `Task 8`.

![Task 8](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%202/Tasks/Task%208.png?raw=true)  
