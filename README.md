# monitor-canada-interest-to-sponsor

This script sends an email for any difference occurred on the Interest to Sponsor Form of the Canadian government website.

This helps anyone who wants to sponsor the parents or grandparents knows the availability of the application.

1. copy `config-sample.ini` to `config.ini` and change the `Email` config
2. Set a cronjob with `python3 fetch.py`
