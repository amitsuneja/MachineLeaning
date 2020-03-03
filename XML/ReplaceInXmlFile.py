import glob, os
import pandas as pd
import lxml.etree as ET

os.system('cls'); print()  # For Windows


path = "E:\\LenovoMyPythonProjects\\Practise\\XML"  # Path containing XML files
new_path = path + "\\NewData"
os.chdir(path)    # change your directory


# List XML files
listofxmlfiles = list()
for file in glob.glob("*.XML"):
    listofxmlfiles.append(file)


keyfile = pd.read_excel("KeyFile.xlsx")  # reading key file

# creating dictionary from dataframe columns.
my_dict = dict(zip(keyfile.orderkey, keyfile.replacekey))

for file in listofxmlfiles:
    new_file = new_path + "\\" + file
    with open(file, "rb+") as my_file:
        tree = ET.parse(my_file)
        root = tree.getroot()
        for elem in root.getiterator():
            for elem1 in elem:
                for key, value in elem1.items():
                    if elem1.attrib[key] in my_dict.keys():
                        elem1.attrib[key] = my_dict[elem1.attrib[key]]
    tree.write(new_file, encoding="utf-8")

###########################################################################################
# print(elem1.attrib)
# try:
#     elem.text = elem.text.replace("CO_202985_64915_008003_B", "Amit_Suneja")
# except AttributeError:
#     pass
###########################################################################################
# # import element tree
# import xml.etree.ElementTree as ET
#
# # import xml file
# tree = ET.parse(r'C:\ProgramData\Genetec Sipelia\SipServer\SipServer.config')
# root = tree.getroot()
# # replace bounding box with new coordinates
#
# elem = tree.find('.//AudioCodecs')
#
# for elem1 in elem:
#     if elem1.attrib["Name"] == "PCMA":
#         elem1.attrib["Enabled"] = "False"
###########################################################################################
