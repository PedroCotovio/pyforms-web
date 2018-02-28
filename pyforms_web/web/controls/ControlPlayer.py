try:
	import cv2, base64, numpy as np
	from PIL import Image
except:
	print( "control player will not work. Libraries missing")
from pyforms_web.web.controls.ControlBase import ControlBase
import simplejson
from io import StringIO

class ControlPlayer(ControlBase):

	def __init__(self, *args, **kwargs):
		self._filename = ''
		ControlBase.__init__(self, *args, **kwargs)

	def init_form(self): 
		return "new ControlPlayer('{0}', {1})".format( self._name, simplejson.dumps(self.serialize()) )

	def processFrame(self, frame):  return frame

	def updateFrame(self):          pass

	def videoPlay_clicked(self):    pass

	def save(self, data):           pass

	def load(self, data):           pass

	def refresh(self):              pass
			
	def convertFrameToTime(self, frame):
		currentMilliseconds = (frame / self.value.videoFrameRate) * 1000
		totalseconds = int(currentMilliseconds/1000)
		minutes = int(totalseconds / 60)
		seconds = totalseconds - (minutes*60)
		milliseconds = currentMilliseconds - (totalseconds*1000)
		return ( minutes, seconds, milliseconds )

	def videoProgress_valueChanged(self):   pass

	def videoProgress_sliderReleased(self): pass

	def videoFrames_valueChanged(self):     pass

	def isPlaying(self):    pass

	def changed(self):      pass

	
	@property
	def value(self): return self._value

	@value.setter
	def value(self, value):
		if self._value!=value: self.mark_to_update_client()
		
		if isinstance( value, (str, str) ):
			if len(value.strip())==0: return
			#link = self.storage.public_download_link(value)
			link = value#self.storage.public_download_link(value)

			#ControlBase.value.fset(self, cv2.VideoCapture( link ) )

			self._filename = value
		else:
			self._value = value

	


	def serialize(self):
		data    = ControlBase.serialize(self)

		if self._filename:
			capture = cv2.VideoCapture( self._filename )
			#capture = self.value
			_, image = capture.read()

			
			if isinstance(image, np.ndarray):
				image = self.processFrame(image)
				if isinstance(image, list) or isinstance(image, tuple): image = tools.groupImage(image, True)
				
				if len(image.shape)>2: image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
				image = Image.fromarray(image)
				buff = StringIO.StringIO()
				image.save(buff, format="PNG")
				content = buff.getvalue()
				buff.close()
				data.update({ 'base64content': base64.b64encode(content) })


			data.update({ 'value':       self._filename      })
			data.update({ 'filename':       self._filename      })
			data.update({ 'startFrame':     0     })
			data.update({ 'endFrame':       1000       })
			data.update({ 'video_index':    self.video_index    })
		return data


	def deserialize(self, properties):
		ControlBase.deserialize(self, properties)
		self._filename   = properties['filename']
		self.value       = self._filename
		self.video_index = properties['video_index']
		



	@property
	def video_index(self): return int(self._value.get(1)) if self._value else 0

	@video_index.setter
	def video_index(self, value):
		if self._value!=value: self.mark_to_update_client()
		if isinstance(self._value, (str, str)): return
		if isinstance( value, (str, str) ):
			if len(value.strip())>0:
				self._value.set(1, float(value))
		elif not isinstance( self._value, (str, str) ):
			self._value.set(1, float(value))
		

	@property
	def image(self): 
		_, image = self._value.read()
		return image