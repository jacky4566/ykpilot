
import time 
from FileActions import *
from TimeHelper import *
from helperTwistedTcp import *


weatherPath = "/storage/emulated/0"
weatherDir = "ykWeather"
weatherAdress = "http://www.pancanal.com/eng/eie/radar/current_image.gif"
weatherIterSleep = 60*15 # 10 min



iterCount = 0

if __name__ == "__main__":
	print("---------------")
	print("--------------- service ")
	fa = FileActions()
	weatherFullPath = "%s/%s" % (weatherPath, weatherDir)
	print("weather dir ",weatherFullPath)
	print("chk if weather dir is there ?")
	fa.mkDir( weatherFullPath )
	print("dir is ", fa.isDir( weatherFullPath ) )

	
	th = TimeHelper()
	tLast = th.getTimestamp()-10000000

	
	while True:


		tn = th.getTimestamp()
		if (tn-tLast) > weatherIterSleep:
			fileName = "%s/wRadar_%s.gif" % (
				weatherFullPath,
				th.getNiceFileNameFromTimestamp()
				)
			DownloadFile( weatherAdress, fileName )
			tLast = tn
		else:
			print(th.getNiceHowMuchTimeItsTaking(weatherIterSleep-(tn-tLast)) )

		
		time.sleep(10)
		print("service ",iterCount)
		iterCount+= 1


		