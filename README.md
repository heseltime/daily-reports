# :paperclip: (Progress | X) Reports :paperclip: with the OpenAI API :postbox:

Where X is any type of report you need to make, progress reports being just my particular use case right now! See examples below, validating this LLM use case. One repetitive writing task offshored to LLM land, the perfect use case for this tech at this moment :rabbit2:

## The Idea

Go to the setup :wrench: section to give it a try with your own reporting-like task, on your own machine/with your own OpenAI API Key, once you have the idea :bulb: - outlined in terms of the following use case.

### Use case

I have a collection of daily reports in a folder somewhere, let's say they all follow the filename format "yyyymmdd.txt", so we know what month they pertain to, and I want to generate an LLM progress report mostly in third person, the type may or may not be asked for consultancy work or any job, here with a slant towards software engineering. 

I want to run a program that takes care of the content accurately but flexibly and in the style I like, even perform some simple summation (this type of math an LLM can currently certainly already do) of hours worked (included in the daily report), thus automating away the monthly task and also doing the simple by-handy tallying of (billable, typically) hours worked.

Daily report example:

> TODO

So imagine 20 or so of these at the end of a month and now you need to submit your progress report. 

The output per month should be:

> TODO

This is the manual progress report example, compare the LLM-example below! (Spoiler: The LLM one is just as good as my bored and haphazard effort at a slightly boring task, probably better.)

### Tools

Let's use the OpenAI python package to call the chat [completion API](https://platform.openai.com/docs/api-reference/chat). OpenAI also has a [quickstart tutorial](https://platform.openai.com/docs/quickstart?context=python) about this topic to get you up to speed, with a quick virtual environment/python installation primer included.

### LLM Point of View/Prompt Engineering

I chose diligent HR worker-type here but this could be anything you feel like you want. I added the important technical detail of not being judgy or providing "all-in-all" type sentences ("All in all, Jack tries really hard") because that is not appropriate for my use case, i.e. the judging is done by someone else.

## Here's the Setup :wrench:

### Just clone this repo, get an OpenAI API Key and set up a virtual environment to follow these steps

See the [quickstart tutorial](https://platform.openai.com/docs/quickstart?context=python) about the initial steps, then do the following.

#### 1: .env-file

You'll need an OPENAI_API_KEY to reproduce, and since it's a good idea to offshore that into an .env file, as per the quickstart tutorial, this implementation makes use of a .env file at the same level as generate_report.py. It should look something like:

```
OPENAI_API_KEY=sc-rt-key123
DEFAULT_FIRST_NAME=Jack
DEFAULT_LAST_NAME=Heseltine
```

#### 2: Virtual Environment and packages

External python packages used: 

* openai
* python-dotenv

Just install them into your virutal environment if you are using one, otherwise install them to your machine globally.

#### 3: Command Line Calling Works Like ...

If you know have a setup that looks like this in terms of directory structure, including some test daily reports ...

```
|-- .env file with OPENAI_API_KEY
|-- generate_report.py
|-- 20240101.txt, 20240102.txt, ... daily reports are **manual**
|-- 01/, 02/, ... archived daily reports
```

... you are good to call the python script, in one of these ways, and after activating the virtual environment:

* `./.venv/Scripts/activate`(Windows)

Then, in my case, for January and a normal [temperature](https://learnprompting.org/docs/basics/configuration_hyperparameters):

* `python ./generate_report.py --employee_name "Jack Heseltine" --month 1 --temperature 0.7`

Or just:

* `python ./generate_report.py` ... which uses the same temperature preset and takes the month according to the daily reports provided (for January, these would be 20240101.txt, 20240102.txt, and so on), pulling the default name from the .env-file instead, along with the api key.

## Progress Report Prompt :postbox:

I use this prompt for my needs, just adapt the system content in the code as needed.

```
You are a diligent and objective HR professional. You have been asked to generate a report for the progress of the consultants in a software department, based on the daily reports submitted by the consultants themselves. 
             
You trust their own judgement and try to be nice but fair and objective too, highlighting completed work but also mentioning potential challenges covered in the daily reports.

Do not judge the consultant, do not include a summary "overall" paragraph at the end, and do not include any personal opinions.

The report is supposed to be in the following format:

Subject: Progress Report for <FirstName> <LastName> <Month> 

* audience: a mix of both executives, colleagues

Suggested format:

* executive summary paragraph, heading Executive Summary.

* details section, the heading should be Details, you can add flexible sub-headings for
    * group by product or major area
    * do include details for benefit of colleagues here
    * think about impact of your work on others
    * list of bugs/tickets completed: Sub-Heading List of Bugs/Tickets Completed

* mention days PTO, but say these are not applicable to consultants. The heading should be PTO.

Data sources:
* bugs and jira databases for tickets
* sent email
* PTO report/timesheets
* Stash
* personal logs
    
Finally, sum together the hours worked per week and give an overall number of hours worked for the month so far. The heading for this part should be Total Hours Worked, then the weeks with their totals and ideally the dates of the start and the end of the respective week too, then the Total for the month below that.
```

## Generated Progress Report Example

> TODO

## Workflow and Similar Use Cases, Generalizations, Extensions ...

> TODO