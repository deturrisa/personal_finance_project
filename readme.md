Personal Finance V.1.0
===========================
Intro
-------
Users can casually note down their daily spending on a text editing app on their smartphones or personal computers. Users will use a single .txt file to do so.

At the end of each day (midnight) the app will back up the note into a folder with the backup date as the file name. If the user's computer is powered off then a manual backup must be done by double clicking a .bat file (this will be explained in the set up)

**V.2.0** will introduce a spreadsheet of each month containing the backed up files. The spreadsheet will allow the user to review their total spending of the month as well as most expensive day, least expensive day, average spending etc.

I am hoping **V.3.0** will bring the use of a cloud service such as **AWS** so it will not be required for a computer to remain on order for the backup to complete.

#### Example

```
#input.txt

Travel,50
Lunch,100
Coffee,30
Dinner,80
```
The app backs up **input.txt** and wipes it. The backup file is named **<backup_date>.csv**

```
#01-01-2018.csv

Travel,50
Lunch,100
Coffee,30
Dinner,80
```
```
#input.txt





```
**input.txt** is wiped ready for use the next day.


SET UP
-------
This app requires an account with a file hosting service such as Dropbox or Google Drive and your computer must be synchronised with it.

1. Clone the repository into a directory on your local workspace that is located in Dropbox or GoogleDrive e.g
```
C:\Users\johnsmith\Dropbox\finance_app
```
