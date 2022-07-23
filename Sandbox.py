#!/usr/bin/python3
# —*— coding:UTF-8 -*-

import argparse
from util.color import *
from modules.threatbook_modules import Threatbook


banner = red + '''

~|~|_   _   |-|\ _ |- _  _|-.  ,_
 | |||`(/_(||_|/(/_|_(/_(_|_|()|| by k1p2y3
''' + end

if __name__ == '__main__':
    print(banner)
    parser = argparse.ArgumentParser(
        usage='sandbox --tb -f filename or path',
        description="Sandbox detection tool ",
    )
    engine = parser.add_argument_group('sandbox')
    engine.add_argument("--tb", dest="threatbook", action="store_true",
                        help="Using threatbook sandbox")
    engine.add_argument("--qax", dest="qax", action="store_true",
                        help="Using qax sandbox")
    engine.add_argument("--360", dest="360", action="store_true",
                        help="Using 360 sandbox")
    engine.add_argument("--vt", dest="VirusTotal", action="store_true",
                        help="Using VirusTotal sandbox")

    misc = parser.add_argument_group('MISC')
    misc.add_argument("-f", dest="file",
                      help="filename")
    misc.add_argument("-fh", dest="hash",
                      help="file hash")
                      
    args = parser.parse_args()
    
    if args.threatbook:
        s = Threatbook(args.file)
        s.login()
        s.check_file()