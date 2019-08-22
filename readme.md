Original fork from https://github.com/yodiaditya/slideshare-downloader.git

# Clone this repo
```
git clone https://github.com/agungw132/slideshare-downloader
```
# Install the required dependencies
```
pip2 install -r requirements_py2.txt #python 2
pip3 install -r requirements_py3.txt #python 3
```
# Download all links in a slideshare channel
Go to slides from the channel (e.g., https://www.slideshare.net/NVIDIA/presentations from NVIDIA channel).
Remember how many pages that this channel contains (e.g., NVIDIA has 12 pages).
Download all links :
```
name="NVIDIA"
cd ~/slideshare-downloader
rm list.txt
for j in {1..30}; do python extractpage2.py https://www.slideshare.net/$name/presentations/$j >> list.txt; done
cat list.txt | grep "/$name/" | grep -v "/presentations" | grep -v "/clipboards" | grep -v "/documents" | grep -v "/videos" | grep -v "/infographics" | grep -v "/followers" > list2.txt
```
# Retrieve the slides
```
for i in `cat list2.txt`; do python3 convertpdf.py https://www.slideshare.net$i; done
```
If you need only 1 file, e.g., https://www.slideshare.net/NVIDIA/nvidia-developer-program-overview-152503775
```
python3 convertpdf.py https://www.slideshare.net/NVIDIA/nvidia-developer-program-overview-152503775
```
