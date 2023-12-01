if ping -c 1 google.com >/dev/null 2>&1; then
	pip install -r requirements.txt
fi
	
cd src
mkdir data
cp -r internal data/
python3 main.py ../sampleText/part1.dn
python3 webserver.py
