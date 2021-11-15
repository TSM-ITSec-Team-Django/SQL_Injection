# SQL Injection

## Set up Docker environment
### Install git
1. Visit: https://git-scm.com/downloads
2. Choose your OS and follow the instructions

### Install docker
#### On Windows:
1. Visit: https://docs.docker.com/desktop/windows/install/
2. Download and install **Docker Desktop for Windows**
3. Restart Computer
4. Download and install the [Linux kernel update package](https://docs.microsoft.com/de-de/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
5. Start **Docker Desktop**

#### On Ubuntu:
1. Install Docker:
   ```
   sudo apt-get install docker-ce docker-ce-cli containerd.io          
   sudo apt install apt-transport-https ca-certificates curl software-properties-common   
   sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -   
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"        
   sudo apt update     
   apt-cache policy docker-ce
   sudo apt install docker-ce  
   ```
2. Check Docker installation:
   ```
   sudo systemctl status docker
   ```
   
3. Install Docker-Compose:
   ```
   sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose  
   sudo chmod +x /usr/local/bin/docker-compose
   ```

4. Check Docker-Compose installation: 
   ```
   docker-compose --version
   ```

### Clone Project
1. Create a new folder for Repositories
2. Start a new Command-line interface (CMD, Terminal, ...) and navigate to the new created folder
3. Clone this Github-Repository: 
   ```
   git clone https://github.com/TSM-ITSec-Team-Django/SQL_Injection.git
   ```

### Start Django Project
1. Navigate with a Command-line interface into the cloned Repository
2. Start the Docker containter: 
   ```
   docker-compose up
   ```
4. If it fails, try again: 
   ```
   docker-compose up
   ```

## Connect to Django Project
* Django is running on http://localhost:8000
* There is a simple login interface
* There are 3 users that can be used to log in:
* username ***admin*** and password ***password***
* username ***alice*** and password ***1234***
* username ***bob*** and password ***4321***

## SQL Injection
* This login system is protected against SQL injection.
* A sql-injection like the following will not work: username ***[anything]' OR 1 = 1 --*** and ***[anything]*** as password
* e.g. username ***alex' OR 1 = 1 --*** and ***123*** as password
