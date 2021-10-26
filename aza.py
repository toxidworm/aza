import argparse
import base64
import os
import binascii
from colorama import Fore, Back, Style, init
if os.name == 'nt':
	init()
	os.system("cls")
else:
	os.system("clear")
print(f"""{Fore.CYAN}
    _              ___                       _           
   /_\\   _____ _  | __|_ _  __ _ _ _  _ _ __| |_ ___ _ _ 
  / _ \\ |_ / _` | | _|| ' \\/ _| '_| || | '_ \\  _/ _ \\ '_|
 /_/ \\_\\/__\\__,_| |___|_||_\\__|_|  \\_, | .__/\\__\\___/_|  
                                   |__/|_|               
                                    Coded by {Fore.GREEN}ToxidWorm{Style.RESET_ALL}""")
print
parser = argparse.ArgumentParser(description='Aza encryptor arguments')
parser.add_argument("--text", type=str, help="Text to encrypt")
parser.add_argument("--method", type=str, help="Method to encrypt (base64, binary, hex)")
parser.add_argument("--tofile", type=str, help="Create file with results, 1 - Create and encrypt, 0 - Encrypt without creating")
args = parser.parse_args()

if args.method == 'base64':
	sample_string = str(args.text)
	sample_string_bytes = sample_string.encode("ascii")
	base64_bytes = base64.b64encode(sample_string_bytes)
	base64_string = base64_bytes.decode("ascii")
	print(f'{Fore.YELLOW}Result: {base64_string}{Style.RESET_ALL}')
	if args.tofile == '1':
		ft = open("out.txt","w+")
		f = open( 'out.txt', 'w' )
		f.write(f"This text encrypted by AZA Cryptor\nResult of encoding:\n{base64_string}")
		f.close()

if args.method == 'binary':
	sample_string = args.text
	res = ''.join(format(ord(i), '08b') for i in sample_string)
	print(f'{Fore.YELLOW}Result: {str(res)}{Style.RESET_ALL}')
	if args.tofile == '1':
		ft = open("out.txt","w+")
		f = open( 'out.txt', 'w' )
		f.write(f"This text encrypted by AZA Cryptor\nResult of encoding:\n{str(res)}")
		f.close()
if args.method == 'hex':
	s = args.text.encode("utf-8").hex()
	print(f'{Fore.YELLOW}Result: {s}{Style.RESET_ALL}')
	if args.tofile == '1':
		ft = open("out.txt","w+")
		f = open( 'out.txt', 'w' )
		f.write(f"This text encrypted by AZA Cryptor\nResult of encoding:\n{s}")
		f.close()
#else:
#	print('Unknown method')