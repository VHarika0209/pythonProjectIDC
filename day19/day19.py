import threading
import requests
import time
from urllib.parse import urlparse
# List of URLs with expected extensions
files = [
    ("https://filesamples.com/samples/image/jpg/sample_640×426.jpg", "image"),
    ("https://www.learningcontainer.com/wp-content/uploads/2019/09/sample-pdf-file.pdf", "pdf"),
    ("https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv", "csv"),
    ("https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt", "txt")
]
def download_file(url, filetype, index):
    ext = urlparse(url).path.split('.')[-1]
    local_filename = f"{filetype}_{index+1}.{ext}"
    print(f"📥 Thread-{index+1}: Downloading {filetype.upper()} from {url}")
    try:
        r = requests.get(url, stream=True)
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"✅ Thread-{index+1}: Saved as {local_filename}")
    except Exception as e:
        print(f"❌ Thread-{index+1}: Failed to download {url} – {e}")
start = time.time()
threads = []
for idx, (u, t) in enumerate(files):
    t_ = threading.Thread(target=download_file, args=(u, t, idx))
    threads.append(t_)
    t_.start()

for t_ in threads:
    t_.join()

print(f"\n⏱️ All downloads completed in {round(time.time() - start, 2)} seconds")
