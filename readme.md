spyder
pycharm
VsCode
Atom
Not jupyter 

We should use function
-- Resuable

never use keywords as function name, variable name
dont use single letter variable name
Variable names and function name which conveys the meaning of it

This makes our code more Readable

technical debt

Code should always contain documentation

Docstring to each function, class, modules
Avoid inline comments as much as possible

Maintainable

Explainability
 -- how easy it is to understand the code
 -- machine learni
 
Scalability
-- vertical scalability -- add ram and harddisk to the same laptop
-- horizontal scalability --- add a new laptop

Assume 4GB 1 TB 4 core cpu+ GPU
ML model with 10000 data
ML 1m data
We need to scale or infra

Modular structure
Use of modules, classes and functions

path, config should be written in a seperate config files.

Empirical logic to find summary 
Split the sentence and use first sentence and find the top 3 sentences with maxm num of words among the rest
Document summarisation
ga1909
	/bin
	- preprocessor.py
		Class ProcessDoc
			fucntions
			- special char
			- token
			- stopword removal
	- summarizer.py
		Class SummarizeDoc
			fucntions
			- readDocs
			- loadConfig
			- splitter
			- groupSentence
			- findNumWords
			- findTop3Sent
			- sentenceCombiner
			
			
relative path

local --push---git repo ---pull -- aws instance-- deploy

git init ----> only once
git add .
git commit -m "first commit"
git remote add origin "https://github.com/saz2nitk/ga1909.git" --> once
git push origin master

git add .
git commit -m "first commit"
git push origin master














 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 