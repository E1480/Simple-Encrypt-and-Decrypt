# Simple-Encrypt-and-Decrypt

Simple encrpyt and decrypt is a simple tool that lets you encrypt and decrypt files, when you run the ``setup.py`` it will create and build the required files when buolding it will create a key with fernet and bake it in the files so when you loose the decrpter or run the setup again and use that decrypter it will not work.

> [!NOTE]
> Go to [Release](https://github.com/E1480/Simple-Encrypt-and-Decrypt/releases/tag/Release) for the latest build.

<b>Dowload</b> `setup.py` and run ```python setup.py```
<br>
it will start generating the code for encrypt and decrypt which you can read in the `setup.py` file; using pyinstaller
<br>
or go to [Release](https://github.com/E1480/Simple-Encrypt-and-Decrypt/releases/tag/Release) and download the `SimpleEncryptDecryptSetup.exe`
<br>
you can read the requiremnts in [`requirements.txt`](https://github.com/E1480/Simple-Encrypt-and-Decrypt/blob/main/requirements.txt)
<br><br>


# Usage:
Encryption:
```bash
encrypt.exe <input_file> <output_file>
```
Decryption:
```bash
decrypt.exe <input_file> <output_file>
```
