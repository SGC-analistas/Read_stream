import argparse
from obspy import read
from colorama.ansi import Fore,Style


DEFAULT_VAL = {"file":None,"plot":None}

def read_args():
    prefix = "+"
    ini_msg = "#"*120

    parser = argparse.ArgumentParser("Plot local streams. ",prefix_chars=prefix,
                         usage=f'Plot local streams.')

    parser.add_argument(prefix+"f",prefix*2+"file",
                        metavar='', default=DEFAULT_VAL["file"],
                        type=str,
                        help="true or false",required=True)
    
    parser.add_argument(prefix+"p",prefix*2+"plot",
                        metavar='', default=DEFAULT_VAL["plot"],
                        type=str,
                        help="true or false")

    args = parser.parse_args()
    return args


def read_local_st(mseed,plot=False):
    st = read(mseed)
    print(st)
    if plot in (True,"true","True","TRUE"):
        st.plot()
    return st

if __name__ == "__main__":
    try:
        args = read_args()
        read_local_st(args.file, args.plot)
    except:
        print(Fore.RED+"Ejemplo : python read.py +f ext.mseed"+Style.RESET_ALL)