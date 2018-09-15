
###### Udacity project at Full Stack Devekoper

This project  will develop an application that provides a list of Dogs  within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Getting Started
You can _clone_ this <a href="https://github.com/MayAlalawi/DogsCataloge.git">project</a> via <a href="https://github.com"> GitHub</a> to your local machine.
 
 ## Requirements 
 
 This project makes use of the same Linux-based virtual machine (VM) and Vagrant.This virtual machine will give you the
 ability to create and manipulate database and support software needed for this project.
 
 
  - <a href="https://www.vagrantup.com/">Vagrant</a></li>
  - <a href="https://www.virtualbox.org/wiki/Download_Old_Builds_5_1">Virtual Box</a></li>
  - <a href="https://git-scm.com/downloads">Git Bash</a></li>
  - You will also need to _clone_ or _download_ these following files to make it work<a href="https://github.com/udacity/fullstack-nanodegree-vm.git"> VM Configuration</a>.

## Installing

### Download the VM configuration
There are a couple of different ways you can download the VM configuration.
You can download and unzip this file: <a  href="https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip">FSND-Virtual-Machine.zip</a> 
This will give you a directory called <strong>FSND-Virtual-Machine</strong>. It may be located inside your <strong>Downloads</strong> folder.
Alternately, you can use Github to fork and clone the repository <a href="https://github.com/udacity/fullstack-nanodegree-vm">VM</a>.
Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with <code>cd</code>. 
Inside, you will find another directory called <strong>vagrant</strong>. Change directory to the <strong>vagrant</strong> directory:

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58487f12_screen-shot-2016-12-07-at-13.28.31/screen-shot-2016-12-07-at-13.28.31.png">


<h3>Start the virtual machine</h3>

<p>From your terminal, inside the <strong>vagrant</strong> subdirectory, run the command <code>vagrant up</code>. 
This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) 
depending on how fast your Internet connection is.</p>

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488603_screen-shot-2016-12-07-at-13.57.50/screen-shot-2016-12-07-at-13.57.50.png">


<p>When <code>vagrant up</code> is finished running, you will get your shell prompt back. At this point, 
you can run <code>vagrant ssh</code> to log in to your newly installed Linux VM!</p>

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488962_screen-shot-2016-12-07-at-14.12.29/screen-shot-2016-12-07-at-14.12.29.png">


### Logged in!

If you are now looking at a shell prompt that starts with the word <code>vagrant</code> (as in the above screenshot), 
congratulations — you've gotten logged into your Linux VM.


## Setting up the enviroment

- _clone_ or _download_ the <a href="https://github.com/MayAlalawi/DogsCataloge.git">project </a>
- Move the folder you downloaded from GitHub and put it into the vagrant folder
- use the following line to get into the vagrant VM folder
  `$ cd /vagrant`
- Use the command line to get in to the folder you just downloaded. Then you can run this command

`$ python database_setup.py`

<br />

`$ python listofdogs.py`
<br />

- After it create the database and added items succesfully, you can run the following command
<br />

`$ python project.py`

<br />

- After finish running project.py you can use your favorite browser to visit this <a href="http://localhost:8000/">link</a>


## JSON Endpoints
<br />

`/catalog/JSON`

<br />

![screenshot_2018-09-15 screenshot](https://user-images.githubusercontent.com/36498810/45585377-63c22900-b8f4-11e8-8674-1a16c58c63a1.png)

<br />

`/catalog/<int:group_id>/JSON`

<br />

![screenshot_2018-09-15 screenshot 2](https://user-images.githubusercontent.com/36498810/45585393-91a76d80-b8f4-11e8-9a03-d14a8d9f8337.png)

<br />

`/catalog/<int:group_id>/<int:dog_id>/JSON`

<br />

![screenshot_2018-09-15 screenshot 1](https://user-images.githubusercontent.com/36498810/45585398-a5eb6a80-b8f4-11e8-8af4-12802626b685.png)


### This is the main page :
<br />

![screenshot_2018-09-15 screenshot 3](https://user-images.githubusercontent.com/36498810/45585403-bc91c180-b8f4-11e8-90f2-fbb75ee180b7.png)



## License
<p>This project is licensed under the <a href="https://github.com/MayAlalawi">MIT</a> License.</p>
