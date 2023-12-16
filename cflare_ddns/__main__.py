import sys
from importlib.metadata import version
from cflare_ddns.main import main
from cflare_ddns.args import init


if __name__ == "__main__":
    args_parse = init()
    args = args_parse.parse_args()
    if args.version:
        print(version("cflare-ddns"))
        sys.exit(0)
    if args.config_file is None:
        print("Please specify config file")
        sys.exit(1)
    main(args)
