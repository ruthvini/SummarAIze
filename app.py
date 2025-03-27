import streamlit as st
from sum import extract_text_from_pdf, summarize_text

# Streamlit UI
st.title("SummarAIze✨")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract Text
    extracted_text = extract_text_from_pdf("temp.pdf")

    if extracted_text:
        st.subheader("Extracted Text Preview:")
        st.text_area("", extracted_text[:1000] + "...", height=200)

        # Summarize Text
        if st.button("Summarize"):
            summary = summarize_text(extracted_text)
            st.subheader("📌 Summary:")
            st.write(summary)
    else:
        st.warning("Could not extract text. The PDF may be scanned (image-based).")
