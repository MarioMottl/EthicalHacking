import pyfiglet
import sys
import socket
from datetime import datetime
import progressbar
from multiprocessing import Pool
from multiprocessing import freeze_support

bar = progressbar.ProgressBar(max_value=int(sys.argv[3]))

'''Define function to run mutiple processors and pool the results together'''
def run_multiprocessing(func, i, n_processors):
    with Pool(processes=n_processors) as pool:
        return pool.map(func, i)

def portscanner(port):

    target = socket.gethostbyname(sys.argv[1])

    try:
        bar.update(port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()

    except KeyboardInterrupt:
            print("\n KeyboardInterrupt.")
            sys.exit()
    except socket.gaierror:
            print("\n Hostname couldnt be resolved.")
            sys.exit()
    except socket.error:
            print("\n Server is not responding.")
            sys.exit()

def main():
    if len(sys.argv) == 4:
        ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
        print(ascii_banner)
        num_max = int(sys.argv[3])
        n_processors =4
        x_ls = list(range(num_max))
        out = run_multiprocessing(portscanner, x_ls, n_processors)


if __name__ == "__main__":
    freeze_support()   # required to use multiprocessing
    main()