# apk-downloader

This script can help you download top selling apps from Google Play Store.

# Requirements

- [protobuf](https://github.com/google/protobuf)

Refer [egirault/googleplay-api](https://github.com/egirault/googleplay-api) for more details.

Briefly,

```bash
git clone https://github.com/google/protobuf
cd protobuf
./autogen.sh
./configure
make
sudo make install
cd python
python setup.py build
sudo python setup.py install
```

# Init this repo

```bash
git clone git@github.com:bdsword/apk-downloader.git
git submodule init
git submodule update
```

Then, setup your google account and password/auth-token in **googleplay_api/config.py**.

# Usage

```bash
./download.py
```
