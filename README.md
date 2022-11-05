# Generic MMO Backend
A Generic MMO Game Backend Made With Django / Python.


* [1. Architecture](#architecture)
* [2. API Specification](#api-specification)
* [3. Authors](#authors)


## 1. Architecture
### 1.1 Terminology

AuthServer = Web Server responsible for the authentication  
DataServer = Web Server responsible for the persistent storage of the game  
MatchmakingServer = Web Server that acts as intermediary between the client and the GameServerManager  
GameServerManager = A cluster manager responsible for starting/stoping GameServerInstances  
GameServerInstance = An instance of the game server

PlayerClient = The game client of the player


### 1.2 Flow
#### 1.2.1 Authentication
1. PlayerClient logins at `/api/auth/login/` to obtain an AuthToken
#### 1.2.2 Retrieving Player Data
1. PlayerClient requests all the needed data from the DataServer at `/api/data/user/{...}`
#### 1.2.3 Connecting To A Game Server
1. PlayerClient requests an available game server from the MatchmakingServer with some parameters
2. The MatchmakingServer checks if there is an available GameServerInstance on the database with these parameters
3. If there is an available GameServerInstance, the MatchmakingServer responds to the PlayerClient with the IP and the Port of the GameServerInstance, else it is gonna send a request to the GameServerManager to spawn one

## 2. API Specification


## 3. Authors


Panagiotis "PanTrakX" Trakadas
