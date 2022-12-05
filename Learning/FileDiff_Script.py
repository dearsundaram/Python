import os
import filecmp
import time
### Creating plugin file variables ###
plugin = r"C:\Users\ChidambaraSundaramP\Desktop\HCT_PrinterIssue\IHS_1_to_WAS_1.xml"
ref_plugin = r"C:\Users\ChidambaraSundaramP\Desktop\HCT_PrinterIssue\IHS_1_to_WAS_1_Orig.xml"
 
### Compare the current plugin with the referenced plugin ###
file_compare = filecmp.cmp(plugin, ref_plugin, shallow=True)
# print(file_compare)
if file_compare != True:
### Obtain the size of the file ###
  file_stat = os.stat(plugin)
  print("The plugin file size is: ", file_stat.st_size)
  print("The plugin file last modified time is: ", time.ctime(file_stat.st_mtime))
  print("Details are below")
  print("------------------------------------------------")
  file1 = open(
    r"C:\Users\ChidambaraSundaramP\Desktop\HCT_PrinterIssue\IHS_1_to_WAS_1.xml", 'r')
  file2 = open(
    r"C:\Users\ChidambaraSundaramP\Desktop\HCT_PrinterIssue\IHS_1_to_WAS_1_Orig.xml", 'r')
  file1_lines = file1.readlines()
  file2_lines = file2.readlines()
  for i in range(len(file1_lines)):
      if file1_lines[i] != file2_lines[i]:
         print("Line " + str(i+1) + " doesn't match.")
         print("------------------------")
         print("plugin_cfg.xml: " + file1_lines[i])
         print("ReferencePlugin.xml: " + file2_lines[i])
  file1.close()
  file2.close()
else:
    print("Plugin not changed!!")
