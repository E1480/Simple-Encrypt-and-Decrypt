"""
This will generate the main file to encrypt the file and decrypt it,
it's static so once compiled it cannot be cahnged.
"""

from cryptography.fernet import Fernet # type: ignore
import shutil
import os
import ctypes
import sys
import PyInstaller.__main__ # type: ignore

class SetUp:
    def __init__(self):
        print("Running Setup...")
        print("Generating Key...")
        self.key = Fernet.generate_key()
        self.fenret = Fernet(self.key)

        # Generate encryption script
        self.Encrypt_Gen = f"""import sys
import os
from cryptography.fernet import Fernet

key = {self.key!r}
fernet = Fernet(key)

def encrypt_file(input_path, output_path):
    _, ext = os.path.splitext(input_path)
    ext_bytes = ext.encode()
    with open(input_path, 'rb') as file:
        original = file.read()
    data_to_encrypt = ext_bytes + b'\\n' + original
    encrypted = fernet.encrypt(data_to_encrypt)
    with open(output_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: encrypt.exe <input_file> <output_file>")
    else:
        encrypt_file(sys.argv[1], sys.argv[2])"""

        # Generate decryption script
        self.Decrypt_Gen = f"""import sys
from cryptography.fernet import Fernet

key = {self.key!r}
fernet = Fernet(key)

def decrypt_file(input_path, output_path):
    with open(input_path, 'rb') as enc_file:
        encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)

        lines = decrypted.split(b'\\n', 1)
        ext = lines[0].decode().strip()
        content = lines[1] if len(lines) > 1 else b''

        if '.' in output_path:
            output_path = output_path.rsplit('.', 1)[0]
        output_path = f"{{output_path}}{{ext}}"
    with open(output_path, 'wb') as dec_file:
        dec_file.write(content)
        print(f"Decrypted file saved as: {{output_path}}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: decrypt.exe <input_file> <output_file>")
    else:
        decrypt_file(sys.argv[1], sys.argv[2])"""

        self.generateFiles()
        # self.clean()
    
    
    def generateFiles(self):
        print("Generating Encryption File...")
        with open('encrypt.py', 'w+') as encrypt:
            encrypt.write(self.Encrypt_Gen)
        print("Generating Decryption File...")
        with open('decrypt.py', 'w+') as decrypt:
            decrypt.write(self.Decrypt_Gen)
        self.createExe()
    
    def createExe(self):
        # input()
        PyInstaller.__main__.run([
                'encrypt.py',
                '--onefile',
                '-c'
        ])
        PyInstaller.__main__.run([
                'decrypt.py',
                '--onefile',
                '-c'
        ])
        self.clean()
    
    def clean(self):
        del_files = ['decrypt.spec', 'encrypt.spec', 'decrypt.py', 'encrypt.py']
        del_folder = ['build']
        move_folders = ['dist']

        for file in del_files:
            if os.path.exists(file):
                os.remove(file)
        for folder in del_folder:
            if os.path.exists(folder):
                shutil.rmtree(folder)
        for folder in move_folders:
            if os.path.exists(folder):
                files = os.listdir(folder)
                for each in files:
                    src = os.path.join(folder, each)
                    dst = os.path.dirname(os.path.abspath(__file__))
                    try:
                        shutil.move(src, dst)
                    except:
                        continue
        try:
            shutil.rmtree('dist')
            os.rmdir('dist')
        except:
            pass
        self.deleteSetUp()

    def deleteSetUp(self):
        ans = input("Delete Setup file? (Y/n): ")
        if ans == '':
            ans = 'y'
        
        if ans.lower() == 'y':
            try:
                os.remove(sys.argv[0])
                ctypes.windll.user32.MessageBoxW(0, "Setup Successful!", sys.argv[0], 64)
                print(f"File '{sys.argv[0]}' deleted successfully.")
            except PermissionError:
                print(f"Error: Permission denied to delete '{sys.argv[0]}'.")
        else:
            pass

if __name__ == "__main__":
    SetUp()
    exit()
