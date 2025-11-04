import os
import json
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from notion_client import Client

class EmailToNotionIntegrator:
    """
    Automated data ingestion pipeline bridging Gmail and Notion.
    Queries recent emails, filters based on allowlists, parses content,
    and creates structured entries in Notion for operational intelligence.
    """
    
    def __init__(self, notion_token, gmail_creds_params, email_db_id, contacts_db_id, plans_db_id):
        """
        Initialize with API credentials and database IDs.
        Impact: Enables secure, configurable integration without hardcoding secrets.
        """
        self.notion = Client(auth=notion_token)
        self.gmail_service = self._authenticate_gmail(gmail_creds_params)
        self.email_db_id = email_db_id
        self.contacts_db_id = contacts_db_id
        self.plans_db_id = plans_db_id
        self.whitelisted = set()  # Populated in _build_allowlists
        self.graylisted = set()
        self.blacklisted = {"reminder@superhuman.com", "sharing@superhuman.com"}
        self.tracked_ids = set()
        self.plan_map = {}
    
    def _authenticate_gmail(self, params):
        """Authenticate Gmail API using OAuth credentials."""
        creds = Credentials(**params)  # Redacted: Proprietary credential params (available under NDA)
        creds.refresh()
        return build('gmail', 'v1', credentials=creds)
    
    def _build_allowlists(self):
        """Fetch contacts from Notion to build email allowlists.
        Impact: Ensures only relevant emails are processed, enhancing data privacy.
        """
        contacts = self.notion.databases.query(database_id=self.contacts_db_id).get('results', [])
        for contact in contacts:
            emails = []  # Redacted: Proprietary email extraction logic
            tags = []    # Redacted: Tag parsing
            if "don't_track_email" in tags:
                self.graylisted.update(emails)
            else:
                self.whitelisted.update(emails)
        # Similarly build email_to_contact_ids and email_to_name maps (redacted)
    
    def _fetch_tracked_emails(self):
        """Fetch existing tracked email IDs from Notion to avoid duplicates."""
        pages = self.notion.databases.query(database_id=self.email_db_id).get('results', [])
        for page in pages:
            gid = ''  # Redacted: Extract Gmail ID
            self.tracked_ids.add(gid)
    
    def _build_plan_map(self):
        """Map Notion plans to subject keywords for categorization."""
        plans = self.notion.databases.query(database_id=self.plans_db_id).get('results', [])
        for plan in plans:
            keywords = []  # Redacted: Keyword parsing
            self.plan_map[plan['id']] = {'keywords': keywords, 'category': []}  # Redacted: Categories
    
    def _fetch_recent_emails(self, days=3):
        """Query Gmail for recent messages using API.
        Impact: Efficiently retrieves unstructured data for transformation.
        """
        after = int((datetime.now() - timedelta(days=days)).timestamp())
        response = self.gmail_service.users().messages().list(userId='me', q=f"after:{after}").execute()
        return [msg['id'] for msg in response.get('messages', [])]
    
    def process_emails(self):
        """Main pipeline: Fetch, filter, parse, and ingest emails into Notion.
        Impact: Automates workflow, turning emails into actionable CRM data.
        """
        self._build_allowlists()
        self._fetch_tracked_emails()
        self._build_plan_map()
        msg_ids = self._fetch_recent_emails()
        tracked_count = 0
        for msg_id in msg_ids:
            if msg_id in self.tracked_ids:
                continue
            msg = self.gmail_service.users().messages().get(userId='me', id=msg_id, format='full').execute()
            # Redacted: Proprietary parsing of headers, body, attachments, and filtering logic
            # (e.g., extract subject, from/to/cc, date, labels, body_rich_text, attachments)
            if False:  # Redacted: Filter condition based on whitelists and patterns
                continue
            properties = {}  # Redacted: Transform to Notion properties (e.g., relations to contacts/plans)
            page = self.notion.pages.create(parent={"database_id": self.email_db_id}, properties=properties)
            # Redacted: Append parsed content blocks to page
            tracked_count += 1
        return tracked_count

# Usage Example:
if __name__ == "__main__":
    notion_token = os.environ["NOTION_TOKEN"]  # Securely from env
    gmail_params = {  # Redacted: Full params
        "refresh_token": os.environ["GMAIL_REFRESH_TOKEN"],
        "client_id": os.environ["GMAIL_CLIENT_ID"],
        "client_secret": os.environ["GMAIL_CLIENT_SECRET"],
        "token_uri": "https://oauth2.googleapis.com/token"
    }
    integrator = EmailToNotionIntegrator(notion_token, gmail_params, "email_db_id", "contacts_db_id", "plans_db_id")
    new_emails_tracked = integrator.process_emails()
    print(f"Tracked {new_emails_tracked} new emails.")
