import os

path= '/Users/matt.wilkinson/Desktop/'
os.chdir(path)
os.mkdir("test_repo")
path2= '/Users/matt.wilkinson/Desktop/test_repo'
os.chdir(path2)
os.mkdir("docs")
path3= '/Users/matt.wilkinson/Desktop/test_repo/docs'
os.chdir(path3)
os.makedirs("Staging")
os.makedirs("Raw Data Vault")
os.makedirs("Business Data Vault")
os.makedirs("Presentation Layer")