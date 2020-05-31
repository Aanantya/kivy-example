## Kivy/Kivymd - Buildozer Android Application

### Getting Started

To me, installing kivy/kivymd and working on it is super easy while using pycharm IDE.
All I had to do was install kivy/kivymd packages and import them straight into the program.

For installing or downloading kivy and it's dependencies one can follow the instructions given at kivy official [site](https://kivy.org/#download) 


Now moving ahead, I had shared 3 super simple example kivy/kivymd programs for testing and running as an android application.


Once you get them running, go ahead and install [buildozer](https://kivy.org/doc/stable/guide/packaging-android.html)

### Working with buildozer 

After you complete installing Buildozer, create an empty folder.

Open the terminal in that folder and run the following command 
```
$buildozer init
```
It will generate a *buildozer.spec* file. Open the file and make changes into the file such as 

* title
* package.name (Make sure you change the package name everytime you build apk in the same folder)
* requirements (Please make sure to add your project requirements here separated via comma. For those who are intrested in using kivymd, add these additional requirements 

``` 
requirements = python3,kivy,git+https://github.com/HeaTTheatR/KivyMD.git,pillow,pygments,android
```

* If you are intrested in adding your own logo or the splash screen to your app, remove the commented lines in *buildozer.spec* file. 

```
# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

```
**Example:**
Add the *presplash.png* and *icon.png* files to your app folder

```
# (str) Presplash of the application
presplash.filename = %(source.dir)s/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

```

If you want, you may customize your app by making more such changes to the *buildozer.spec* file.
When you are ready to build the apk, connect your device in USB debugging mode and run the following command 

'''
buildozer android debug deploy run
'''

It will take sometime to build the apk. The apk will be running directly into your device on successful build. 

You can also share the .apk file generated into the bin folder of app directory. 

To see the status of your app running in your device, run the following command on your system terminal

```
$adb logcat | grep python
```

