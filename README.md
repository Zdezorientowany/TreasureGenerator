# Treasure Generator

This repository contains Python code that generates random treasures by choosing a random combination of item, quality, and material. You can generate treasures in different ways, and also modify some of the key parameters.

## Getting Started

### Prerequisites

To use this code, you need to have Python 3 installed on your system. You also need to install the required dependencies, which you can do by running the following command in your terminal:

```
pip install -r requirements.txt
```

To use the Discord output function, you need to create a `config.ini` file and fill it with the appropriate values for your Discord bot and channel. The following code should be included in the `config.ini` file:

```
[CONFIG]
API_KEY = #BOT API 
KEYCHANNEL_ID = #CHANNEL ID
```

### Usage

To generate treasures, run the following command:

```
python main.py
```

This will display a menu with several options:

1. Advanced Generate: Generate treasures by choosing the number of items, quality, and material.
2. Quick Generate: Generate random treasures by one click.
3. Quick Generate to DISCORD: Generate random treasures and send the results to a Discord channel.
4. Options: Modify some of the key parameters used for generating treasures.
5. Exit: Exit the program.

Choose the appropriate option and follow the prompts to generate treasures.

## Built With

* Python 3
* [tabulate](https://pypi.org/project/tabulate/): A Python library for creating tables from data.
* [subprocess](https://docs.python.org/3/library/subprocess.html): A Python module for spawning new processes and executing commands.

## Authors

* [Szymon Kilian](https://github.com/Zdezorientowany)
* [Sebastian Koza](https://github.com/KozaCode)

## License

This code is unlicensed, which means it is free to use, modify, distribute and share without any restrictions or obligations. You are free to use this code for any purpose, commercial or non-commercial, without attribution or permission.

However, please note that the code is provided "as is" and without warranty of any kind, express or implied. The author of this code shall not be liable for any damages or losses arising from the use or inability to use this code.

Please use this code responsibly and ethicall.
See the [LICENSE.md](https://chat.openai.com/chat/LICENSE.md) file for details.
