import streamlit as st
import json
import uuid

# Page Configuration
st.set_page_config(page_title="QuickTask - Context Bridge", page_icon="⚡", layout="centered")

st.title("⚡ QuickTask Context Bridge")
st.caption("Paste messy notes, emails, or chat logs to instantly generate structured action items.")

# 1. Input Area
raw_input = st.text_area(
    "Unstructured Input",
    height=150,
    placeholder="e.g., Need to send the updated PDF report to client by 4 PM. Also check server logs for errors and call Alex."
)

def parse_text_to_tasks(text: str):
    """Splits raw text into actionable task lines with automatic basic priority detection."""
    lines = [line.strip("- *•\t") for line in text.split("\n") if line.strip()]
    tasks = []
    
    for line in lines:
        priority = "Medium"
        if any(word in line.lower() for word in ["urgent", "today", "asap", "error", "4 pm", "immediately"]):
            priority = "High"
        elif any(word in line.lower() for word in ["later", "maybe", "eventually"]):
            priority = "Low"
            
        tasks.append({
            "id": str(uuid.uuid4())[:8],
            "title": line,
            "priority": priority,
            "completed": False
        })
    return tasks

# 2. Processing & Display Action
if st.button("Extract Action Items", type="primary"):
    if not raw_input.strip():
        st.warning("Please paste some text to extract tasks.")
    else:
        st.session_state["extracted_tasks"] = parse_text_to_tasks(raw_input)

# 3. Interactive Output Rendering
if "extracted_tasks" in st.session_state and st.session_state["extracted_tasks"]:
    st.markdown("---")
    st.subheader("Actionable Checklist")
    
    updated_tasks = []
    for idx, task in enumerate(st.session_state["extracted_tasks"]):
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            is_done = st.checkbox(f"**{task['title']}**", value=task["completed"], key=f"chk_{task['id']}")
        with col2:
            badge_color = "🔴" if task["priority"] == "High" else ("🟡" if task["priority"] == "Medium" else "🟢")
            st.caption(f"{badge_color} {task['priority']}")
        
        updated_tasks.append({**task, "completed": is_done})

    # Downloadable JSON Export
    json_data = json.dumps({"items": updated_tasks}, indent=2)
    st.download_button(
        label="📥 Export Structured JSON",
        data=json_data,
        file_name="tasks_export.json",
        mime="application/json"
    )