# IcedID Decryptor



A script to statically decrypt `license.dat` files associated with IcedID infections. 
The script will also decrypt the `.data` section from unpacked IcedID samples. 

**Sample `license.dat` file**

https://bazaar.abuse.ch/sample/1de8b101cf9f0fabc9f086bddb662c89d92c903c5db107910b3898537d4aa8e7

**Sample Unpacked IcedID file**

https://bazaar.abuse.ch/sample/669e69bc2a322d87cf3e21b3277f1a97ce550afb353074238b0be8faa317a82f/

### ## Usage

`icedid-decrypt.py --file unpacked_icedid.bin` 

`icedid-decrypt.py --file license.dat`





