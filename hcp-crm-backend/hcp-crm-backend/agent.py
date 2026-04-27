import os
import datetime
import requests
import json


class LangGraphAgent:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama-3.3-70b-versatile"

    def call_llm(self, prompt: str):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a strict JSON generator. Always return valid JSON only. No explanations."
                },
                {"role": "user", "content": prompt}
            ],
            "temperature": 0,
            "response_format": {"type": "json_object"}
        }

        response = requests.post(self.base_url, headers=headers, json=payload)
        data = response.json()

        print("RAW LLM OUTPUT:", data)

        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        else:
            raise ValueError(f"Groq API error: {data}")

    def run_tool(self, tool_name, payload):
        if tool_name == "log_interaction":
            return self.log_interaction(payload)
        elif tool_name == "edit_interaction":
            return self.edit_interaction(payload)
        elif tool_name == "schedule_followup":
            return self.schedule_followup(payload)
        elif tool_name == "generate_insights":
            return self.generate_insights(payload)
        elif tool_name == "compliance_check":
            return self.compliance_check(payload)

    def log_interaction(self, payload):
        text = payload.get("user_input") or payload.get("notes")

        prompt = f"""
Extract structured CRM data from the text below.

Return ONLY valid JSON. No explanation.

Format:
{{
  "hcp_name": "Doctor name (e.g., Dr. Sharma)",
  "interaction_type": "Meeting | Call | Email | null",
  "date": "YYYY-MM-DD",
  "time": "HH:MM or null",
  "attendees": "names of people present (e.g., Dr. Sharma, Dr. Rao)",
  "topics": "main subject discussed",
  "sentiment": "Positive | Neutral | Negative",
  "materials_shared": "items given like brochure, samples, presentation, leaflet",
  "outcomes": "short summary of what happened or result of meeting",
  "followup": "next action, plan, or future step (e.g., follow up next week, send details, schedule meeting)",
  "notes": "original text"
}}

If materials like brochure, samples, or documents are mentioned, fill materials_shared.
If people are mentioned, include them in attendees.
If any future action is mentioned (like follow up, send, schedule, revisit), fill followup.

Text:
{text}
"""

        structured = self.call_llm(prompt)

        try:
            parsed = json.loads(structured)

            required_keys = [
                "hcp_name", "interaction_type", "date", "time",
                "attendees", "topics", "sentiment",
                "materials_shared", "outcomes", "followup", "notes"
            ]

            for key in required_keys:
                if key not in parsed:
                    parsed[key] = None

            # ✅ Auto-fill date
            if not parsed.get("date"):
                parsed["date"] = str(datetime.date.today())

            # ✅ Auto-fill time
            if not parsed.get("time"):
                parsed["time"] = datetime.datetime.now().strftime("%H:%M")

            # ✅ 🔥 FOLLOWUP FALLBACK (IMPORTANT)
            if not parsed.get("followup") or parsed.get("followup") in ["", None]:
                text_lower = text.lower()

                if "follow up" in text_lower or "followup" in text_lower:
                    parsed["followup"] = "Follow up planned"
                elif "next week" in text_lower:
                    parsed["followup"] = "Follow up next week"
                elif "schedule" in text_lower:
                    parsed["followup"] = "Schedule next interaction"
                elif "send" in text_lower:
                    parsed["followup"] = "Send requested information"
                else:
                    parsed["followup"] = None

        except Exception as e:
            print("JSON ERROR:", e)
            print("RAW OUTPUT:", structured)

            parsed = {
                "hcp_name": None,
                "interaction_type": None,
                "date": str(datetime.date.today()),
                "time": datetime.datetime.now().strftime("%H:%M"),
                "attendees": None,
                "topics": None,
                "sentiment": None,
                "materials_shared": None,
                "outcomes": None,
                "followup": None,
                "notes": text
            }

        return parsed

    def edit_interaction(self, payload):
        return {"updated_fields": payload["changes"]}

    def schedule_followup(self, payload):
        return {
            "suggested_date": str(datetime.date.today() + datetime.timedelta(days=14))
        }

    def generate_insights(self, payload):
        return {"insight": "Most interactions last month were positive"}

    def compliance_check(self, payload):
        return {"status": "Compliant", "issues": []}


# ✅ Initialize agent
langgraph_agent = LangGraphAgent()
