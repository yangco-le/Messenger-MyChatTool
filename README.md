# Messenger

A simple chat tool implemented from scratch.  Coursework of course IS301, Computer Communication and Network, SJTU.

<img src="imgs/login_background.png" alt="Logo" title="Logo" style="zoom: 150%;" />

<!-- TOC -->

- [Messenger](#messenger)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
  - [Usage](#usage)
  - [To Do](#to-do)

<!-- /TOC -->

## Getting Started

First download all the files, after that you have two ways to run the project:
1. You can enter the /bin folder, run `server.exe`, open two `login.exe` files at the same time, log in to two accounts, in which you can conduct one-to-one chat, group chat, file transfer, picture transfer, emoticon package using, etc.
2. Follow the instructions to configure the corresponding environment, run `server.py` and `login.py` in the python runtime environment, the running process and functions are the same as the first case.

### Prerequisites

- Windows 10
- Python 3.7.0
- [server.py](https://github.com/yangco-le/Messenger-MyChatTool/blob/main/server.py) Used as the server, accepting the request of the clients and then processes it accordingly.
- [login.py](https://github.com/yangco-le/Messenger-MyChatTool/blob/main/login.py)  Used as the clients, responsible for requesting connection. Also it contains the code for the login interface.
- [main_page.py](https://github.com/yangco-le/Messenger-MyChatTool/blob/main/main_page.py)	Used to build the main page.
- [personal_chat.py](https://github.com/yangco-le/Messenger-MyChatTool/blob/main/personal_chat.py)  Code for one-to-one chat and the interface, including the code for file transfer, picture transfer, emoticon package using.
- [group_chat.py](https://github.com/yangco-le/Messenger-MyChatTool/blob/main/group_chat.py)  Code for group chat and the interface.
- [/bin](https://github.com/yangco-le/Messenger-MyChatTool/blob/main/bin)  The folder where the executable files is located.
- [/emoji](https://github.com/yangco-le/Messenger-MyChatTool/tree/main/emoji)  Used to support the emoji function.
- [/imgs](https://github.com/yangco-le/Messenger-MyChatTool/tree/main/imgs)  Picture files needed for this project.
- [/ui_dir](https://github.com/yangco-le/Messenger-MyChatTool/tree/main/ui_dir)  The folder where the ui original files is located.

## Usage

```
git clone git@github.com:yangco-le/Messenger-MyChatTool.git
cd Messenger-MyChatTool

pip install -r requirements.txt
python server.py
python login.py    # Client 1: You mat log in with: Account 518030910001, Password 1
python login.py    # Client 2: You mat log in with: Account 518030910002, Password 2
```

Or you can just `cd bin` and double click the two executable files to replace the code running operations above.

## Supplement

### IP Settings

The IP address of the server is initially set as the `local loopback address(127.0.0.1)` in the project. Therefore, for now this project only supports the communication between the two local processes if not changing the configuration. If you want to expand the service range, you can change the server IP address to the local IP address, with the terminals performing access and communication based on the given IP address.

### Original Accounts

Six original accounts are set up in this project, given as follows:

| Account      | Password |
| ------------ | -------- |
| 518035910001 | 1        |
| 518035910002 | 2        |
| 518035910003 | 3        |
| 518035910004 | 4        |
| 518035910005 | 5        |
| 518035910006 | 6        |

## Contributor

- [yangco-le](https://github.com/yangco-le)

## Contact Me

- yanglily@sjtu.edu.cn