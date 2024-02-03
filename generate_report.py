import argparse
from datetime import datetime
from glob import glob
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generate_report(year, month, temperature):
    # Access the API key from environment variables
    api_key = os.getenv('OPENAI_API_KEY')
    client = openai.OpenAI(api_key=api_key)

    file_pattern = f"{year}{month:02d}??*.txt"
    files = glob(file_pattern)

    # Concatenate the content of the reports
    reports_content = "\n\n".join(open(file, "r").read() for file in files)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=temperature,
        messages=[
            {"role": "system", "content": """You are a diligent and objective HR professional. You have been asked to generate a report for the progress of the consultants in a software department, based on the daily reports submitted by the consultants themselves. 
             
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
            """},
            {"role": "user", "content": reports_content}
        ]
    )

    print("Completion usage information:\n", completion.usage)

    return completion.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description='Generate a progress report from daily reports.')
    parser.add_argument('--month', type=int, default=datetime.now().month, help='Month for which to generate the report (integer 1-12).')
    parser.add_argument('--temperature', type=float, default=0.5, help='Model temperature for OpenAI completion.')
    # Add first_name and last_name arguments with default values
    parser.add_argument('--first_name', type=str, default='Jack', help='First name of the employee.')
    parser.add_argument('--last_name', type=str, default='Heseltine', help='Last name of the employee.')
    args = parser.parse_args()

    year = datetime.now().year
    month_name = datetime(year, args.month, 1).strftime("%B")

    report_content = generate_report(year, args.month, args.temperature)

    # Use args.first_name and args.last_name in the file name
    file_name = f"{args.first_name}_{args.last_name}_Progress_Report_{month_name}_{year}.txt"
    directory_path = os.path.join("..", "progress-reports")
    os.makedirs(directory_path, exist_ok=True)
    file_path = os.path.join(directory_path, file_name)

    # Save the report content to a file
    with open(file_path, 'w') as file:
        file.write(report_content)
    
    print(f"Report generated and saved to {file_path}")

if __name__ == "__main__":
    main()
