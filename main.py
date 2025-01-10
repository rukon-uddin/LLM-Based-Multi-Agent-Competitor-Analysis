import time
import itertools
import json
import llmDataProcessingAgent
import saveReport
import fethDataAgent as fda
import llmAgent as llm


print("*"*50)
print("Do research about your competitor (Companies Only).")
print("*"*50)
userQuerry = input("Search for companies (eg: 'AI Companies', 'software companies'): ")
numbOfCompanies = input("Number of Companies to search (eg: 4): ")

search_query = userQuerry + " goodfirms"
results = fda.scrape_google_links(search_query)

companyDict = {}

sourceLink = ""
for result in results:
    if "goodfirms" in result:
        sourceLink = result
        break

if sourceLink:
    
    # Step 2: Extract company names and URLs from GoodFirms
    company_names_and_urls = fda.get_company_names_from_source(sourceLink)
    print("Extracted Company Names and URLs:")
    for name, url in itertools.islice(company_names_and_urls.items(), int(numbOfCompanies)): # Finding report for only top 5 companies
        print(f"{name}: {url}")
        
        driver = fda.ChromeDriverInit().driver

        # Website to scrape
        # url = url # Replace with the actual website URL
        driver.get(url)
        time.sleep(5)

        # Scroll to the bottom of the page -> To load all contents
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for new content to load
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:  # Check if we have reached the bottom
                break
            last_height = new_height

        # Extract all text from the page
        all_text = driver.find_element("tag name", "body").text
        
        llmResponse = llm.getLLMResponse(all_text, "Your work is to find What services does the company provides, what technologies they use, What market they focus, and write a SWOT report. Write everythin in short bullet points.")
        
        companyDict[name] = llmResponse
        
        # Close the browser
        driver.quit()
    
    with open("RawData.json", "w") as json_file:
        json.dump(companyDict, json_file, indent=4)
    
    print("Processing Fetched Data ...")
    processedData = llmDataProcessingAgent.format_data(companyDict)
    
    with open("CompanyData.json", "w") as json_file:
        json.dump(processedData, json_file, indent=4)
        
    print("Making Competitor report...")
    threeSixtyInsight = llm.getLLMResponse(json.dumps(processedData), "I have data about several companies in a specific country, including details about their strengths, weaknesses, services offered, and SWOT analyses. Based on this data, I need a comprehensive analysis to identify aggregate trends, actionable insights and overal SWOT.")
    saveReport.competitorReport(threeSixtyInsight)
    
    
else:
    print("GoodFirms link not found.")