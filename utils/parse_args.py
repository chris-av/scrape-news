import json
import random


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


def pick_header():
    headers_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    ]
    rand_int = random.randint(0, len(headers_list)-1)
    print(f"getting header: {rand_int} / {len(headers_list)}")
    use_header = headers_list[rand_int]
    print(f"using header : {use_header}")
    return use_header

