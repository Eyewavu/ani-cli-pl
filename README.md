# Anime Cli PL
command-line tool for searching and watching anime episodes. You can easily search for your favorite anime titles, browse through their episodes, and watch them directly from the command-line interface.

## Getting Started
To use this tool, you will need to have Python 3.6 or higher installed on your system, as well as the MPV media player. Once you have those installed, clone this repository by running the following command in your terminal
```bash
git clone https://github.com/Eyewavu/ani-cli-pl.git
cd ani-cli-pl
```

Then, install all necessary dependencies with:
```bash
pip install -e .
```

## Usage
To start using it, navigate to the repository's directory and run the following command in your terminal:
```bash
anicli -s 'show-title'
```
This will search for the anime show titled 'show-title' and display the results in the command-line interface. From there, you can select the episode you want to watch and start streaming it directly in the terminal.

## Special Thanks to
- [pystardust/ani-cli](https://github.com/pystardust/ani-cli) for creating original app
- [Tsugumik/shindenpl-master](https://github.com/Tsugumik/shindenpl-master) for getting video links with raw http requests


## Noteworthy
- This CLI currently works only inside the repository's directory.
- All the data (aside from the videos themselves) is being scraped from the shinden.pl website.
- Pull requests are welcome! If you have any suggestions for improving this tool, please feel free to contribute.

## Todo
- [ ] Add scripts for sites that are unsupported on mpv
- [ ] Add Polish README.md
