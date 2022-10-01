#IcedID Decryptor Script
#Author: Matthew Brennan @HuntressLabs
#Twitter: @embee_research

import struct,re,argparse,pefile,sys

#parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str,required=True)
parser.add_argument("--out",type=str,required=False, default="output.bin")
args=parser.parse_args()


inputname = args.file
outputname = args.out


#read input file
f =  open(inputname, "rb")
enc = f.read()
f.close()

#check if file is a PE
if enc[0:2] == b"MZ":
    try:
        #open file again and parse as a PE
        pe = pefile.PE("./"+inputname)
        #look for data section containing encrypted content
        for section in pe.sections:
            
            if ".data" in str(section.Name):
                #retrieve data section
                rdata = section.get_data()
                #Grab first blob containing the encrypted data
                offset = re.search(b'\x00\x00\x00\x00', rdata).start()
                enc = rdata[0:offset]
         
                
    except Exception as e:
        print(e)
        sys.exit(1)

#function to allow 32-bit ror calculations
def ror32(value, key):

    left = (value >> key) 
    right = (value << (32-key))
    
    return (left | right) & 2**32-1

maxLen = len(enc)
decoded = bytearray(enc)
mi = ""

#Initialize keys
rawkey = bytes(enc[-16:])
key = [0 for i in range(4)]
for i in range(4):

    #Unpack the key structure?
    temp = struct.unpack('<I', rawkey[i*4:i*4+4])
    #get first value since struct returns tuples
    key[i] = temp[0]

#perform the main decoding
for count in range(maxLen):
    
    counter = count & 3
    index = ((count & 0xff) + 1) & 3
    value = key[index] 
    decoded[count] = ((key[index] + key[counter])  ^ enc[count]) &0xff
    mbyte = value & 7
    value = (ror32(key[counter], mbyte)+1)
    key[counter] = value & 2**32-1
    mbyte = value & 7
    key[index] = (ror32(key[index], mbyte)+1) & 2**32-1



#look for strings/c2's in the restult
strings_re = re.findall("[a-zA-Z0-9\.\-]{10,}", str(decoded))

out = ""
print("{} strings found ".format(len(strings_re)))

#print a short subset of the strings   
for i in strings_re[0:6]:
    word = re.sub("x[0-9]{1,2}","", i)
    out += word + "\n"
    print(word)

                     
                     
#Write binary results to file
try:
    f = open(outputname, "wb")
    f.write(bytes(decoded))
    f.close()
    print("Wrote {} bytes to file: {}".format(len(decoded),outputname))
except:
    print("Failed to write binary file")
    print("Something went wrong :(")

#write strings to a .txt file
try:
    outputname += ".txt"
    f = open(outputname, "w")
    f.write(out)
    f.close()
    print("Wrote {} strings to file: {}".format(len(strings_re),outputname))
except Exception as e:
    print(e)
    print("Failed to write file")
    print("Something went wrong :(")

