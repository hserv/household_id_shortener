import sys

helptext = """

You need Python 2.7.x to run. If the script detects the lxml module,
this script will make use of it to parse the xml.

To run....

    print his.py {/path/to/xml/to/convert}

"""

if len(sys.argv) != 2:
    print helptext
    sys.exit()

try:
    from lxml import etree
    # load the document
    topsecret = etree.ElementTree(file=sys.argv[1])
except:
    import xml.etree.ElementTree as ET
    # load the document
    topsecret = ET.parse(sys.argv[1])

Converted_Household_IDs = []

# identify legitimate HouseholdID values
validIDs = sorted([ts.text for ts in topsecret.iter('{http://www.hudhdx.info/Resources/Vendors/4_0_1/HUD_HMIS.xsd}HouseholdID') if len(ts.text) <= 10])

# identify all HouseholdID tags where text is of length greater than 10
IDsplusten = [ts.text for ts in topsecret.iter('{http://www.hudhdx.info/Resources/Vendors/4_0_1/HUD_HMIS.xsd}HouseholdID') if len(ts.text) > 10]

i = 1
for n, hid in enumerate(IDsplusten):
    print '%d of %d' % (n+1, len(IDsplusten))
    while str(i) in validIDs:
        i += 1

    # change all occurences
    idpt =  [ts for ts in topsecret.iter('{http://www.hudhdx.info/Resources/Vendors/4_0_1/HUD_HMIS.xsd}HouseholdID') if ts.text == hid]
    log = False
    oldID = ''
    for tag in idpt:
        log = True
        oldID = tag.text
        tag.text = str(i)

    if log:
        Converted_Household_IDs.append('Old ID: %s,  New ID: %s\n' % (oldID, str(i)))
        i += 1

#import pprint; pprint.pprint(IDsplusten)

# save log
log = open('conversion_log.txt', 'w')
for i in Converted_Household_IDs:
    log.write(i)
log.flush()
log.close()

# save the converted xml
new_xml = open('converted.xml', 'w')
topsecret.write(new_xml)
