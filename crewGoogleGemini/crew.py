import streamlit as st
from crewai import Process, Crew
from tasks import research_task, write_task, sanitize_filename
from agents import news_researcher, news_writer

# Streamlit UI Setup
st.set_page_config(page_title="AI Blog Generator", layout="wide")

# Title
st.title("📝 AI-Powered Tech Blog Generator")

# Sidebar for Input
st.sidebar.header("🔍 Enter Blog Topic")
topic = st.sidebar.text_input("Topic", "AI in Tech")

# Button to Start Process
if st.sidebar.button("Generate Blog"):
    st.sidebar.success("🔄 Generating... Please wait!")

    # Step-wise Progress in Left Box
    with st.spinner("🔍 Researching topic..."):
        crew = Crew(
            agents=[news_researcher, news_writer],
            tasks=[research_task, write_task],
            process=Process.sequential
        )
        result = crew.kickoff(inputs={'topic': topic})

    # Generate filename dynamically
    output_filename = sanitize_filename(topic)

    # Save the blog
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(str(result))

    # Display Blog in Right Box
    col1, col2 = st.columns([1, 2])  # Split into two columns

    with col1:
        st.subheader("✅ Blog Generation Completed!")
        st.success(f"Saved as: `{output_filename}`")

    with col2:
        st.subheader("📜 Generated Blog:")
        st.text_area("Blog Content", str(result), height=400)

    # Add a download button
    with open(output_filename, "rb") as file:
        st.download_button(
            label="📥 Download Blog",
            data=file,
            file_name=output_filename,
            mime="text/markdown"
        )

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Developed by **Shivam Mishra** 🚀")
