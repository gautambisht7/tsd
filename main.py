from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.list import MDList,OneLineAvatarListItem,ImageLeftWidget
import time
import pygame.camera
import pygame.image
import sys



def captureyouface():


 pygame.camera.init()

 cameras = pygame.camera.list_cameras()
 webcam = pygame.camera.Camera(cameras[0])
 webcam.start()
 img = webcam.get_image()
 pygame.image.save(img,"filename.jpg")

class MyApp(MDApp):
   captureyouface()

if __name__ == "__main__":
	MyApp().run()

