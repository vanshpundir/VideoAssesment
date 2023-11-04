from gradio_client import Client

def getTextFromAudio(path):
	client = Client("https://sanchit-gandhi-whisper-jax.hf.space/")
	result = client.predict(
					path,	# str (filepath or URL to file) in 'inputs' Audio component
					"transcribe",	# str in 'Task' Radio component
					False,	# bool in 'Return timestamps' Checkbox component
					api_name="/predict"
	)
	return result