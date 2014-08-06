# Craigslist Scraper Thing

So you'll need quite a few things to get this working.  I'll try to make this
as 'user friendly' as possible, but I can't make any promises that it will
be great.  Let me know if anything is confusing.

## Get pip

Everything should be at [this link](http://pip.readthedocs.org/en/latest/installing.html),
but I'll reiterate here.  If you're using a Mac, open up Terminal and run these commands:

```sh
cd ~/ # This isn't really necessary
curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
python get-pip.py
```

This *should* install pip properly.  Oh, if you were wondering, pip apparently
stands for ['Pip installs python'](http://esmithy.net/2012/08/25/python-packaging-demystified/).
Clever.

Ok, now that pip is installed, you can install other things.

## You *should* have the Ruby Gem installer on your computer (if you have a Mac)

To test this, run :

```sh
gem search ^rails$
```

Hopefully you'll see something along the lines of:

```sh
*** REMOTE GEMS ***

rails (4.1.4)
```
