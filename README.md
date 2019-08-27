# BASE64/AES ENCODER
### A SIMPLE PYTHON SCRIPT FILE TO CREATE AND READ BASE64/AES ENCODED TEXT STRINGS VIA A CORPORATE 'PASSWORD BASED KEY DERIVATION FUNCTION' (PBKDF2).

Usage: python base64_aes.py

| LANGUAGE | FILENAME          | MD5 HASH                         | CONFIDENTIALITY MODE |
|------    |------             | -------                          | -----                |
| python   | base64-aes_cfb.py | 7d46a682002ffd598c40d5b667af8361 | CFB                  |
| python   | base64-aes_ecb.py | 96529abfc1d84196c5103594cab8cc1a | ECB                  |

- [x] Confidentiallity mode, see https://csrc.nist.gov/Projects/Block-Cipher-Techniques/BCM

### Cipher Feedback Mode
__The Cipher Feedback (CFB) mode__ is a confidentiality mode that features the feedback of successive ciphertext segments into the input blocks of the forward cipher to generate output blocks that are exclusive-ORed with the plaintext to produce the ciphertext, and vice versa. The CFB mode requires an IV as the initial input block. The IV need not be secret, but it must be unpredictable.

### PBKDF2
In cryptography, __PBKDF1 and PBKDF2__ (Password-Based Key Derivation Function 2) are key derivation functions with a sliding computational cost, used to reduce vulnerabilities to brute force attacks. PBKDF2 is part of RSA Laboratories' Public-Key Cryptography Standards (PKCS) series, specifically PKCS #5 v2.0, also published as Internet Engineering Task Force's RFC 2898. It supersedes PBKDF1, which could only produce derived keys up to 160 bits long. RFC 8018 (PKCS #5 v2.1), published in 2017, recommends PBKDF2 for password hashing.

## CONSOLE DISPLAY
![Screenshot](picture1.png)
