Installing Nextlinux CLI from source
==================================

The Nextlinux grafeas CLI can be installed from source using the Python
pip utility. The utility connects to an existing nextlinux-engine DB and
constructs grafeas note and occurrence documents.  Below is an example
installation if, say, one were running a fresh container based on
centos:latest

.. code::

    yum -y install epel-release && yum -y install python-pip git && pip install --upgrade pip && pip install --upgrade setuptools

    git clone https://github.com/nextlinux/nextlinux-grafeas-cli
    cd nextlinux-grafeas-cli
    pip install --upgrade . 
    cd ..

Using Nextlinux Grafeas CLI
==================================

The pre-requisites for using this tool are that there is an existing
nextlinux-engine service up and running, along with the nextlinux-engine
database port exposed and accessible from the place where this tool is
being executed.  Note that if you are running nextlinux-engine using the
supplied docker-compose.yaml, you will have to add a section to the
nextlinux-db service (and restart the services) to expose the DB port
5432 in order for it to be accessed externally.  If you do not have
nextlinux-engine service running already, please visit the
`nextlinux-engine github page <https://github.com/nextlinux/nextlinux-engine>`_ for instructions on
how to install nextlinux-engine.

Once nextlinux-engine is up and running (we also recommend adding some
images to nextlinux-engine, in order to get package notes and
package-vulnerability occurrences), the general flow is to set the
NEXTLINUX_DB_CONNECT environment to the connect string for the
nextlinux-engine DB, and then use the tool to list and then generate
vulnerability/package note JSON documents.  To generate grafeas
package-vulnerability occurrences, set GRAFEAS_HOSTPORT environment to
an accessible grafeas service, and then use the tool to list and then
generate package-vulnerability occurrence JSON documents.

.. code::

    export NEXTLINUX_DB_CONNECT="postgresql+pg8000://postgres:<your-nextlinux-db-password>@<your-nextlinux-db-host>:5432/postgres"
    nextlinux-grafeas note vulnerabilities
    nextlinux-grafeas note vulnerabilities <vulnerabilityId from previous>
    nextlinux-grafeas note packages
    nextlinux-grafeas note packages <packageName from previous>

    export GRAFEAS_HOSTPORT="<your-grafeas-host>:8080"
    nextlinux-grafeas occurrence package-vulnerabilities
    nextlinux-grafeas occurrence package-vulnerabilities <full line (imageId packageName vulnId) from previous>

Examples with curl uploads to grafeas service (for the 'nash' package in this example)

.. code::

    nextlinux-grafeas note packages nash | curl -v -H 'content-type: application-json' -XPOST http://${GRAFEAS_HOSTPORT}/v1alpha1/projects/nextlinux-distro-packages/notes?noteId=nash -d @-
    nextlinux-grafeas note packages nash | curl -v -H 'content-type: application-json' -XPUT http://${GRAFEAS_HOSTPORT}/v1alpha1/projects/nextlinux-distro-packages/notes/nash -d @-
    curl -v -XGET http://${GRAFEAS_HOSTPORT}/v1alpha1/projects/nextlinux-distro-packages/notes/nash    
    curl -v -XDELETE http://${GRAFEAS_HOSTPORT}/v1alpha1/projects/nextlinux-distro-packages/notes/nash
