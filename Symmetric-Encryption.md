Symmetric Encryption

-->Definition:
Symmetric encryption is a cryptographic technique where the same secret key is used for both encryption (locking data) and decryption (unlocking data). 
This makes it efficient, but it requires secure key sharing between parties.

-Fast and efficient for large amounts of data.
-The same key must remain secret; if leaked, security is compromised.


-->Algorithms: 
>>AES (Advanced Encryption Standard):
-The most widely used symmetric algorithm today.
-Supports key sizes of 128, 192, or 256 bits.
-Resistant to all known practical attacks.
-Adopted as the U.S. government standard.

>>DES (Data Encryption Standard):
-Key size: 56 bits.
-Widely used in the 1970s–1990s but now considered insecure due to brute-force attacks.

>>3DES (Triple DES):
-Applies DES three times with different keys for better security.
-Stronger than DES but slower and gradually being phased out.

>>Blowfish and Twofish:
-Flexible key lengths, designed for efficiency.
-Still considered secure but less common than AES.


-->Strengths:
-High performance and low computational cost.
-Works well for encrypting large amounts of data.
-Widely supported and standardized.

-->Weaknesses:
-Key distribution problem: The secret key must be shared securely between parties.
-Scalability: In large networks, managing unique keys between many users becomes complex.
-No built-in authentication: Alone, symmetric encryption cannot verify the identity of the sender or recipient.
