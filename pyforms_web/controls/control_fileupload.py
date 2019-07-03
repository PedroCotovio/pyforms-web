import os
from django.conf import settings
from pyforms_web.controls.control_base import ControlBase
import simplejson

class ControlFileUpload(ControlBase):

	def __init__(self, *args, **kwargs):
		super(ControlFileUpload, self).__init__(*args, **kwargs)
		self._button = None
		self._feedback = None
		self._feedback2 = None
		self._drop = None
		self._remove_confirmation = None
		self._limit_name = 15

	def init_form(self):
		return "new ControlFileUpload('{0}', {1})".format(self._name,
														  simplejson.dumps(self.serialize()) )

	@property
	def filepath(self):
		if self.value:
<<<<<<< HEAD
			return os.path.join(settings.MEDIA_ROOT, self.value[len(settings.MEDIA_URL):])
=======
			return os.path.join( settings.MEDIA_ROOT, self.value[len(settings.MEDIA_URL):] )
>>>>>>> v4
		else:
			return None

	def serialize(self):
<<<<<<< HEAD
		data 	  = super(ControlFileUpload, self).serialize()
		data.update({'button':self._button,
					 'feedback':self._feedback,
					 'feedback2':self._feedback2,
					 'drop':self._drop,
					 'remove_confirmation':self._remove_confirmation,
					 'limit_name': self._limit_name,})

=======
		data = super(ControlFileUpload, self).serialize()
>>>>>>> v4
		if self.value:
			try:
				file_data = {
					'name': os.path.basename(self.value),
					'size': os.path.getsize(self.filepath),
					'file': self.value,
					 'url': self.value
				}
				data.update({ 'file_data':file_data })
			except OSError:
				pass

		return data