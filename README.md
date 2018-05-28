# Pocketsphinx

	Indian Language Speech Recognition Engine

# Supported Languages
	
	Hindi, Kannada

# Dependencies
	
* Anaconda3			

# Steps To Adapt the default acoustic model

### Step 1: Specify input audio(.raw) and corresponding transcript(.txt) file

### Step 2: Run ad.py

	python ad.py -makelocaldictonly <inputfolder> <language>

# Steps To Test the adapted acoustic model

### Step 1: Specify input audio(.raw) and corresponding transcript(.txt) file
	
### Step 2: Run single_tst.py

	python single_tst.py
	
### Step 3: Check the test results in test_adapt.txt	
	
`note:` (Check all the path equivalents in ad.py and single_tst.py) and runs only on Python 3