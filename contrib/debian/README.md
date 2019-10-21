
Debian
====================
This directory contains files used to package diytubed/diytube-qt
for Debian-based Linux systems. If you compile diytubed/diytube-qt yourself, there are some useful files here.

## diytube: URI support ##


diytube-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install diytube-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your diytubeqt binary to `/usr/bin`
and the `../../share/pixmaps/diytube128.png` to `/usr/share/pixmaps`

diytube-qt.protocol (KDE)

