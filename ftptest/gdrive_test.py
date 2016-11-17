import ftplib

ftp = ftplib.FTP('drive.google.com')
ftp.login(uder = 'login', passwd =  'pass')
ftp.cwd('')

def grabFile():
	filename = '11-15.docx'
	localfile = open(filename, 'wb')
	ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
	ftp.quit()

def placeFile():
	filename = '11-15.docx'
	ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
	ftp.quit()


grabFile()

placeFile()