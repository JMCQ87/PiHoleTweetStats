# tweetStats

Send a daily tweet with your Pi-Hole statistics!

## How to use

1. `git clone https://github.com/mwoolweaver/tweetStats.git`
2. Install Python 3
3. `pip3 install -U -r requirements.txt`
4. Copy `config.ini.example` to `config.ini` and adjust it `cp config.ini.example config.ini`
   - `api_path` = Path to your `/admin/api.php` of Pi-Hole
   - Tokens: Create an application [here](https://apps.twitter.com/)
5. Run it!
6. ???
7. Profit

## Cronjob

This will tweet your stats at 23:59 everyday and redirects output to /dev/null:

```
59 23 * * * python3 /path/to/pihole_tweeter.py >/dev/null 2>&1
```

# What Does It Mean

 * 🚫🌐 = domains_being_blocked
 * 🈵⁉️  = dns_queries_today
 * 📢🚫 = ads_blocked_today && ads_percentage_today
 * ⁉️⏭  = queries_forwarded
 * ⁉️💾  = queries_cached
 * 🦄🙈 = unique_clients
 * 🔐🎚️ = privacy_level
 * 🆙⏳ = uptime
 * ⚖️x̅  = loadavg
 * 🐏📈 = psutil.virtual_memory()[2] && psutil.virtual_memory()[3] && psutil.virtual_memory()[1]
 * 🔗📡 = netifaces.interfaces()
 * 🐧🌽 = platform.platform
