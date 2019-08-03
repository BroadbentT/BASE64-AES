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

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Initialise program variables.
# Modified: N/A
# -------------------------------------------------------------------------------------
 
secret   = 'secret'
salt     = 'salt'
key      = 'keykeykeykeykeykeykeykeykeykeykey'  
key 	 = key[:32] 				# Must be 16, 24 or 32 bytes in length.
string   = secret + salt

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Encrypt string Base64/AES.
# Modified: N/A
# -------------------------------------------------------------------------------------

iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
encrypted = base64.b64encode(iv + cipher.encrypt(string))
print encrypted

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Decrypt string Base64/AES.
# Modified: N/A
# -------------------------------------------------------------------------------------

encrypted = base64.b64decode(encrypted)
iv = encrypted[:AES.block_size]
cipher = AES.new(key, AES.MODE_CFB, iv)
decrypted = cipher.decrypt(encrypted[AES.block_size:])
print decrypted



