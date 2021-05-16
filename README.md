# telegramWatchdog

Watch for changes on any file in current directory  and send the last line of the file to a telegram chat using a pre-configured bot account.


## Setup

First you need [create a bot](https://core.telegram.org/bots) on Telegram and get your API KEY.

Start a chat with the boot and get the chatid by running this command:

```curl https://api.telegram.org/bot<API-KEY-HERE>/getUpdates | json_pp```

You should see something like:

```
"chat" : {
               "type" : "private",
               "username" : "username",
               "first_name" : "Your Name",
               "id" : 9398161236
```

Edit the telegram.conf file and replace it with your API-KEY and CHAT-ID


# Usage

`python3 telegramWatchdog.py`


```
usage: telegramWatchdog.py [-h] [-p P]

Watch for changes on any file in current directory and send the last line of the file to a telegram chat using a pre-configured bot account.

optional arguments:
  -h, --help  show this help message and exit
  -p P        Especify a File or Directory to watch (default: ".")
  ```
