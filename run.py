# from source import airtable as url_paths_to_try
import requests
import shutil

url_paths_to_try=[
"https://v5.airtableusercontent.com/v1/15/15/1679342400000/AXgRdRQrXFUGMA8UC4RARw/TnJ93fJ8r0PNzxeCplV04Fq7Xv5DKFOv_YutdmeZ4UNhJ8YQQ_I2MODETwR738NO13ABHn8i-icsvpddc4fr1-4mH3aw9SMpVGdr_TR4o9o/Eu2753h82HVIvCH9PYoNJiJC-Psf0RFiUKJVXoIoktk"
]

for file_name, url_image_path in enumerate(url_paths_to_try):
    f_path = str(file_name)+".jpg"
    try:
        response = requests.get(url_image_path, stream=True)
        if response.status_code == 200:
            with open(f_path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, 'output')
        del response
            # print(True)
            # open(file_name, 'wb').write(r.content)
            # with open(file_name, 'wb') as f:
            #     f.write(r.content)
    except Exception as e:
        print(e)