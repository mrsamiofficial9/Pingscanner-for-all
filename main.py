import ping3
from colorama import Fore, Back, Style, init

init(autoreset=True)

def create_ascii_banner():
    banner = r"""
     ____  _  _  ____  _  _  ____  ____    __   _  _  _  _  ____  __     ____  __  __ _  _  _  ____  __ _  ____ 
    (  _ \( \/ )(  _ \( \/ )(  _ \(_  _)  / _\ ( \/ )( \/ )(  _ \(  )   / ___)/  \(  ( \( \/ )(  _ \ (  ( \(  __)
     )   / \  /  )   / )  (  )   /  )(   /    \/ \/  )  (  ) __/ )(__   \___ \\  O ))    /  ) __/ /    / ) _) 
    (_)\_) (__) (__)  (__/  (__) (__)  \_/\_/\_/\_/   (__)(__)   (____)  (____/ \__/(__\_)(__)  (__)  (__)  (____)
    """

    return banner

def ping(host):
    pinger = ping3.Ping()
    response_time = pinger.ping(host)

    if response_time is not None:
        response_str = f'{Fore.GREEN}Response from {host}: time={response_time} ms'
    else:
        response_str = f'{Fore.RED}No response from {host}'

    return response_str

if __name__ == "__main__":
    banner = create_ascii_banner()
    print(Back.BLUE + Fore.WHITE + banner)
    host = input(Fore.YELLOW + "Enter the hostname or IP address to ping: ")

    response_str = ping(host)
    print(response_str)
