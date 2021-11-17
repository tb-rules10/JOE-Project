# Installing ‘Motion’ in Raspberry Pi for Video feed

Motion Software is free, open-source motion detector CCTV software, developed for Linux. It can process images from many different types of cameras. Motion software can monitor video from more than one camera, and it can detect a change in the picture. With the help of Motion software, you can change your Raspberry pi into a CCTV surveillance camera that can detect the motion and send alerts. Motion software can also be used to get the live video feed on a Webpage.

- Before installing the Motion, first, update your Raspberry Pi OS using the following command:

     `sudo apt-get update`

- After that, install the Motion using the below command:

     `sudo apt-get install motion`

- Now navigate to the /etc/default/motion file to set Motion daemon to yes so that it will always be running. Use the below command to edit the file:

     `sudo nano /etc/default/motion`

![image](https://user-images.githubusercontent.com/58645688/142214432-120a1455-8afb-464d-9f5f-096270d918ad.png)
Then press CTRL+X > ‘Y’ > Enter to save the file.

Now, use the below command to set the permission for the motion Directory (/var/lib/motion/), where it saves all the Video recordings and picture files.

`sudo chown motion:motion /var/lib/motion/`
 

Now in this final step, turn off the localhost inside the motion configuration file to access the video feed outside the Raspberry Pi on the same network. To turn off the localhost, use the following command:

`sudo nano /etc/motion/motion.conf`
You can use the ctrl+W to search for a specific word inside the nano editor.

![image](https://user-images.githubusercontent.com/58645688/142214732-8b4766a7-7aff-4eaf-9424-939ba9192d57.png)
Now to check the video feed, start the motion using the below command:

`sudo /etc/init.d/motion restart`
 

After that, open the video feed page using your Pi’s IP address with port 8081 (192.168.1.207:8081).

## Installing Flask in Raspberry Pi

After Motion, now install Flask to create a Web Server to control the robot.

The webpage to control the Robot will be created using Flask Web Framework. The webpage will have controls to move the robot in left, right, forward, and backward. In IoT based applications, Webservers are used to control or monitor any sensor values using web browsers, we previously created many webservers using Arduino, ESP8266, NodeMCU, ESP32, Raspberry Pi, etc.

Use the below command to install the Flask:

`pip install Flask`

