## offline
Demonstrates one pattern for offline estimation of time series models using GitHub actions

### What it does 

 - Schedules a github action that ...
 - Updates some parameters and saves them, then 
 - Commits the parameter file to the master branch

In this way the repository will always contain up to date parameters

### To use 

Don't fork this repository, as scheduled Github actions won't run on a fork. Instead, 
make a new public repository and manually create a new GitHub action. Then cut and paste from workflows/fit.yml into your newly created workflow file.
 
 
See you at www.microprediction.com 

