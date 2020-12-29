<h1 align="center"> ISENW <br> Image Search Engine using Neural networks and Web scrapping </h1>

<br>
<p>
A web app which generates the information about an object image. The concept of <b>Convolutional Neural Networks ( CNN ) Architecture</b> is used to build the model which detects the object from the image based on the features and generates the information of it.
</p>
<br> 
Some of tools used in this project are :

* Python <br>
* Django Framework <br>
* Keras <br>
* Tensorflow <br>
* Pretrained Models <br>
* OpenCV
<br>
<img align="right" src="/Demo.gif" width="75%" height="400"/>
  
# Demo
<b>Note:</b> The Images shown in the demo are for explaination. ISENW is **not** limited to these images only. Fork this repo and check with your own images dataset.
</div>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Setup Local Environment
1. Fork this repo and clone your fork :
   <br><br> <code> $ git clone https://github.com/thedivyanshuyadav/ISENW.git </code>
   <br><br>
   ## Project Tree
    ```bash
    ISENW
    ├───.idea
    │   └───inspectionProfiles
    ├───djangoImageProject
    │   └───__pycache__
    ├───icml
    │   ├───migrations
    │   │   └───__pycache__
    │   ├───static
    │   │   └───favicon
    │   └───__pycache__
    ├───media
    │   └───icml
    │       ├───images
    │       └───predictedPie
    ├───templates
    │   ├───icml
    │   │   └───icml
    │   └───modelweight
    ├───venv
    │   ├───Include
    │   ├───Lib
    │   │   └───site-packages
    │   │       ├───pip
    │   │       │   ├───_internal
    │   │       │   │   ├───cli
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───commands
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───distributions
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───index
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───models
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───network
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───operations
    │   │       │   │   │   ├───build
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   ├───install
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───req
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───resolution
    │   │       │   │   │   ├───legacy
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   ├───resolvelib
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───utils
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───vcs
    │   │       │   │   │   └───__pycache__
    │   │       │   │   └───__pycache__
    │   │       │   ├───_vendor
    │   │       │   │   ├───cachecontrol
    │   │       │   │   │   ├───caches
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───certifi
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───chardet
    │   │       │   │   │   ├───cli
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───colorama
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───distlib
    │   │       │   │   │   ├───_backport
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───html5lib
    │   │       │   │   │   ├───filters
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   ├───treeadapters
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   ├───treebuilders
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   ├───treewalkers
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   ├───_trie
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───idna
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───msgpack
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───packaging
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───pep517
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───pkg_resources
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───progress
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───requests
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───resolvelib
    │   │       │   │   │   ├───compat
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───toml
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───urllib3
    │   │       │   │   │   ├───contrib
    │   │       │   │   │   │   ├───_securetransport
    │   │       │   │   │   │   │   └───__pycache__
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   ├───packages
    │   │       │   │   │   │   ├───backports
    │   │       │   │   │   │   │   └───__pycache__
    │   │       │   │   │   │   ├───ssl_match_hostname
    │   │       │   │   │   │   │   └───__pycache__
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   ├───util
    │   │       │   │   │   │   └───__pycache__
    │   │       │   │   │   └───__pycache__
    │   │       │   │   ├───webencodings
    │   │       │   │   │   └───__pycache__
    │   │       │   │   └───__pycache__
    │   │       │   └───__pycache__
    │   │       ├───pip-20.2.4.dist-info
    │   │       ├───pkg_resources
    │   │       │   ├───extern
    │   │       │   │   └───__pycache__
    │   │       │   ├───_vendor
    │   │       │   │   ├───packaging
    │   │       │   │   │   └───__pycache__
    │   │       │   │   └───__pycache__
    │   │       │   └───__pycache__
    │   │       ├───setuptools
    │   │       │   ├───command
    │   │       │   │   └───__pycache__
    │   │       │   ├───extern
    │   │       │   │   └───__pycache__
    │   │       │   ├───_distutils
    │   │       │   │   ├───command
    │   │       │   │   │   └───__pycache__
    │   │       │   │   └───__pycache__
    │   │       │   ├───_vendor
    │   │       │   │   ├───packaging
    │   │       │   │   │   └───__pycache__
    │   │       │   │   └───__pycache__
    │   │       │   └───__pycache__
    │   │       ├───setuptools-50.3.2.dist-info
    │   │       ├───_distutils_hack
    │   │       │   └───__pycache__
    │   │       └───__pycache__
    │   └───Scripts
    └───__pycache__
    ```
    Check for [Full Tree](</Project Tree>) .
    <br><br>
    
2. Change current directory :
    <br><br> <code> $ cd ISENW </code>
    <br><br>
    
3. Install the project dependencies :
  <br><br> <code> $ pip install -r requirement.txt </code>
  <br><br>
  
4. Run the project with this command :
  <br><br> <code> $ python manage.py runserver </code>
  
<br>

# Contributers
   * Divyanshu Yadav https://thedivyanshuyadav.github.io .    
 <br>
   
# License & Copyright 
Divyanshu Yadav , Owner of ISENW.
Licensed under the [MIT License](/LICENSE) .
