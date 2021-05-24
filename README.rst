A library for constructing data structures used by the Slack Block Kit API
==========================================================================

blockkit provides a simple to use, Pythonic interface for creating the JSON data structures
used by Slack's API for constructing and displaying messages. It aims to provide clean interface
that fully supports introspection and type checking. It also provides complete and comprehensive
support for all of the supported block elements, as well as making it simple to extend the
available structures as new ones are added to the API.

Installation
------------

To install the most recent release use:
::

  pip install blockkit

To install the latest version of the code from GitHub use:

::

  pip install -e git+https://github.com/nickovs/blockkit.git@master#egg=blockkit

Documentation
-------------

The Slack Block Kit API expects to receive JSON data structures made up of a set of Blocks,
Elements and Components. Blocks are the top level structure for building messages and
interactive forms, Elements represent the parts of these blocks that users interact with
or which display information while Components are low-level structures that make up the
Elements. See the Slack Block Kit documentation for details.





.. --- PyPI STOP ---

Usage
-----

Build your message or UI from instances from various types of Block.

Python strings can be used where plain Text structures are expected.

Get the JSON representation by calling the json() method on your top level object,
or get the dictionary representation by calling asdict().



To Do List
----------

While the functionality of this module is fairly complete, the project itself still needs a little
work. Specifically it still needs:

- Unit tests
- Better examples
