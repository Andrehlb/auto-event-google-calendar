from google.oauth2 import service_account
from googleapiclient.discovery import build

# Caminho para a chave JSON da conta de serviço
SERVICE_ACCOUNT_FILE = r"C:\Users\GitHub-Repos\auto-event-google-calendar\robotic-aviary-441207-f8-7a7e939b58d5.json"

SCOPES = ["https://www.googleapis.com/auth/calendar"]

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

service = build("calendar", "v3", credentials=credentials)

# Teste: Listar os próximos 5 eventos do Google Calendar
calendar_id = "782b753f298393b479c4ad9c86b847ce6b50571816177e8f14e484d767cfb23c@group.calendar.google.com"
events_result = service.events().list(
    calendarId=calendar_id, maxResults=5, singleEvents=True, orderBy="startTime"
).execute()

events = events_result.get("items", [])

if not events:
    print("Nenhum evento encontrado.")
else:
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        print(f"{start} - {event['summary']}")
