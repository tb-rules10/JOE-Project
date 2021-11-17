# Pi Camera:
![image](https://user-images.githubusercontent.com/58645688/142211948-515f33a8-6cb9-40e0-bf97-ad5149f9645e.png)
---------------------------------------------------------------------------------------------
1. To use pi-camera with Raspberry Pi, first enable camera interfacing from raspi-config. For it, run the sudo raspi-config and select Interfacing options.

![image](https://user-images.githubusercontent.com/58645688/142212052-0fcda440-a077-49aa-a7e3-96e457f5dbe8.png)

2. Then select the Camera option and Enable it on the next window and reboot the Pi.

![image](https://user-images.githubusercontent.com/58645688/142212309-90fc8406-732a-4c4e-9528-6767cf719a17.png)

3. Now to test the camera, use the below command to capture a photo.
` raspistill -o image.jpg`

### If you get an image in Pi directory, then you are ready to go else check your camera strip and camera module.
