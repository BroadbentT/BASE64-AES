#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#  A SIMPLE PYTHON SCRIPT FILE FOR CREATING AND READING BASE64/AES ENCRYPTED STRINGS
#               BY TERENCE BROADBENT BSc CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Load required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 2.0                                                                
# Details : Display my universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("clear")

print " ____    _    ____  _____ __   _  _       __  _    _____ ____    _____ _   _  ____ ___  ____  _____ ____   "
print "| __ )  / \  / ___|| ____/ /_ | || |     / / / \  | ____/ ___|  | ____| \ | |/ ___/ _ \|  _ \| ____|  _ \  "
print "|  _ \ / _ \ \___ \|  _|| '_ \| || |_   / / / _ \ |  _| \___ \  |  _| |  \| | |  | | | | | | |  _| | |_) | "
print "| |_) / ___ \ ___) | |__| (_) |__   _| / / / ___ \| |___ ___) | | |___| |\  | |__| |_| | |_| | |___|  _ <  "
print "|____/_/   \_\____/|_____\___/   |_|  /_/ /_/   \_\_____|____/  |_____|_| \_|\____\___/|____/|_____|_| \_\ "
print "                                                                                                           "
print "                            BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)                        \n"

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Initialise program variables.
# Modified: N/A
# -------------------------------------------------------------------------------------
 
plainText  = "Blessent mon coeur d'une langueur monotone."
uniqueSalt = 'Pots de sel et de poivre'
uniqueKey  = 'Enterprise_Key'
bytes      = 32                         # Must be 16, 24 or 32 bytes in length.
while len(uniqueKey) % bytes:
   uniqueKey = uniqueKey + "="          # Add appropriate padding.
codedMessage = plainText + uniqueSalt

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Display program data to the screen
# Modified: N/A
# -------------------------------------------------------------------------------------

print "Plain Text  : " + plainText
print "Unique Salt : " + uniqueSalt
print "Unique Key  : " + uniqueKey
print "Key Length  : " + str(bytes) + " bytes"
print "Cipher Text : " + codedMessage

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Encrypt coded message - Base64/AES.
# Modified: N/A
# -------------------------------------------------------------------------------------

iv = Random.new().read(AES.block_size)
cipher = AES.new(uniqueKey, AES.MODE_CFB, iv)
encrypted = base64.b64encode(iv + cipher.encrypt(codedMessage))
print "Encrypted   : " + encrypted

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Decrypt coded message - Base64/AES.
# Modified: N/A
# -------------------------------------------------------------------------------------

encrypted = base64.b64decode(encrypted)
iv = encrypted[:AES.block_size]
cipher = AES.new(uniqueKey, AES.MODE_CFB, iv)
decrypted = cipher.decrypt(encrypted[AES.block_size:])
print "Decrypted   : " + decrypted.rstrip(uniqueSalt) + "\n"


