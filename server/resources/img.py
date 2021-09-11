from resources.database.pathinfo import img_dir
import base64

def accio_photo(head):
    dir = img_dir()
    headname = dir + head
    with open(headname, 'rb') as f:
        t = f.read()
        b = base64.b64encode(t)
    return b.decode()


def save_photo(photo, photoname):
    b = base64.b64decode(photo.encode())
    uri = img_dir() + photoname
    with open(uri, 'wb') as f:
        f.write(b)

if __name__ == '__main__':
    p = accio_photo('default.jpg')
    save_photo(p,'asdka.jpg')