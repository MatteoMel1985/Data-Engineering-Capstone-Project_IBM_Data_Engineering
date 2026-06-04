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
