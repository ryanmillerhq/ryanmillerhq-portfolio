# Ryan J. Miller's Development Portfolio

Self-taught Python developer with 5+ years blending sales operations expertise and technical automation. Specialized in web scraping, data pipelines, CRM integrations, and AWS orchestration using Selenium, AWS (Lambda, EC2, S3, EventBridge, Secrets Manager), and gspread. Developed AI-driven tools that boosted lead generation by 157% and automated workflows for 45 clients. Seeking part-time remote roles in data integration, sales ops automation, or web scraping to deliver scalable solutions.

LinkedIn: [https://linkedin.com/in/ryanmillerhq](https://linkedin.com/in/ryanmillerhq)  
Email: ryan@zenithproject.co
Website: [zenithproject.co](https://zenithproject.co)  
Resume: [Ryan's Resume](https://drive.google.com/file/d/1eWeQfYQYL2q69_kr2A92uzQGrmlq3mlx/view?usp=sharing)

## Skills
- **Languages/Tools**: Python, Selenium (with detection evasion), AWS (Lambda, EC2, S3, EventBridge, Secrets Manager), gspread (Google Sheets API), JavaScript, VBA, HTML  
- **Domains**: Data manipulation, API integrations, CRM optimization/migration, undetectable web scraping, sales ops enablement  
- **Approach**: Quick learner; built production tools handling 1K+ profiles/month without detection.

## Featured Projects

### 1. Human-Like Evasion Suite (human_simulator.py)
- **Description**: Integrated simulator for cursor movements, typing errors, breaks, and navigation to make web automation undetectable. Combines elements from cursor_sim.py, sleep_sim.py, typing_sim.py, and human_behavior.py.
- **Tech Stack**: Python, Selenium (ActionChains, Keys), random/time for variability.
- **Impact**: Enabled 100s of hours of LinkedIn automation in 2024 and 2025 without bans; handled 50+ requests and 100s of conversations daily with 40-60% acceptance rates.
- **Code Snippet**: See [/human-like-evasion/human_simulator.py](/human-like-evasion/human_simulator.py) (redacted version; full evasion available post-NDA).
- **Demo**: [Loom screen recording of simulator in action](https://www.loom.com/share/your-video-id) (ethical public data demo).

### 2. Threaded Database Processor (threaded_ai_cruncher.py)
- **Description**: Threaded analyzer for LinkedIn prospects and conversations, deciding AI methods and strategies with concurrent processing.
- **Tech Stack**: Python, concurrent.futures (ThreadPoolExecutor), gspread_mgr for Sheets integration, random for weighted selections.
- **Impact**: Processed 1K+ prospects/month, deciding AI prompts based on strategies.
- **Code Snippet**: See [/threaded-processor/threaded_ai_cruncher.py](/threaded-processor/threaded_ai_cruncher.py).

### 3. GSpread Manager with Exponential Backoff (gspread_mgr.py)
- **Description**: Custom wrappers for gspread with threaded calls, exponential backoff, and thread-safety for rate-limited scenarios.
- **Tech Stack**: Python, gspread, concurrent.futures, threading (Locks), urllib3/requests for error handling.
- **Impact**: Handled API rate limits for 45 clients' data syncing.
- **Code Snippet**: See [/gspread-manager/gspread_mgr.py](/gspread-manager/gspread_mgr.py).

### 4. Futures Monitoring Utility (monitor_futures_completion.py)
- **Description**: Monitors concurrent futures completion with timeout, stability window, and debug logging for thread-safe scraping pipelines.
- **Tech Stack**: Python, collections (deque), time for rolling windows.
- **Impact**: Prevented thread leaks in operations processing 50+ concurrent requests.
- **Code Snippet**: See [/utils/monitor_futures_completion.py](/utils/monitor_futures_completion.py).

### 5. Gmail-to-Notion Integrator (email_to_notion_integrator.py)
- **Description**: Automated pipeline to query Gmail, filter emails, parse content, and ingest into Notion databases.
- **Tech Stack**: Python, googleapiclient (Gmail API), notion_client, datetime for timestamp handling.
- **Impact**: Bridged unstructured emails to structured databases for operational intelligence.
- **Code Snippet**: See [/gmail-to-notion/email_to_notion_integrator.py](/gmail-to-notion/email_to_notion_integrator.py).

### 6. Homebase Orchestrator (homebase_orchestrator.py)
- **Description**: Bidirectional sync framework for task dashboards using AWS Lambda, with prioritization, modes, and backoff.
- **Tech Stack**: Python, boto3 (S3, SecretsManager), gspread for Sheets, logging for orchestration.
- **Impact**: Ensured real-time alignment across distributed dashboards for sales ops.
- **Code Snippet**: See [/homebase/homebase_orchestrator.py](/homebase/homebase_orchestrator.py).

## How to Explore
- Clone this repo: `git clone https://github.com/ryanmillerhq/ryanmillerhq-portfolio.git`
- View demos and contact for collaborations or deeper code reviews.

This portfolio is a work in progress—check back for updates!
