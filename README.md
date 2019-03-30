# call-history

## Description
Lightweight web service that registers and lists outgoing and incoming VoIP calls from a Mitrastar HGU GPT-2541GNAC device.

Written in Python and powered by [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/), [Pandas](https://pandas.pydata.org/), [SQLite](https://www.sqlite.org/), [Bottle](https://bottlepy.org/) and [Bootstrap](https://getbootstrap.com/).

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
