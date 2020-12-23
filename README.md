## offline
A model repository that conducts tests.  

### What it does 

 - Schedules a github action that ...
 - Runs the model to check that it is working...
 - Updates some parameters and saves them, then 
 - Deployed the updated model. 
 - Commits the parameter file to the master branch

In this way the repository will always contain up to date parameters

### Install

    Not intended to be used as a package

### To use

Load pre-trained parameters or models. For example:

    from getjson import getjson
    params = getjson('https://raw.githubusercontent.com/microprediction/offline/main/modelfits/expnorm/z1~altitude~3555.json')


### To do something similar 

Don't fork this repository, as scheduled Github actions won't run on a fork. Instead, 
make a new public repository and manually create a new GitHub action. Then cut and paste from workflows/fit.yml into your newly created workflow file.
 
## Tutorials

New video tutorials are available at https://www.microprediction.com/python-1 to help you
get started running crawlers at www.microprediction.com
 

