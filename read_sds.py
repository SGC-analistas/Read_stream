import argparse
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
from obspy import read
from colorama.ansi import Fore,Style

DEFAULT_VAL = {"sds":"/mnt/sc232","network":None,
                "station":None,"location":None,"channel":None,
                "starttime":None,"endtime":None, "plot":None,
                "save":None}

def read_args():
    prefix = "+"
    ini_msg = "#"*120

    parser = argparse.ArgumentParser("Plot streams. ",prefix_chars=prefix,
                         usage=f'Plot streams.')

    parser.add_argument(prefix+"sds",prefix*2+"sds",
                        type=str,
                        default=DEFAULT_VAL["sds"],
                        help="ejemplo: /mnt/sc232",
                        metavar='')

    parser.add_argument(prefix+"net",prefix*2+"network",
                        metavar='', default=DEFAULT_VAL["network"],
                        type=str,
                        help="network", required=True)

    parser.add_argument(prefix+"sta",prefix*2+"station",
                        metavar='', default=DEFAULT_VAL["station"],
                        type=str,
                        help="station '*'->todos", required=True)

    parser.add_argument(prefix+"loc",prefix*2+"location",
                        metavar='', default=DEFAULT_VAL["location"],
                        type=str,
                        help="location '*'->todos", required=True)
    
    parser.add_argument(prefix+"cha",prefix*2+"channel",
                        metavar='', default=DEFAULT_VAL["channel"],
                        type=str,
                        help="channel '*'->todos", required=True)

    parser.add_argument(prefix+"start",prefix*2+"starttime",
                        metavar='', default=DEFAULT_VAL["starttime"],
                        type=str,
                        help="Tiempo inicial YYYYmmddTHHMMSS", required=True)

    parser.add_argument(prefix+"end",prefix*2+"endtime",
                        metavar='', default=DEFAULT_VAL["endtime"],
                        type=str,
                        help="Tiempo final YYYYmmddTHHMMSS", required=True)

    parser.add_argument(prefix+"p",prefix*2+"plot",
                        metavar='', default=DEFAULT_VAL["plot"],
                        type=str,
                        help="true or false")

    parser.add_argument(prefix+"s",prefix*2+"save",
                        metavar='', default=DEFAULT_VAL["save"],
                        type=str,
                        help="meed path")

    args = parser.parse_args()
    return args


def read_st(sds,net,sta,loc,cha,start,end,
            plot=False,save=None):
    client = Client(sds)
    print(net,sta,loc,cha,
                UTCDateTime(start) ,UTCDateTime(end))
    st = client.get_waveforms(net,sta,loc,cha,
                UTCDateTime(start) ,UTCDateTime(end))
    print(st)
    if plot in (True,"true","True","TRUE"):
        st.plot()
    if save not in (None, "None"):
        st.write(save, format="MSEED") 
    return st



if __name__ == "__main__":
    try:
        args = read_args()
        read_st(args.sds,args.network,args.station,args.location,
                    args.channel,args.starttime,args.endtime,
                    args.plot,args.save)
    except:
        print(Fore.RED+"Ejemplo : python read.py +net CM +sta BAR2 +loc '*' +cha '*' +start 20210701T000000 +end 20210701T020000 +s ext.mseed"+Style.RESET_ALL)