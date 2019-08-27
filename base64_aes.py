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
from Crypto import Random
from Crypto.Cipher import AES

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
uniqueSalt = 'Pots de sel et de poivre'
secretText =  uniqueSalt + plainText
uniqueKey  = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'

bytes   = 16					# 16, 24 or 32 bytes for uniqueKey.
padding = "="					# Add appropriate padding.
while len(uniqueKey) % bytes:
   uniqueKey = uniqueKey + padding
while len(secretText) % bytes:			# 16 or 32 bytes for secretMessage.
   secretText = secretText + padding

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Display program data to the screen
# Modified: N/A
# -------------------------------------------------------------------------------------

print "Plain Text  : " + plainText
print "Unique Salt : " + uniqueSalt
print "Salted Text : " + secretText
print "Unique Key  : " + uniqueKey
print "Cipher Mode : CFB\n"			# ECB, CBC, PCBC, CFB, OFB, CTR modes

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Encrypt coded message - Base64/AES.
# Modified: N/A
# -------------------------------------------------------------------------------------

#cipher = AES.new(uniqueKey, AES.MODE_ECB)	# ECB mode

iv = Random.new().read(AES.block_size)		# CFB mode
cipher = AES.new(uniqueKey, AES.MODE_CFB, iv)	# CFB mode

cipher = cipher.encrypt(secretText)		# Both
encrypted = base64.b64encode(cipher)		# Both
print "Encrypted   : " + encrypted

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Decrypt coded message - Base64/AES.
# Modified: N/A
# -------------------------------------------------------------------------------------

decrypted = base64.b64decode(encrypted)		# Both

#decipher = AES.new(uniqueKey, AES.MODE_ECB)	# ECB mode
#plainText = decipher.decrypt(decrypted)		# ECB mode

iv = decrypted[:AES.block_size]			# CFB mode
cipher = AES.new(uniqueKey, AES.MODE_CFB, iv)	# CFB mode
plainText = cipher.decrypt(decrypted[AES.block_size:])

print "Decrypted   : " + plainText.lstrip(uniqueSalt).rstrip(padding) + "\n"




