# HSR Achievement Scanner
This is an Achievement Scanner for Honkai: Star Rail.
It is very, very inspired from [kel-z/HSRScanner](https://github.com/kel-z/HSR-Scanner).
It uses a virtual controller to navigate through the menus, and is able to upload the
achievements to the best tracker for them around, [stardb.gg](https://stardb.gg).

## Running
With the OneFile version, just click on the .exe.
With the OneDir version, unzip then launch the exe in the extracted folder.

The first time running, it may ask you to install the ViGEmBus driver.
This is what allows this project to emulate a controller. 

DO NOT MOVE THE MOUSE OR TOUCH THE KEYBOARD WHILE IT IS RUNNING,
as HSR will go back to keyboard+mouse mode, and the current scan *might* break!

To stop the scanner while it is running, you have to press Alt+Tab.

### If you want to upload the achievements to stardb, do the following:
Go and retrieve your cookie from stardb (you need to be logged in). You can do either one of these methods, or other if you know how:
* For that, open the developer menu by pressing F12 in the tracker and go the network tab, then check and uncheck an achievement.
You now see an achievement at the bottom. Click on it and scroll down until you see `Cookie: _____`.
Copy the value in it following `id:`.
* On Chrome, open the developer menu by pressing F12 and go to the Application tab.
In the left, expand cookies and click on `https://stardb.gg`. In the right panel, click on `id` and copy its value below.
* On Firefox, open the developer menu by pressing F12 and go to the Storage tab.
In the left, expand cookies and click on `https://stardb.gg`.In the right panel, click on `id`.
Then on the new panel that opened, right click on `id` and click copy. When pasting, remove at the beginning: `id :"` and at the end `"`.

Copy that value and paste it in the scanner.

The achievements get saved in a file. If they ever add a function to import them,
you will also be able to just put that file on there, no need for the cookie.

## Acknowledgements
* [kel-z/HSRScanner](https://github.com/kel-z/HSR-Scanner) for providing me the code base and the UI for this project.
* [Dimbreath/StarRailData](https://github.com/Dimbreath/StarRailData) for the data.
* The epic people at [stardb.gg](https://stardb.gg) for the best achievement tracker website.
* The awesome packages I used, such as `vgamepad`.
