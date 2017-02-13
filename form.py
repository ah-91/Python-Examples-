''' Location of pyhton interpreter '''
#!C:\Users\ashanish.haldar
import cgi

form = cgi.FieldStorage()

print ("Content-Type:text/html")

print ("<html>")
print ("<head>")
print ("<title>Inside python program- from server</title>")
print ("</head>")
print ("<body>")
print ("<h1> Your form has been processed <h1>")


firstname=form.getvalue("Firstname")
secondname = form.getvalue("Secondname")
print("Name of the person is :" , firstname ,"." ,secondname)

print ("</body>")
print ("<html>")