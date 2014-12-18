gitography-dependencies
-----------------------

Commandline tool for building dependencies from a docker file

This tool is used as part of the gitography build pipeline to handle depedncy
resolution for Dockerimages


We look for a Dockerfile with the following comments in it's header:

<pre>#IMAGE_REPO = /home/obowersa/webapp3/</pre>
<pre>#IMAGE_TAG = 1.1</pre>
<pre>#IMAGE_REG = http://localhost:5000/v1/repositories/</pre>
The IMAGE_REPO is either a local or remote git repository which we clone from if
the parent image cant be found in registry specified with IMAGE_REG. The name we query
for is a combination of the directory name specified in IMAGE_REPO and the
IMAGE_TAG

In the above, we'd query localhost:5000/v1/repositories for the image
webapp3:1.1


syntax example:
gitography-dependency --repo /home/obowersa/webapp

TODO:
Resolve logging. 
Improve documentation

