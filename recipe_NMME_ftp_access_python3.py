# # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Access / Interact with NMME FTP using Python3 ftplib
# 
# RECIPE FOR IARC NOVEMBER 2017 HACKATHON
# 
# Author: Michael Lindgren (malindgren@alaska.edu)
# Funder: SNAP
# # # # # # # # # # # # # # # # # # # # # # # # # # # 

if __name__ == '__main__':
	import ftplib, os

	base_url = 'ftp.cpc.ncep.noaa.gov'

	# connect and login to the public FTP service
	f = ftplib.FTP()
	f.connect( base_url )
	f.login()
	
	# change the current directory to the NMME project
	f.cwd( 'NMME' )

	# list the projects
	project_list = f.nlst()
	
	# from the project you want...  list the subdirs (models)
	project = 'realtime_anom'

	f.cwd( project )
	model_list = f.nlst()

	# from the model you want... list the available datas
	model = 'GFDL'

	f.cwd( model )
	time_list = f.nlst()

	# choose a time-step we want:
	cur_time = time_list[-1] # choose the last one

	f.cwd( cur_time )
	dat_list = f.nlst()

	# now lets download a file from this list.
	fn = dat_list[10]
	output_path = '/home/UA/malindgren/TMP'
	out_fn = os.path.join( output_path, fn )
	f.retrbinary( "RETR " + fn, open(out_fn, 'wb').write )
