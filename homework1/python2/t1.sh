#!/bin/bash
sudo curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
 
sudo echo "export PATH="/root/.pyenv/bin:$PATH"" >> $HOME/.bash_profile
export PATH="/root/.pyenv/bin:$PATH"
sudo yum install -y gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel
sudo yum install -y patch 
pyenv install 2.7
pyenv install 3.5.4
#TMP_PATH=`echo $PATH`
#sudo echo "export PATH="/root/.pyenv/versions/2.7/bin/:$PATH"" >> $HOME/.bash_profile
#export PATH="/root/.pyenv/versions/2.7/bin/:$PATH"
echo "eval "$(pyenv init -)"" >> $HOME/.bash_profile
echo "eval "$(pyenv virtualenv-init -)"" >> $HOME/.bash_profile 
source $HOME/.bash_profile
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv global 2.7
pyenv virtualenv python2
#sudo echo "export PATH="/root/.pyenv/versions/3.5.4/bin/:$TMP_PATH"" >> $HOME/.bash_profile
#export PATH="/root/.pyenv/versions/3.5.4/bin/:$TMP_PATH"
pyenv global 3.5.4
pyenv virtualenv python3




