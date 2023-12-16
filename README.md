# cflare-ddns

This is yet another Cloudflare Dynamic DNS application.

## Installation

```shell
pip install cflare-ddns
```

## Usage

First is you need to create a config file. You can place it in the default location `/etc/cflare-ddns.json` or anywhere in your filesystem that is readable by the script. You'll need to pass that config location in the cli if it's not the default location.

Edit the config file, you'll need to provide the following:

- `api_key` - You can get this through this [link](https://developers.cloudflare.com/fundamentals/api/get-started/keys/).
- `email` - The email account you use in cloudflare.
- `zone_id` - [Zone ID](https://developers.cloudflare.com/fundamentals/setup/find-account-and-zone-ids/) of your domain name.
- `domain` - The domain name. Example: `example.com`
- `record_name` - The sub domain you want to update with your public ip. This subdomain should be an `A` record type. Example: `www`

### Configuration file example

```json
{
  "api_key": "xxxx",
  "email": "xxxx@gmail.com",
  "records": [
    {
      "zone_id": "xxxx",
      "domain": "example.xyz",
      "record_name": "vpn"
    },
    {
      "zone_id": "xxxx",
      "domain": "example.sh",
      "record_name": "www"
    }
  ]
}
```

## CLI Reference

```shell
usage: cflare-ddns [-h] [-c CONFIG_FILE] [-i INTERVAL] [-v]

options:
  -h, --help            show this help message and exit
  -c CONFIG_FILE, --config CONFIG_FILE
                        Path to your configuration file. Default paths: /etc/cflare-ddns.json,
                        cflare-ddns.json
  -i INTERVAL, --interval INTERVAL
                        Number of seconds between each sync. This will make the program run
                        forever.Hit Ctrl-C to stop.
  -v, --version         App version
```
