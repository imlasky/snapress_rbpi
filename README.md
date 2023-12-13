# snapress

snapress is a way to share photos in person instead of online

run this code on linux

---

## instructions (raspberry pi)

1. if you're using a raspberry pi, get that setup [[instructions](https://www.raspberrypi.com/documentation/computers/getting-started.html#install-using-imager)]
2. once you reach the settings page (below), click "Edit Settings" and do the following:
    * keep the raspberry.local
    * set the username and password (i'll be using *snapress* for the username for the rest of this)
    * add your wifi (if you have the nano, it has to be the 2.4ghz since it doesn't support 5g)
    * click select locale settings

![settings page](./img/rbpi_settings_page.png)

3. put the sd card into the raspberry pi and plug the raspberry pi in for power (its on when the green light stops blinking)
4. on your computer type `git clone https://github.com/imlasky/snapress_rbpi.git`
5. then type `cd snapress_rbpi`
6. then `chmod +x install_and_run.sh`
7. then `chmod +x run_script.sh`
8. then `./install_and_run.sh`

At this point your raspberry pi should be set up and able to print to your local printer. 

Feel free to [email me](mailto:ian@snapress.com?subject="setup help") if you run into issues or open an issue above!
