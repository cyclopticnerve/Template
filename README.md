<!----------------------------------------------------------------------------->
<!-- Project : PyPlate                                         /          \  -->
<!-- Filename: README.md                                      |     ()     | -->
<!-- Date    : 12/19/2022                                     |            | -->
<!-- Author  : cyclopticnerve                                 |   \____/   | -->
<!-- License : WTFPLv2                                         \          /  -->
<!----------------------------------------------------------------------------->

# PyPlate

## "It mostly works™"
[![License: WTFPL](https://img.shields.io/badge/License-WTFPL-brightgreen.svg)](http://www.wtfpl.net/about/)

<!-- __RM_SHORT_DESC_START__ -->
A program for creating module/package/CLI/GUI projects in Python from a template
<!-- __RM_SHORT_DESC_END__ -->

<!-- ![Screenshot](misc/screenshot.jpg) -->

## Requirements
<!-- __RM_PY_DEPS_START__ -->
None
<!-- __RM_PY_DEPS_END__ -->

## Installing
You can download the (hopefully stable)
[latest release](https://github.com/cyclopticnerve/PyPlate/releases/latest) 
from the main branch.<br>
Download either the 'tar.gz' or 'zip' file and extract it.<br>
Rename the folder without the version, e.g. 'PyPlate-0.1.0' to 'PyPlate'.

Or you can clone the git repo to get the latest (and often broken) code from the
dev branch:
```bash
foo@bar:~$ cd ~/Downloads
foo@bar:~/Downloads$ git clone https://github.com/cyclopticnerve/PyPlate
```

Next, cut/copy/paste the 'PyPlate' directory wherever you want. For the examples
below, we will use '~/Documents/Projects/Python/'.
```bash
foo@bar:~/Downloads$ mv PyPlate ~/Documents/Projects/Python
```

Lastly, you can delete the downloaded folder, if you copied it.

## Uninstalling
Just delete the 'PyPlate' folder from wherever you put it in the install step.

## Usage
To create a project, cd into the 'PyPlate/src/' directory, and run 'pyplate.py':
``` bash
foo@bar:~$ cd ~/Documents/Projects/Python/PyPlate/src
foo@bar:~/Documents/Projects/Python/PyPlate/src$ ./pyplate.py
```

Enter the required information, and 'pyplate.py' will create the required files
and folders in a subdirectory of 'DIR_BASE', where 'DIR_BASE' is the directory
above 'PyPlate'. In our example, 'DIR_BASE' is '~/Documents/Projects/Python'.

So Modules/Packages will be generated in 
'~/Documents/Projects/Python/Libs', and CLI/GUI apps will be generated in 
'~/Documents/Projects/Python/Apps'.

From there you are free to modify the projects in your favorite IDE.

Once your priject is ready for release, run the 'metadata.py' file from the 
project's 'conf' directory. This will update any metadata you have added/edited 
in the 'conf' directory.

## Metadata/Customizing the project
These files should be viewed/edited AFTER the project is generated, but BEFORE 
'metadata.py' is run.

[Click here](README/blacklist.md) to learn more about the conf/blacklist.json 
file.  
[Click here](README/metadata.md) to learn more about the conf/metadata.json 
file.  
[Click here](README/settings.md) to learn more about the conf/settings.json 
file.

After these files have been edited appropriately, run 'metadata.py' from the
'conf' directory to update the metadata in the project. This module can be run
any time AFTER the project has been created to update the metadata in the
project. Here is an example for a project of type 'm' (module) named 'ModTest':

``` bash
foo@bar:~$ cd ~/Documents/Projects/Python/Libs/ModTest/conf
foo@bar:~/Documents/Projects/Python/Libs/ModTest/conf$ ./metadata.py
```

## Notes
If you make any changes to this template to better suit your own style/setup, 
please let me know or send a pull request. I will take a look and see if I can 
incorporate your changes to make them user-agnostic. This way the template can 
hopefully become more customizable to suit everyone's needs.

## -)
<!-- -) -->
