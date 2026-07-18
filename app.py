import streamlit as st
import requests

from config import (
    APP_NAME,
    TONES,
    EMAIL_TEMPLATES
)

from database.db import (
    create_table,
    save_email,
    get_all_emails,
    clear_history
)

from database.analytics import (
    get_dashboard_stats
)


# ==================================================
# DATABASE INITIALIZATION
# ==================================================

create_table()


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title=APP_NAME,
    page_icon="📧",
    layout="wide"
)


# ==================================================
# CONSTANTS
# ==================================================

API_URL = "https://ai-email-assistant-7ged.onrender.com/generate"


# ==================================================
# LOAD DATA
# ==================================================

history = get_all_emails()

dashboard = get_dashboard_stats()



# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.header("📧 AI Email Assistant")


    st.markdown(
        """
        Generate professional emails using AI.

        ### Features

        ✅ Multiple Tones  
        ✅ Email Templates  
        ✅ AI Generation  
        ✅ Download Email  
        ✅ History Tracking  
        ✅ SQLite Database  
        ✅ Analytics Dashboard
        """
    )


    st.divider()


    st.metric(
        "Emails Generated",
        len(history)
    )


    st.metric(
        "Most Used Tone",
        dashboard["most_used_tone"]
    )


    st.divider()


    st.subheader("📜 Email History")


    if history:


        for row in history:

            email_id = row[0]
            prompt = row[1]
            tone_name = row[2]
            email = row[3]
            created_at = row[4]


            with st.expander(
                f"{tone_name} | {created_at}"
            ):


                st.write(
                    "Prompt:"
                )


                st.write(prompt)


                st.text_area(
                    "Email",
                    value=email,
                    height=200,
                    key=f"history_{email_id}"
                )


    else:

        st.info(
            "No history available."
        )


    st.divider()


    if st.button(
        "🗑 Clear History",
        use_container_width=True
    ):

        clear_history()

        st.success(
            "History cleared."
        )

        st.rerun()



# ==================================================
# HEADER
# ==================================================

st.title(
    "📧 AI Email Assistant"
)


st.write(
    "Generate professional emails instantly using AI."
)


st.divider()



# ==================================================
# MAIN SECTION
# ==================================================

left_col, right_col = st.columns(
    [1,1]
)



# ==================================================
# LEFT COLUMN
# ==================================================

with left_col:


    st.subheader(
        "✍️ Email Details"
    )


    selected_template = st.selectbox(
        "Choose Template",
        list(EMAIL_TEMPLATES.keys())
    )


    email_prompt = st.text_area(
        "Describe Your Email",
        value=EMAIL_TEMPLATES[selected_template],
        height=250
    )


    st.caption(
        f"Characters: {len(email_prompt)}"
    )



    tone = st.selectbox(
        "Select Tone",
        TONES
    )



    generate_btn = st.button(
        "🚀 Generate Email",
        use_container_width=True
    )




# ==================================================
# RIGHT COLUMN
# ==================================================

with right_col:


    st.subheader(
        "📨 Generated Email"
    )


    if generate_btn:


        if not email_prompt.strip():


            st.warning(
                "Please enter email requirements."
            )


        else:


            payload = {

                "prompt": email_prompt,

                "tone": tone

            }


            try:


                with st.spinner(
                    "Generating Professional Email..."
                ):


                    response = requests.post(

                        API_URL,

                        json=payload,

                        timeout=60

                    )



                    result = response.json()



                if result.get("status") == "success":



                    generated_email = result.get(
                        "generated_email"
                    )



                    save_email(

                        email_prompt,

                        tone,

                        generated_email

                    )



                    st.success(
                        "✅ Email Generated Successfully"
                    )



                    st.text_area(

                        "Generated Email",

                        value=generated_email,

                        height=350

                    )



                    st.download_button(

                        label="📥 Download Email",

                        data=generated_email,

                        file_name="generated_email.txt",

                        mime="text/plain"

                    )



                else:


                    st.error(

                        result.get(

                            "message",

                            "Generation Failed"

                        )

                    )



            except requests.exceptions.Timeout:


                st.error(

                    "⏳ AI server timeout."

                )



            except requests.exceptions.ConnectionError:


                st.error(

                    "❌ Unable to connect to AI server."

                )



            except Exception as e:


                st.error(

                    f"Unexpected Error: {e}"

                )



    else:


        st.info(
            "Generated email will appear here."
        )




# ==================================================
# ANALYTICS DASHBOARD
# ==================================================

st.divider()


st.subheader(
    "📊 Analytics Dashboard"
)



metric1, metric2 = st.columns(2)



with metric1:


    st.metric(

        "Total Emails",

        dashboard["total_emails"]

    )



with metric2:


    st.metric(

        "Most Used Tone",

        dashboard["most_used_tone"]

    )




st.divider()



st.subheader(
    "📈 Tone Distribution"
)



if dashboard["tone_counts"]:


    st.bar_chart(

        dashboard["tone_counts"]

    )


else:


    st.info(

        "No email data available."

    )




st.divider()



st.subheader(
    "🕒 Recent Emails"
)



recent = dashboard["recent_emails"]



if recent:


    for row in recent:


        st.write(

            f"📧 {row[2]} | {row[4]}"

        )


        st.caption(

            row[1][:100]

        )


else:


    st.info(

        "No recent emails."

    )