<img src="https://i.ibb.co/Jn4Nyqf/cool.png" width="300" height="225">

# P-Game (◠﹏◠)

Hi! Do you know what to do here? Yes exactly, no one knows here too. But that's the fun part of this project. We're making a game and when it's finished it's should be **at least playable**.
No one knows what's gonna happen and actually, no one cares. Just don't mess the project way too much and keep your codes clean huh?

# Files

As I was said we have to keep our code clean. But we also have to keep our directory clean. Here are some instructions on what to do when to do.

## A new python dependency

If you are going to depend on another dependency that is not yet depended on. Don't forget to add it to "**requirements.txt**".

## A different folder for a different cause

In this project, every folder has its own purpose. First things first we have four different folders in our main directory one is for **client side** and one is for **server side**.
and you can guess what's other ones for.

### Server

In our server side, we have our game manager. This will have Socket.IO communication with our client side and will manage the game users. Also why not we create a real-time text chat? That could be great. File extension ".py" is accepted by default. Other files extension that allowed will be taken from "extensions.txt" in the same folder.

### Client

All files here will be static and there won't be any server-side executed files. These files will be served to the client by our web server over https. Files here will have extension either of ".html, .js, .css, .jpg, .png, .gif, .mp3, .ogg".
All extensions are case insensitive.

### Tests

All tests belong here. There is no extension restriction or anything. Actually, our deployment server ignores this folder anyway.

### Tools

This folder includes some tools that you can use in your development. This folder is also ignored by the deployment server.

### Deployment (Not in this repository)

Also, we have a lot of things going on in our deployment server that waits for you to push some code then deploy it to live game server. But because of some reasons (!), those are in a different repository. Check here: [Deployment Github Repository](https://github.com/Nycrera/Deployment-pgame)

# Deploying

You had written some code, executed your tests and here you are pushing your commits.
(For god's sake please execute your tests before push !)

Thank you for your hard work and now you have to wait for some time before our servers check your code and get everything ready. From this point everything is automated.
Our servers checks code then checks if any new requirement exists. And then our server messages currently running old game server to alert and shut down.

- Deployment server will sync all folders with proper folders in our live game server.
  > You just have to push to this repository. Also, you can do this manually with deploy.py in the tools folder

# Database (MySQL)

For now, in our DB we only have a table for users but this is expected to extend with time.
You can view database design in dbdesign.png and you can see the MySQL create script as pgame_mysql_create.sql
