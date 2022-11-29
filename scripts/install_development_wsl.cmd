# ------- WSL -------

# Please visit following pages for wsl set up
# https://realpython.com/installing-python/#what-your-options-are
# https://learn.microsoft.com/en-us/windows/wsl/install
# https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/
# https://learn.microsoft.com/en-us/windows/wsl/basic-commands
# https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html
# After executing following commands, for PyCharm :
# Go to Interpreter, then select WSL, and paste following path
# usr/bin/python3.8

# ------- PYTHON -------

sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8
sudo apt-get install python3-pip


# ------- DEPENDENCIES -------

sudo python3.8 -m pip install pip --upgrade
sudo python3.8 -m pip install "setuptools<60.0"
sudo python3.8 -m pip install setuptools-rust
sudo python3.8 -m pip install python-dev-tools
sudo python3.8 -m pip install cython
sudo python3.8 -m pip install numpy
sudo python3.8 -m pip install --ignore-installed pexpect
sudo python3.8 -m pip install --ignore-installed PyYAML

sudo python3.8 -m pip install dependencies_wheels/tables-3.6.1-cp38-cp38-manylinux1_x86_64.whl
sudo python3.8 -m pip install -r src/requirements.txt

# ------- SKYVIEW -------
./install_development.sh
