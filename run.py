from source import airtable as url_paths_to_try
import requests
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


for file_name, url_image_path in enumerate(url_paths_to_try):
    f_path = 'output/'+str(file_name)+".jpg"
    try:
        response = requests.get(url_image_path)
        # raise Exception("trigger exception") 
        if response.status_code == 200:
            with open(f_path, 'wb') as f:
                f.write(response.content)
        del response
    except Exception as e:
        logging.error(e)