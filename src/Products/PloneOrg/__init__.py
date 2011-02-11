from Products.CMFCore.DirectoryView import registerFileExtension
from Products.CMFCore.FSFile import FSFile

registerFileExtension("zip", FSFile)
registerFileExtension("txt", FSFile)
