import scan
import search
import compare
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--print', type=str, default = 't', help='Print soft list')
parser.add_argument('-s', '--save', type=str, default = 'f', help='save results or not')
parser.add_argument('-f', '--file', type=str, default = '', help='file name')
parser.add_argument('-c', '--compare', type=str, default = 'f', help='compare results')
parser.add_argument('--full', type=str, default = 'f', help="find / -perm /111")
parser.add_argument('-sr', '--search', type=str, nargs='+', default = '', help="search")


if parser.parse_args().print == 't':
    scan.print_soft()

if parser.parse_args().save == 't':
    if parser.parse_args().file != '':
        scan.scan_save(filename = parser.parse_args().file)
    else:
        scan.scan_save()

if parser.parse_args().search != '':
    search.soft_search(search_args = parser.parse_args().search)

if parser.parse_args().compare == 't':
    if parser.parse_args().file != '':
        compare.compare(last_scan_file = parser.parse_args().file )
    else:
        compare.compare()

if parser.parse_args().full == 't':
    scan.get_full_list()