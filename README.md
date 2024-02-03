# Welcome to (Progress | X) Reports with the OpenAI API!

Where X is any type of report you need to make, progress reports being just my particular use case right now!

## The Idea

Let's use the OpenAI python package to call the chat [completion API](https://platform.openai.com/docs/api-reference/chat). OpenAI also has a [quickstart tutorial](https://platform.openai.com/docs/quickstart?context=python) about this topic to get you up to speed, with a quick virtual environment/python installation primer included.

## Here's the Setup

You'll need an OPENAI_API_KEY to reproduce, it's a good idea to offshore that into an .env file, as per the quickstart tutorial.

External python packages used: openai, python-dotenv. (Just install them into your virutal environment if you are using one.)

```
|-- .env file with OPENAI_API_KEY
|-- generate_report.py
|-- 20240101.txt, 20240102.txt, ... daily reports are **manual**
|-- 01/, 02/, ... archived daily reports
```

## Similar Use Cases, Generalizations, Extensions

TODO