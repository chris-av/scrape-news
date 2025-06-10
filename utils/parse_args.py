import json
from utils.headers import get_random_user_agent


def extract_args(args: list[str]) -> dict:
    # default config
    config = {
        "link": "",
        "headers": {
            'User-Agent': pick_header(),
            'Connection': 'keep-alive',
        },
        "max-w": 80,
        "padding": 5
    }

    for indx, arg in enumerate(args):
        try:
            if indx == 0 and ("https" in arg.lower()):
                link = args[indx]
                config["link"] = link
        except Exception as e:
            print("did not supply a valid link")
            raise(e)


        # headers
        if arg == "-h":
            try:
                print(arg, args[indx+1])
                headers_str = args[indx+1]
                headers = json.loads(headers_str)
                config["headers"] = headers
            except Exception as e:
                print("did not supply a valid -h argument")
                raise(e)

        # headers path
        if arg == "-t":
            try:
                print(arg, args[indx+1])
                headers_path = args[indx+1]
                f = open(headers_path)
                headers = json.load(f)
                f.close()
                config["headers"] = headers
            except Exception as e:
                print("did not supply a valid -t argument")
                raise(e)

        # padding
        if arg == "-p":
            try:
                print(arg, args[indx+1])
                config["padding"] = int(args[indx+1])
            except Exception as e:
                print("did not supply a valid -p argument")
                raise(e)

        # width
        if arg == "-w":
            try:
                print(arg, args[indx+1])
                config["max-w"] = int(args[indx+1])
            except Exception as e:
                print("did not supply a valid -w argument")
                raise(e)

    return config

