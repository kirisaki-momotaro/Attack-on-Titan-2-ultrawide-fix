# Attack on Titan 2 Ultrawide Support Patch

This repository contains a Python script that adds ultrawide monitor support to Attack on Titan 2 game by patching specific executable files to allow for wider screen resolutions. This script supports 2560x1080 and 3440x1440 resolutions.

## Prerequisites

Before you run this script, ensure you have Python 3 installed on your system. You can download Python [here](https://www.python.org/downloads/).

## Installation

1. **Download the Script**: Clone this repository or download the script to your local machine.
2. **Locate the Game Executable**: Place the scripts inside the Steam folder where the game is installed, usually found at: C:\Program Files (x86)\Steam\steamapps\common\AoT2
3. **Run the Script**: left click the res_fix.py and select "Open with" -> "Python, follow the instuctions"
5. **Game Startup Settings**: Set "Fullscreen" to "Off" and "Region" to "EU/NA". The resolutions are not changed in the selection but are properly applied in-game so just choose the resolution you chose when you run the script. 


## Gameplay Video
![Gameplay](/readme_assets/gameplay.gif)


## Limitations
Please note that this patch is made mostly for fun and to share with the world something that has inpacted positively my gaming experience while playint this game.

Limitations include the following:
1. The patch seems to work properly only with "Fullscreen" set on off, so there will be this annoying bar at the top.
2. In any other region other than "EU/NA" the game enlarges the screen more than it should.
3. The UI as well as the cutscenes end up streched.

![Alt text](/readme_assets/settings.png)

If you change your mind and want to undo the patch you can run undo_res_fix.py or through Steam go to the settings icon on the game's page in your Steam library and then: "Properties..."->"Installed Files"->"Verify integrity of game files" and it should return the game to it's original state.
undo_res_fix.py

## Files Pached

The script will attempt to patch the following executable files:
- `AOT2_AS.exe`
- `AOT2_EU.exe`
- `AOT2_JP.exe`

## Legal Warning

This script modifies game executable files, which can potentially violate the game’s terms of service. Use this script at your own risk. Always ensure that you have backups of the original files before proceeding. This modification is for personal use only and should not be distributed as part of other software or as a standalone patch without permission from the original copyright holders of "Attack on Titan 2".

## Disclaimer

This software is provided 'as is', without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

## Acknowledgements

This script is developed by and for the community around "Attack on Titan 2". It is not officially endorsed by the developers or publishers of the game.
