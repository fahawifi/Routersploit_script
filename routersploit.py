from routersploit.modules.scanners import autopwn
import sys
import sysgetopt
def pwn(ip_target):
    atpwn = autopwn.Exploit()
    atpwn.target = ip_target
    atpwn.run()

def run(argv):
    ip_target = ''
    auto_pwn = ''
    try:
        opts, args = getopt.getopt(argv, 'ht:a')
    except getopt.GetoptError:
        print('python3 ./routersploit -t <target>')
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print('chuong trinh ra quet lo hong router dua tren routersploit \n'
                  'python3 ./routersploit -a (autopwn) -t <target> ')
            sys.exit()
        elif opt == '-t' or opt == '--target':
            ip_target = arg
        elif opt == '-a' or opt == '--auto':
            auto_pwn = True
    if auto_pwn == True:
        print(ip_target)
        pwn(ip_target)
if __name__ == '__main__':
    run(sys.argv[1:])
