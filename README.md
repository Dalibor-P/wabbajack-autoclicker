# wabbajack-autoclicker

A complementary script for [Wabbajack](https://github.com/wabbajack-tools/wabbajack), a Modlist installer for Skyrim. The script autoclicks on the download button, which benefits people who do not have Nexus Premium and want to download a modlist with hundreds to thousands of mods.

You can still use your PC while the script is running, as long as you don't obstruct the Wabbajack window and don't mind the script stealing your focus every 8 seconds.

## Limitations

- The script literary just clicks on a button if it finds it. If the button is obstructed, it can't click on it.
- It doesn't check if there is already a download in progress. This script is intended to download mods that are small in size (max 50 MB). Fortunately, Wabbajack sorts the downloaded mods by their size, starting with the smallest of mods.
- The download button is responsive, so you need to make a custom screenshot for your window size.

## Prerequisites

[Python 3.x](https://www.python.org/downloads/)

`pip install keyboard`

`pip install PyAutoGUI`

A custom screenshot of a download button. You can use Snipping Tool or `WIN + SHIFT + S` (sample is provided in the archive).

## Usage

Make sure you have the screenshot in the same folder as your script with the name `slow download button.png`.

Run the script and reposition the console window so that it does not obstruct the Wabbajack window.

Hold `CTRL + E` if you want to end the script.
