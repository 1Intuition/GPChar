# COPYRIGHT #
#
# Copyright 2018, Teodor George Oprea, All rights reserved.
# I am not responsible for your actions.
#
# COPYRIGHT #

__version__ = "v1.3.1"
__author__ = "Intuition"
__prog__ = "python3 gpchar.py"


import os
import time
from datetime import datetime, timedelta
import argparse
from ast import literal_eval
import itertools
import sys
import string
from pathlib import Path
import copy
from timeit import default_timer as timer
import tempfile
import pyperclip


def generate(a, to, from_var=None, sure_char=None, mode:int=0):
    # modes:
    # 0 default
    # 1 noinfo
    # 2 verbose

    words_before_verbose = 1000000
    word_count = 0
    times_passed = 0

    # no surechar
    if sure_char is None:
        # no after
        if from_var is None:
            if mode != 1: print("\nWriting to file...")
            if mode != 2:
                with open(to, 'w') as file:
                    for x in itertools.product(*a):
                        file.write(''.join(map(str, x)) + "\n")
            # verbose
            else:
                with open(to, 'w') as file:
                    for x in itertools.product(*a):
                        file.write(''.join(map(str, x)) + "\n")
                        word_count += 1
                        if word_count == words_before_verbose:
                            times_passed += 1
                            word_count = 0
                            print("Written " + str(times_passed * words_before_verbose) + "th word -->", ''.join(map(str, x)))
                print("Finished!\n")

        # after
        else:
            if mode != 1: print("\nWriting to file...")
            if mode != 2:
                with open(to, 'w') as file:
                    i = (len(a) - 1)
                    while i >= 0:
                        array = list(a)
                        after_list = list(from_var)
                        after_list[i] =  list(array[i][((array[i].index(after_list[i])) + 1):])
                        r=1
                        while (r+i) < len(a):
                            after_list[i+r] = a[i+r]
                            r += 1
                        for x in itertools.product(*after_list):
                            file.write(''.join(map(str, x)) + "\n")
                        i -= 1

            # verbose
            else:
                with open(to, 'w') as file:
                    i = (len(a) - 1)
                    while i >= 0:
                        array = list(a)
                        after_list = list(from_var)
                        after_list[i] =  list(array[i][((array[i].index(after_list[i])) + 1):])
                        r=1
                        while (r+i) < len(a):
                            after_list[i+r] = a[i+r]
                            r += 1
                        for x in itertools.product(*after_list):
                            file.write(''.join(map(str, x)) + "\n")
                            word_count += 1
                            if word_count == words_before_verbose:
                                times_passed += 1
                                word_count = 0
                                print("Written " + str(times_passed * words_before_verbose) + "th word -->", ''.join(map(str, x)))
                        i -= 1
                print("Finished!\n")


    else: raise Exception('DONT USE SURECHAR')
    # # surechar
    # else:
    #     # no after with surechar
    #     if from_var is None:
    #         print("\nWriting to file...")
    #         with open(to, 'w') as file:
    #             for x in itertools.product(*a):
    #                 n = ''.join(map(str, x))
    #                 write = True
    #                 for substring in sure_char:
    #                     if substring not in n:
    #                         write = False
    #                         break
    #                 if write:
    #                     file.write(n)
    #                     file.write("\n")
    #         print("Finished!\n")


    #     # after with surechar
    #     else:
    #         print("after with surechar")


def stdout_generate(a, from_var=None, sure_char=None):

    # no surechar
    if sure_char is None:
        # no after
        if from_var is None:
            for x in itertools.product(*a): print(''.join(map(str, x)))
        # after
        else:
            i = (len(a) - 1)
            while i >= 0:
                array = list(a)
                after_list = list(from_var)
                after_list[i] =  list(array[i][((array[i].index(after_list[i])) + 1):])
                r=1
                while (r+i) < len(a):
                    after_list[i+r] = a[i+r]
                    r += 1
                for x in itertools.product(*after_list):
                    print(''.join(map(str, x)))
                i -= 1

    else: raise Exception('DONT USE SURECHAR')
    # # surechar
    # else:
    #     # no after with surechar
    #     if from_var is None:
    #         gen_iter = itertools.product(*a)
    #         for x in gen_iter:
    #             n = ''.join(map(str, x))
    #             write = True
    #             for substring in sure_char:
    #                 if substring not in n:
    #                     write = False
    #                     break
    #             if write:
    #                 print(n)


    #     # after with surechar
    #     else:
    #         isPassed = False
    #         for x in itertools.product(*a):
    #             n = ''.join(map(str, x))
    #             write = True
    #             for substring in sure_char:
    #                 if substring not in n:
    #                     write = False
    #                     break
    #             if write:
    #                 if isPassed:
    #                     print(n)
    #                 else:
    #                     if n == from_var:
    #                         isPassed = True


def test_speed_nostdout(array, no_words: int):    
    if no_words <= 1000000:
        clear_screen_with_returns()
        return "Instantly"
    else:
        print("\nCalculating estimated time... It can take up to a minute!")
        if no_words > 1000000 and no_words <= 100000000: no_words_test = 500000
        elif no_words > 100000000 and no_words <= 10000000000: no_words_test = 5000000
        else: no_words_test = 50000000
    f = tempfile.NamedTemporaryFile().name
    start = timer()
    i=0
    with open(f, 'w') as file:
        for x in itertools.product(*array):
            if i == no_words_test: break
            file.write(''.join(map(str, x)) + "\n")
            i += 1
    end = timer()
    clear_screen_with_returns()
    no_secs = round((no_words / no_words_test) * (end - start))
    return str(timedelta(seconds=no_secs))


def test_speed_stdout(array, no_words: int):
    if no_words <= 350000:
        clear_screen_with_returns()
        return "Instantly"
    else:
        if no_words > 350000 and no_words <= 35000000: no_words_test = 35000
        elif no_words > 35000000 and no_words <= 3500000000: no_words_test = 350000
        else: no_words_test = 3500000
    print("\nCalculating estimated time...")
    if no_words <= 35000000: time.sleep(1)
    else: time.sleep(2.5)
    start = timer()
    i=0
    for x in itertools.product(*array):
        if i == no_words_test: break
        print(''.join(map(str, x)))
        i += 1
    end = timer()
    clear_screen_with_returns()
    no_secs = round((no_words / no_words_test) * (end - start))
    return str(timedelta(seconds=no_secs))


def check_for_luns(n):
    if "aa" in n:
        # all chars
        n = n.replace("aa", """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'""" + string.ascii_lowercase + string.ascii_uppercase + string.digits)
    else:
        if "ll" in n:
            # all lowercase letters
            n = n.replace("ll", string.ascii_lowercase)
        if "uu" in n:
            # all uppercase letters
            n = n.replace("uu", string.ascii_uppercase)
        if "nn" in n:
            # all numbers
            n = n.replace("nn", string.digits)
        if "ss" in n:
            # all symbols
            n = n.replace("ss", """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'""")
    return list(sorted(set(n)))


def clear_screen_with_returns(n: int=25):
    for x in range(n):
        print("\n")


def query_yes_no(question, default=None):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def size_format(no_bytes):
    if no_bytes < 0:
        raise ValueError("!!! no_bytes can't be smaller than 0 !!!")
    step_to_greater_unit = 1000.
    no_bytes = float(no_bytes)
    unit = 'bytes'
    if (no_bytes / step_to_greater_unit) >= 1:
        no_bytes /= step_to_greater_unit
        unit = 'kB'
    if (no_bytes / step_to_greater_unit) >= 1:
        no_bytes /= step_to_greater_unit
        unit = 'MB'
    if (no_bytes / step_to_greater_unit) >= 1:
        no_bytes /= step_to_greater_unit
        unit = 'GB'
    if (no_bytes / step_to_greater_unit) >= 1:
        no_bytes /= step_to_greater_unit
        unit = 'TB'
    if unit == 'bytes':
        return str(int(round(no_bytes))) + ' ' + unit
    else:
        return str(round(no_bytes, 1)) + ' ' + unit


def is_surechar_valid(array, sure_char):
    raise Exception('DONT USE SURECHAR')

    # check length
    if len(''.join(sure_char)) > len(array):
        return "The length of surechar must not be higher than the length of words in wordlist."
    # check if surechars can exist individually and together
    badsurechar, whatindex = list(), list()
    for x in sure_char:
        passed2, wherepassed = list(), list()
        for i in range(len(array) - len(x), -1, -1):
            passed1 = True
            for t in range(len(x)):
                if x[t] not in array[i+t]:
                    passed1 = False
            passed2.append(passed1)
            if passed1:
                wherepassed.append(i)

        if True not in passed2:
            badsurechar.append(x)
        else:
            whatindex.append(wherepassed)
    if len(badsurechar) == 0:
        if len(sure_char) == 1:
            return True
        # dealing with overlapping
        else:
            for i in range(len(whatindex)):
                for x in range(len(whatindex[i])):
                    indexesforeach = ""
                    for y in range(len(sure_char[i])):
                        indexesforeach += str(whatindex[i][x] + y)
                    whatindex[i][x] = indexesforeach
            for x in itertools.product(*whatindex):
                if len(set(''.join(map(str, x)))) == len(array):
                    return True
            return "The surechars cannot exist together in the wordlist."
    elif len(badsurechar) > 0:
        return "The surechar {} cannot exist in the wordlist.".format(", ".join(badsurechar))


def is_afterchar_valid(array, after_char, sure_char=None):

    # check if not good len
    if len(after_char) != len(array):
        return "Cannot generate after this word because it has to have the same length as the words in wordlist."

    # no surechar
    if sure_char is None:
        # checks if each letter is possible
        for r in range(len(after_char)):
            if not list(after_char)[r] in array[r]:
                return "Cannot generate after this word because it will not be in the wordlist."
        return True


    else: raise Exception('DONT USE SURECHAR')
    # # with surechar
    # else:
    #     code pls


def get_gen_info(isStdout: bool, array, after, sure_char, full_path= None, isOverwriting: bool = False):
    
    # no surechar
    if sure_char is None:
        # no after
        if after is None:
            no_words = 1
            for i in range(len(array)):
                no_words *= len(array[i])

            if isStdout:
                ETA = test_speed_stdout(array, no_words)
                print("[GENERATE INFORMATION]")
                print("\nMode:             ", "Print to screen")
            else:
                ETA = test_speed_nostdout(array, no_words)
                print("[GENERATE INFORMATION]")
                print("\nMode:             ", "Write to file")
                print("File to generate: ", full_path)
                print("Overwriting file: ", isOverwriting)

            print("\nSurechar:         ", sure_char)
            print("After word:       ", after)
            print("\nNumber of words:  ", no_words)
            print("Length of words:  ", str(len(array)))
            print("Number of bytes:  ", size_format(no_words * (len(array) + 1)))
            print("\nEstimated time:   ", ETA)
            input("\n[PRESS ENTER TO START GENERATING]")
            
        # after
        else:
            after_list, no_words = list(after), 0
            for i in range(len(array)):
                mult = ((len(array[i])) - (array[i].index(after_list[i])) - 1)
                for x in range(1, len(array) - i):
                    mult *= len(array[x+i])
                no_words += mult

            if isStdout:
                ETA = test_speed_stdout(array, no_words)
                print("[GENERATE INFORMATION]")
                print("\nMode:             ", "Print to screen")
            else:
                ETA = test_speed_nostdout(array, no_words)
                print("[GENERATE INFORMATION]")
                print("\nMode:             ", "Write to file")
                print("File to generate: ", full_path)
                print("Overwriting file: ", isOverwriting)

            print("Surechar:         ", sure_char)
            print("After word:       ", after)
            print("\nNumber of words:  ", no_words)
            print("Length of words:  ", str(len(array)))
            print("Number of bytes:  ", size_format(no_words * (len(array) + 1)))
            print("\nEstimated time:   ", ETA)
            input("\n[PRESS ENTER TO START GENERATING]")
    


    else: raise Exception('DONT USE SURECHAR')
    # info if surechar
    # else:
    #     # no after with surechar
    #     if after is None:
    #         print("info no after with surechar")
    #     # after with surechar
    #     else:
    #         print("info after with surechar")


def main():

    parser = argparse.ArgumentParser(prog=__prog__, add_help=False)

    help_version = parser.add_mutually_exclusive_group()
    help_version.add_argument("-h", "--help", help="gives this help menu and exits", action="store_true")
    help_version.add_argument("-v", "-V", "--version", help="gives the version and exits", action="store_true")
    parser.set_defaults(dest="all")
    subs = parser.add_subparsers()

    guided_parser = subs.add_parser("guided", help="generate wordlist in user-frendly mode")
    guided_parser.add_argument("--getcmd", help="prints command and copies on clipboard instead of generate", action="store_true")
    guided_parser.set_defaults(dest="guided")

    # chars mode
    characters_parser = subs.add_parser("chars", help="generate wordlist with one command")
    c1_arg = characters_parser.add_argument("characters", help="Enter characters (visit the manuel)", metavar="<characters>", type=str)
    c2_arg = characters_parser.add_argument("path", help="Output path", metavar="<path>", type=str)
    genmode_arg = characters_parser.add_mutually_exclusive_group()
    genmode_arg.add_argument("-ni", "--noinfo", help="does not print details generating", action="store_true")
    genmode_arg.add_argument("-vv", "--verbose", help="prints details of what is happening", action="store_true")
    c5_arg = characters_parser.add_argument("-ovr", "--overwrite", help="overwrite existing file?", action="store_true")
    # c6_arg = characters_parser.add_argument("-s", "--surechar", help="all words from list will include these letters (visit the manuel)", metavar="chars", type=str)
    c7_arg = characters_parser.add_argument("-a", "--after", help="generates after this word", metavar="word", type=str)
    c8_arg = characters_parser.set_defaults(dest="chars")

    # stdout mode
    stdout_parser = subs.add_parser("stdout", help="prints to screen (can input in aircraick for example without generating a file)")
    s1_arg = stdout_parser.add_argument("characters", help="Enter characters (visit the manuel)", metavar="<characters>", type=str)
    s2_arg = stdout_parser.add_argument("-i", "--info", help="prints details before generating", action="store_true")
    # s3_arg = stdout_parser.add_argument("-s", "--surechar", help="all words from list will include these letters (visit the manuel)", metavar="chars", type=str)
    s4_arg = stdout_parser.add_argument("-a", "--after", help="generates after this word", metavar="word", type=str)
    s5_arg = stdout_parser.set_defaults(dest="stdout")

    # paramquided mode
    paramguided_parser = subs.add_parser("paramguided", help="guided mode but with some parameters entered")
    paramguided_parser.set_defaults(dest="paramguided")

    args = parser.parse_args()

    # no args
    if not len(sys.argv) > 1:
        parser.print_help()

    # help arg before mode error
    elif args.help and args.dest != "all":
        parser.error("Do not use -h/--help argument before a mode.")

    # version arg before mode error
    elif args.version and args.dest != "all":
        parser.error("Do not use -v/--version argument with a mode.")



    # chose guided mode
    elif args.dest == "guided":

        # prog info
        clear_screen_with_returns()
        print("GeneratorPerCharacter",__version__,"\n"
              "AKA: GPCHAR\n"
              "\nBy {}\n\n".format(__author__))

        # specifies the lentgh
        array, untreated_array = list(), list()
        while True:
            try:
                char = int(input("Length: "))
            except ValueError:
                print("ERROR: It must be an integer!\n")
                continue
            if char > 25:
                print("ERROR: Cannot be more than 25 characters!\n")
                continue
            break

        # sets each value in list array
        for i in range(char):
            while True:
                n = input("Character {}: ".format(i+1))
                if n != "": break
                elif n == "": print("ERROR: It cannot be empty!\n")
                else: print("UNEXPECTED ERROR...\n")
            untreated_array.append(n)
            array.append(check_for_luns(n))

        # set surechar
        sure_char = None
        # while True:
        #     sure_char = input("\nAny letter(s) you are sure (separated by commas): [leave blank if none]\n")
        #     if sure_char == "":
        #         sure_char = None
        #         break
        #     else:
        #         sure_char = sure_char.split(",")
        #         # remove break below
        #         # break
        #         if is_surechar_valid(array, sure_char) is True:
        #             break
        #         else:
        #             print(is_surechar_valid(array, sure_char))

        # set after variable
        while True:
            after_char = input("\nGenerator will start after this word: [leave blank if none]\n")
            if after_char == "":
                after_char = None
                break
            elif is_afterchar_valid(array, after_char, sure_char) is True: break
            else: print(is_afterchar_valid(array, after_char, sure_char))     

        # if stdout or not
        if query_yes_no("Do you want to generate as a STDOUT?\n(print it instead of writing it on to a file)"):
            if args.getcmd:
                cmd = stdout_parser.prog
                if after_char is not None: cmd += s4_arg.option_strings[0] + " " + after_char
                cmd += " " + '//'.join(untreated_array)
                pyperclip.copy(cmd)
                print("\n-----------------------\nThe command was copied to clipboard:\n\n" + cmd + "\n")
                exit()
            else:
                get_gen_info(True, array, after_char, sure_char, None, None)
                stdout_generate(array, after_char, sure_char)
                exit()

        # gen on file
        else:
            while True:
                gen_path = input("\nExport wordlist to this full path or relative path:\n")
                if gen_path == "":
                    print("ERROR: Enter a full path or a relative path!")
                    continue
                else:
                    if args.getcmd:
                        cmd = characters_parser.prog
                        if after_char is not None: cmd += " " + c7_arg.option_strings[0] + " " + after_char
                        cmd += " " + '//'.join(untreated_array) + " " + gen_path
                        pyperclip.copy(cmd)
                        print("\n-----------------------\nThe command was copied to clipboard:\n\n" + cmd + "\n")
                        exit()
                    elif Path(gen_path).is_file():
                        override_question = "Do you want to overwrite the file {} ?".format(gen_path)
                        if query_yes_no(str(override_question)):
                            get_gen_info(False, array, after_char, sure_char, os.path.abspath(gen_path), True)
                            generate(array, gen_path, after_char, sure_char)
                            break
                        else:
                            continue
                    else:
                        try:
                            get_gen_info(False, array, after_char, sure_char, os.path.abspath(gen_path), False)
                            generate(array, gen_path, after_char, sure_char)
                            break
                        except IOError:
                            print("ERROR: File cannot be created! Please verify the path.")
            exit("Thank you for using GPCHAR!\n")


    # chose chars mode
    elif args.dest == "chars":
        # modes
        if args.noinfo: gen_mode = 1
        elif args.verbose:  gen_mode = 2
        else:  gen_mode = 0
        # treat array
        array, surechar = list(), None
        for i in args.characters.split("//"):
            if i == '': exit("ERROR: Cannot have zero characters in one position!\n")
            array.append(check_for_luns(i))
        # after format
        if args.after is not None:
            if is_afterchar_valid(array, args.after, surechar) is not True:
                exit("ERROR: " + is_afterchar_valid(array, args.after, surechar) + "\n")
        # generate
        if Path(args.path).is_file():
            if args.overwrite:
                if not args.noinfo:
                    get_gen_info(False, array, args.after, surechar, os.path.abspath(args.path), True)
                generate(array, args.path, args.after, surechar, gen_mode)
                exit("Thank you for using GPCHAR!\n")
            else:
                exit("ERROR: " + os.path.abspath(args.path) + " is already a file! To overwrite is put the --overwrite argument.")
        else:
            if not args.noinfo:
                get_gen_info(False, array, args.after, surechar, os.path.abspath(args.path), False)
            try:
                generate(array, args.path, args.after, surechar, gen_mode)
            except IOError:
                exit("ERROR: File cannot be created! Please verify the path.")
            exit("Thank you for using GPCHAR!\n")


    # chose stdout mode
    elif args.dest == "stdout":
        # treat array
        array, surechar = list(), None
        for i in args.characters.split("//"):
            if i == '': exit("ERROR: Cannot have zero characters in one position!\n")
            array.append(check_for_luns(i))
        # after format
        if args.after is not None:
            if is_afterchar_valid(array, args.after, surechar) is not True:
                exit("ERROR: " + is_afterchar_valid(array, args.after, surechar) + "\n")
        # generate
        if args.info:
            get_gen_info(True, array, args.after, surechar)
        stdout_generate(array, args.after, surechar)
        exit()


    # chose paramguided mode
    elif args.dest == "paramguided":
        print("paramguided mode")



    # help arg
    elif args.help and args.dest == "all":
        parser.print_help()

    # version arg
    elif args.version and args.dest == "all":
        print("GPCHAR", __version__)

    # other unknown errors
    else:
        parser.error("Unknown parser error...")


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nQuitting GPChar...\n")
        exit()
    
