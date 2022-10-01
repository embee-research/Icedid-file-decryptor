# IcedID Decryptor



A script to statically decrypt `license.dat` files associated with IcedID infections. 

The script will also decrypt the `.data` section from unpacked IcedID samples. 

Notes:
- The script will automatically detect whether a PE file or license.dat file has been given. 
- If a PE has been provided, the script assumes that the file has been unpacked first. 
- If a decryption is successful, a raw dump will be written to output.bin
- As well, a quick string search will be performed, and detected strings written to a file. 
- If an unpacked PE has been provided, C2's will be displayed on the screen.


**Sample `license.dat` file**

https://bazaar.abuse.ch/sample/1de8b101cf9f0fabc9f086bddb662c89d92c903c5db107910b3898537d4aa8e7

**Sample Unpacked IcedID file**

https://bazaar.abuse.ch/sample/669e69bc2a322d87cf3e21b3277f1a97ce550afb353074238b0be8faa317a82f/

**Usage**

`icedid-decrypt.py --file unpacked_icedid.bin` 

`icedid-decrypt.py --file license.dat`


Sample 


<img width="740" alt="image" src="https://user-images.githubusercontent.com/82847168/193405347-5bf1ca62-250f-4ede-83ca-f67fe9d1ad27.png">
