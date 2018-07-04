# call-history

## Description
Lightweight web service that registers and lists outgoing and incoming VoIP calls from a Mitrastar HGU GPT-2541GNAC device.

Written in Python and powered by [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/), [Pandas](https://pandas.pydata.org/), [SQLite](https://www.sqlite.org/) and [Bottle](https://bottlepy.org/).

## Contents
- `systemd/`: unit files for systemd.
- `template/`: page template for bottle.
- `app.py`: bottle HTTP service script.
- `call_history.py`: call history update script.
  - Requires a `.passwd` file containing the HGU password.
  - Stores data in a SQLite database `call_history.db`.
- `LICENSE`: license file.
- `README.md`: this file.
- `requirements.txt`: requirements file for `pip`.

## License
- Code licensed under GNU General Public License v3.0.
- Template: Copyright (c) 2017 by [Nikhil Krishnan](http://codepen.io/nikhil8krishnan/pen/WvYPvv).
