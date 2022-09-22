# pubchempy
Python script to retreive information from PubChem and insert into a .xlsx file

## Usage
Run the script with a text file as an argument that has each compound name as a separate line. See c.txt for an example of how the file should be formatted.

```
python3 pubmedxls.py c.txt
```

This will create a .xlsx file in the same directory, called xlspy, which contains the output

## Basic installation guide
First, click the green "Code" button, then hit "Download ZIP." Next, click on the ZIP file to unzip it. 
Open the app "Terminal", which you can do by hitting Command and Spacebar, then typing "Terminal"
From there, type paste in this command and hit enter.

```
cd Downloads/pubchempy-main
```

You are now ready to run. Open the text file c.txt and add any compounds you want information about to a new line. Then type in this command and hit enter:

```
python3 pubmedxls.py c.txt
```
