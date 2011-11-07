__ License __

This bunch of files is licensed with GNU GPLv3. See LICENSE.txt for details.

Some parts of it are not covered by GPL. Files and parts of files that are not include text claiming that.

__ Credits __

- Software is mainly put together by Henri Holopainen. 
- Physical installation was done by Olli Jarva and Hanno Nevanlinna
- Bus/taxi screen layout was done by Iiro Isotalo and Timo Sulanne

__ Background __

In Futurice Ltd Helsinki office lobby we have taxi post with large button for ordering taxi to front door.
That system was built and programmed before our annual party, so it's a quick hack. It's not production
ready software.

__ Quick HOWTO __

Read all the code. It won't run without modifications. At least API keys and serial ports must be changed.

1) Connect button to Arduino, upload button.pde from arduino subdirectory.
2) Install kannel
3) Install mobile broadband USB stick
4) Edit kannel.conf and taxi-daemon.py
5) Start taxi-daemon.py
6) (Re)start kannel
7) Install apache2 and php5 module for apache2
8) Edit var/www/bus_display/script.js and index.html. At least API keys for weatherbug and HSL are missing. Add your own logo.
9) Start chrome with parameter --no-web-security and open var/www/bus_display/
10) Debug.

Feel free to contact <olli.jarva@futurice.com> if you have some problems. I'll try to answer, but I
can't make any promises on that matter.
