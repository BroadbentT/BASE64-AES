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
from Crypto.Protocol.KDF import PBKDF2

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 2.0                                                                
# Details : Display universal header.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("clear")
print " ____   __   _  _        __     _    _____ ____    _____ _   _  ____ ___  ____  _____ ____   " 
print "| __ ) / /_ | || |      / /    / \  | ____/ ___|  | ____| \ | |/ ___/ _ \|  _ \| ____|  _ \  "
print "|  _ \| '_ \| || |_    / /    / _ \ |  _| \___ \  |  _| |  \| | |  | | | | | | |  _| | |_) | "
print "| |_) | (_) |__   _|  / /    / ___ \| |___ ___) | | |___| |\  | |__| |_| | |_| | |___|  _ <  "
print "|____/ \___/   |_|   /_/    /_/   \_\_____|____/  |_____|_| \_|\____\___/|____/|_____|_| \_\ "
print "                                                                                             " 
print "                    BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)                  \n"

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Initialise program variables.
# Modified: N/A
# -------------------------------------------------------------------------------------
 
plainText  = "Blessent mon coeur d'une langueur monotone"
companyKey = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
blockSize  = 16 				# 16 to 256 in mutiples of 16 in length
padding    = lambda s: s + (blockSize - len(s) % blockSize) * chr(blockSize - len(s) % blockSize)
unpad      = lambda s: s[:-ord(s[len(s) - 1:])]

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Create the functions called from main.
# Modified: N/A
# -------------------------------------------------------------------------------------

def Key(companyKey):
   salt = 'Pots de sel et de poivre'
   key = PBKDF2(companyKey, salt, 64, 1000)
   return key[:32]

def encrypt(plainText, companyKey):
   privateKey = Key(companyKey)
   text = padding(plainText)
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(privateKey, AES.MODE_CBC, iv)
   return base64.b64encode(iv + cipher.encrypt(text))

def decrypt(encryption, companyKey):
   privateKey = Key(companyKey)
   decrypted = base64.b64decode(encryption)
   iv = decrypted[:16]
   cipher = AES.new(privateKey, AES.MODE_CBC, iv)
   return unpad(cipher.decrypt(decrypted[16:]))

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : MAIN - Display program variables, and encrypt/decrypt plainText.
# Modified: N/A
# -------------------------------------------------------------------------------------

print "Plain Text  : " + plainText
print "Company Key : " + companyKey
print "Unique Salt : Pots de sel et de poivre"
print "Private Key : " + base64.b64encode(Key(companyKey))
print "Cipher Mode : CFB\n"			# Modes = ECB, CBC, CFB, PCBC, OFB, CTR

encrypted = encrypt(plainText, companyKey)
print "Encrypted   : " + encrypted
 
decrypted = decrypt(encrypted, companyKey)
print "Decrypted   : " + bytes.decode(decrypted) + "\n"



