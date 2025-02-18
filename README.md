# LLM Based Multi-Agent Competitor Analysis

This is the code base for Multi-Agent Competitor Analysis System,
designed to collect, process, and generate comprehensive reports on competitors based on
user input. The system integrates three main agents: Data Retrieval Agent, Data Processing
Agent, and Report Generation Agent, orchestrated by a main script.

# Requirements

* Python 3.11.0
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)
* [Chrome Driver](https://googlechromelabs.github.io/chrome-for-testing/) (Required for Selenium)

# Chrome Driver Installation
If you already have chrome driver please ignore this step. Chrome driver is essential for selenium to do web scrapping.

1. Download the chromoe driver from the link provided above.
2. After downloading, unzip and include the path when initializing selenium. Check ```fetchDataAgent.py``` **line 20**.

# Instalation
1.  Clone the repository:
    
    `git clone https://github.com/rukon-uddin/LLM-Based-Multi-Agent-Competitor-Analysis.git`
    
    `cd LLM-Based-Multi-Agent-Competitor-Analysis`
2. Create new python environment and activate
    
    `python3.11 -m venv env`
    
    For Linux -  `source env/bin/activate`
    
    For Windows - `env\Scripts\activate`
3. Install the required dependencies:

    `pip install -r requirements.txt`
4. Execute the main file

    `python main.py`

# Inputs required
1. The first input required by the system is the company category with which you want to do the analysis for example `Web development companies in bangladesh` or `Health tech companies` or `Wordpress development companies`, `AI startups in dubai` etc.

2. The second input is the number of companies you want to search for that category.


# Expected Outputs from the system
The system will generate 3 files.

`RawData.json` - This file will have all the information collected from companies website. The informations will be unformated and very noisy.

`CompanyData.json` - It will have company information in an organized and formatted manner.

`CompetitorAnalysisReport.pdf` - This pdf is the final output which will have an overall competitor analysis consists of all the companies information it has collected.

