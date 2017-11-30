#!/bin/bash
sudo curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
 
echo "export PATH="/root/.pyenv/bin:$PATH"" >> $HOME/.bash_profile
echo "export PATH="/root/.pyenv/bin:$PATH"" >> $HOME/.bashrc
yum install -y gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel patch
source $HOME/.bash_profile
pyenv install 2.7
pyenv install 3.5.4
echo 'eval "$(pyenv init -)"' >> $HOME/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> $HOME/.bash_profile 
echo 'eval "$(pyenv init -)"' >> $HOME/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> $HOME/.bashrc
source $HOME/.bash_profile
pyenv virtualenv 3.5.4 python3
pyenv virtualenv 2.7 python2
pyenv activate python2


