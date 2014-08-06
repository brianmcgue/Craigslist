# Craigslist Scraper Thing (for Mac)

So you'll need quite a few things to get this working.  I'll try to make this
as 'user friendly' as possible, but I can't make any promises that it will
be great.  Let me know if anything is confusing.

## Get pip

Everything should be at [this link](http://pip.readthedocs.org/en/latest/installing.html),
but I'll reiterate here.  Open up Terminal and run these commands:

```sh
cd ~/ # This isn't really necessary
curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
python get-pip.py
```

This *should* install pip properly.  Oh, if you were wondering, pip apparently
stands for ['Pip installs python'](http://esmithy.net/2012/08/25/python-packaging-demystified/).
Clever.

## You *should* have the Ruby Gem installer on your computer

To test this, run :

```sh
gem search ^rails$
```

Hopefully you'll see something along the lines of:

```sh
*** REMOTE GEMS ***

rails (4.1.4)
```

Good? Good.

## Now you can actually install the two things you need

For BeautifulSoup (you'll need to enter in the root user password):

```sh
sudo pip install beautifulsoup4
```

This will take HTML and parse it so we can scrape what we want.

For Terminal-Notifier (again, the password):

```sh
sudo gem install terminal-notifier
```

This will make it so you can get Mac Notifications

## No GitHub account? No problem

This will give you the simple file to scrape craigslist.

```sh
curl https://raw.githubusercontent.com/brianmcgue/Craigslist/master/craigslist.py > craigslist.py
```

Here's the tricky part though. You'll need to open that file up in a text editor
and replace the url with you main search url.

So head on over to [craigslist](http://www.craigslist.org/).
Fill out the exact search that you would continually go to every 20 minutes or
so if you had the time.  Then copy the url, open `craigslist.py` in a text editor,
and replace the `mainSearch` url with your custom url.

## Another tricky part: creating a cron job

Cron jobs are great.  They are tasks that you ask your computer to run every set
amount of time, which you get to decide.  I've just made it 20 minutes. You'll
need the output from these commands

```sh
which python
# => /Library/Frameworks/Python.framework/Versions/2.7/bin/python
pwd
# => /Users/brianmcgue 
```

So in Terminal type `crontab -e`, then KEEP READING BEFORE YOU TYPE ANYTHING ELSE.

This will open your crontab (file that holds all cron jobs) to edit.  It will open
the file in vim.  If you don't know how to use vim, it's a living hell.  If you do,
good for you I guess.

Press `i`.  Then copy and paste this, filling in the correct names:

```sh
*/20 * * * * which_python_output pwd_output/craigslist.py
```

For me, this would be:

```sh
*/20 * * * * /Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/brianmcgue/craigslist.py
```

* Note: you will not be able to use your cursor in vim, just your keyboard.

Then press the `esc` key, and type `:wq` before hitting enter.

Hopefully the terminal will say `crontab: installing new crontab`

Then you're done.

## Stopping the search

All you need to do is go into your crontab, `crontab -e`, press `dd`, then press
`:wq` and hit enter.  All *should* be fine after that.

## Not done

I realize this is terrible, and I'll plan to make it better sometime in the near
future.  Hopefully all you'll have to do is run one script and everything will
magically happen.
