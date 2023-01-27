Replace file extension of all files in a folder:
	for file in *.html
	do
		mv "$file" "${file%.html}.txt"
	done

Clean filenames in a folder:
	import re
	import os
	import pathlib
	import glob

	nbs = glob.glob('/content/docs/docs/tutorials/*.md')

	def process(path):
		x = str(pathlib.Path(path).stem)
		x = x.lower()
		x = re.sub(r'[^a-z]','-',x)
		x = re.sub(r'-+','-',x)
		x = x.strip('-')
		x = os.path.join(str(pathlib.Path(path).parent), x+'.mdx')
		x = re.sub('/[a-z]\-','/',x)
		os.rename(path, x)

	_ = [process(x) for x in nbs]

Download all files from html index:
wget -r -np -nH --cut-dirs=3 -R index.html <url>

Cut command:
# The command below shows how to extract the first four characters
	echo "database" | cut -c1-4
# The command below shows how to extract 5th to 8th characters
	echo "database" | cut -c5-8
# Non-contiguous characters can be extracted using the comma.
# The command below shows how to extract the 1st and 5th characters
	echo "database" | cut -c1,5

Replace file extension of all files in a folder:
	for file in *.html
	do
	mv "$file" "${file%.html}.txt"
	done

Wget download all files from html index:
	wget -r -np -nH --cut-dirs=3 -R index.html <url>