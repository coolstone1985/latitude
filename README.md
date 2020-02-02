# Data Engineering Coding Challenges


## Judgment Criteria
- Beauty of the code (beauty lies in the eyes of the beholder)
- Testing strategies
- Basic Engineering principles

## Parse fixed width file
- Generate a fixed width file using the provided spec.
- Implement a parser that can parse the fixed width file and generate a csv file. 
- DO NOT use pre built python libraries like pandas for parsing. You can use a library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding


## Instructions for use
- Use docker to build image `docker build .`
- Log into docker using `docker run -it <img_id> bash`
- Run tests using `python -m unittest discover test`
- Generate fixed width file using `python cli.py -s <spec-file(sample spec file at src/spec.json)> generate-file <OUTPUT_FILE_NAME>`
- Parse and generate csv file using `python cli.py -s <spec-file(sample spec file at src/spec.json)> parse-file <OUTPUT_FILE> <INPUT_FILE>
