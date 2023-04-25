# wabbajack-autoclicker

A complementary script for [Wabbajack](https://github.com/wabbajack-tools/wabbajack), a Modlist installer for Skyrim. The script autoclicks on the download button, which benefits people who do not have Nexus Premium and want to automate downloading a modlist with hundreds to thousands of mods.

You can still use your PC while the script is running, as long as you don't obstruct the Wabbajack window and don't mind the script stealing your focus every 8 seconds.

## Limitations

- The script literary just clicks on a button if it finds it. If the button is obstructed, it can't click on it.
- It doesn't start parallel  downloads. The script monitors your down rate and only starts downloading the next file once the previous one is completed.
- The download button is responsive, so you need to make a custom screenshot for your window size.
- This isn't fast download you would get for buying Nexus Premium. It's automation of the free slow download. You are still limited to 1.5 MB or 3 MB down speed and forced to wait 5s.

## Prerequisites

[Python 3.x](https://www.python.org/downloads/)

`pip install keyboard`

`pip install PyAutoGUI`

`pip install psutil`

A custom screenshot of a download button. You can use Snipping Tool or `WIN + SHIFT + S` (example is provided in the archive).

## Usage

Run Wabbajack and begin downloading your modlist. Once a new window opens, redirecting you onto Nexus page, take a screenshot of the `SLOW DONWLOAD` button.

![Example of the SLOW DOWNLOAD button](https://github.com/Dalibor-P/wabbajack-autoclicker/blob/6120a7fe5a8f3c8b1fb408b501e092d9977f5593/example%20slow%20download%20button.png)

Make sure you have the screenshot in the same folder as your script with a name `slow download button.png`.

Run the script. Select your network interface (probably Ethernet, so 0). Reposition your windows so that none of them obstruct the Nexus window.

Press enter to start the autoclicker. Hold `CTRL + SHIFT + E` if you want to end the script.
