This script was developed using Python 2.7.12 though it should work with any version in the 2.7.x series.

If the script detects the lxml module, it will make use of it in order to process the xml at a faster pace.

If there is an interest in using lxml, it could be installed using the following from the commandline assuming
you have permissions to do so:

pip install lxml

The script takes only 1 argument and that is the path to the xml file you have access to that you wish to
process.

Example:

    python his.py /tmp/HUD.xml

The script generates 2 output files:

* The converted xml file called "converted.xml" which should exist in the directory you ran the script from.
  This is the xml file with the updated HouseholdIDs.
* The log file called "conversion_log.txt" which should exist in the directory you ran the script from.
  This file shows the old vs new HouseholdIDs.
