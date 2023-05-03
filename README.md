# Encrypted Notes

## Create virtual environment

```sh
python3 -m venv env
```

```
. env/bin/activate
```

## Required modules

```sh
pip install rsa tinydb pymongo uuid Pillow screeninfo
```

## In windows install

```sh
pip install "pymongo[srv]"
```

## It is important to generate the mongoUri.py file, to define username and password and connection link

```sh
echo "def URI():
    user, password = ('','')
    uri = f'mongodb://localhost' if len(user) == 0 else f'mongodb+srv://{user}:{password}@cluster0.0000.mongodb.net/?retryWrites=true&w=majority'
    return uri" > mongoUri.py
```

[![2023-05-02-221347-1599x875-scrot.png](https://i.postimg.cc/qv3c5C1V/2023-05-02-221347-1599x875-scrot.png)](https://postimg.cc/dhJT7DM4)

![logoN1-w.png](https://i.postimg.cc/bvwkKP8Y/logoN1-w.png)
