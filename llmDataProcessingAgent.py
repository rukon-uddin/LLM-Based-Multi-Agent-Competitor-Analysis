def format_data(data):
    try:    
        companies = {}
        for company, info in data.items():
            sections = {}
            current_section = ""
            current_content = []
            
            for line in info.split('\n'):
                line = line.strip()
                if not line:
                    continue
                    
                if line.startswith(('##', '**', '###')):
                    if current_section and current_content:
                        sections[current_section] = current_content
                        current_content = []
                    current_section = line.replace('#', '').replace('*', '').strip(':').strip()
                    
                elif line.startswith('- '):
                    current_content.append(line[2:])
                elif line.startswith('*'):
                    continue
                else:
                    current_content.append(line)
            
            if current_section and current_content:
                sections[current_section] = current_content
                
            companies[company] = sections
        
        return companies
        
    except Exception as e:
        print(f"Error: {str(e)}")