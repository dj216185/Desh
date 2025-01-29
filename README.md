## Complete Workflow Example 🔄

### Encryption Process:
```plaintext
----Encryption----
Enter a string: Devesh
Enter a key value: 5

Converted string: ['0809', '2609', '2312']
Converted numbers: [0.0809, 0.2609, 0.2312]
Tan values: [0.0811, 0.267, 0.2354]
Encrypted value after key2: 081103010008
Key2 values for each pair:
Pair 1: [0, 0]
Pair 2: [1, 3]
Pair 3: [1, 2]
CipherText: ildbai

Decryption Process:

----Decryption----
Input the key value to decrypt:- 5

Converted ciphertext: ['0811', '0301', '0008']
Tangent values: [0.0811, 0.2876, 0.2558]
Arctangent values: [0.0809, 0.2609, 0.2312]
[809, 2609, 2312]
Recovered plaintext: DEVESH

Workflow Visualization 🔍

graph TD
    A[Original Message: Devesh] --> B[Add Key1: 5]
    B --> C[Convert to Numbers: 0809 2609 2312]
    C --> D[Apply Tangent Function]
    D --> E[Key2 Processing]
    E --> F[Ciphertext: ildbai]
    F --> G[Decryption Key: 5]
    G --> H[Reverse Tangent]
    H --> I[Remove Key1]
    I --> J[Recovered Text: DEVESH]

Key Observations:

    Case-insensitive conversion (Input: Devesh → Output: DEVESH)

    Automatic padding for odd-length strings

    Multi-layer mathematical transformations

    Symmetric key requirement for decryption

Requirements 📋

    Python 3.6+

    Standard libraries only (math)

Security Notice ⚠️

❗ This is an experimental cryptographic system. Not recommended for production use. For research/educational purposes only. ❗
