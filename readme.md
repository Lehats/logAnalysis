
This is a project for demonstrating sql database handling using python and PostgreSQL.

In this case the DB runs on a Virtual machine powered by VirtualBox.
Vagrant is the software that sets up your VM and let you share documents from your local machine and your VM.
This requires vagrant to install Linux on your VM so it may take a while. 

Install VirtualBox:

https://www.virtualbox.org/wiki/Download_Old_Builds_5_1

To install Virtualbox use the link above and install the platform package for your os. You won't need the extension packages.
You don't need to run Virtualbox after installation. Vagrant will do that for you.

Install Vagrant:

https://www.vagrantup.com/downloads.html

To install Vagrant use the link above.

Get the necessary files adn set up vagrant:

https://github.com/udacity/fullstack-nanodegree-vm

Fork and clone the repo above. Once you done that navigate to the repo where you see a directory called vagrant. Chenage to this directory and run vagrant up. If it is the first time, this will cause the installation of linux and may take a while. Once this is done, you can always start your VM using vagrant up. Eitherway to log on to your vm us the commant vagrant ssh. After your log in was sucessfully, you have access to all the files in your local directory from where you setted up vagrant. 

Download teh data:

https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

You can download the sql file from the link above. Please copy it to your vagrant directory (the shared folder). After you logged onto your VM useing vagrant ssh run the following command:

psql -d news -f newsdata.sql

this will load the data from newsdata.sql into the DB news and create all the necessary tables. When this step was sucessfully you can alwas acces the db with the folowing command.

psql news

Run the python script:

Once your logged in and completed all the steps above. You can simply run the python script neDa.py by the command

python neDa.py

But since this script uses a view, first manually create the view below.

create pathCount View:

Create this view, because it'll be used in the queries of the get_Top_Articles()- and get_Top_Authors()-functions. So it cleans up both queries. Run psql news to get acces to the news-DB and insert the query below.


 create or replace view pathCount as select path, count(*) as count from log where status = '200 OK' and path like '%/article%'group by path order by path;