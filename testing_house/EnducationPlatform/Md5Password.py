import hashlib

def get_password(pwd):
    # md5pwd = pwd
    m1 = hashlib.md5(b'123').hexdigest()
    print(m1)

if __name__ == '__main__':
    get_password(123)