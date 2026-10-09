
import streamlit as st

from config import validate_config
from rag_pipeline import process_pdfs, answer_question

st.set_page_config(
    page_title="Smart StudyMate",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Smart StudyMate")
st.caption(
    "Your AI-powered college study assistant"
)

# Session state
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "indexed_files" not in st.session_state:
    st.session_state.indexed_files = []

# Sidebar
with st.sidebar:
    st.header("Upload Study Materials")

    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("Process Documents", type="primary"):
        if not uploaded_files:
            st.warning("Upload at least one PDF.")
        else:
            try:
                validate_config()

                with st.spinner(
                    "Extracting text and creating embeddings..."
                ):
                    vectorstore, chunk_count = process_pdfs(
                        uploaded_files
                    )

                st.session_state.vectorstore = vectorstore
                st.session_state.indexed_files = [
                    file.name for file in uploaded_files
                ]
                st.session_state.messages = []

                st.success(
                    f"Indexed {chunk_count} text chunks "
                    f"from {len(uploaded_files)} PDFs."
                )

            except Exception as error:
                st.error(f"Document processing failed: {error}")

    if st.session_state.indexed_files:
        st.subheader("Indexed documents")
        for filename in st.session_state.indexed_files:
            st.write(f"📄 {filename}")

    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()

    st.caption(
        "Only ask questions about documents you have indexed."
    )

# Chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("sources"):
            with st.expander("View source passages"):
                for source in message["sources"]:
                    st.markdown(
                        f"**{source['filename']} — "
                        f"page {source['page']}**"
                    )
                    st.write(source["text"])

# Question input
question = st.chat_input(
    "Ask a question about your notes..."
)

if question:
    if st.session_state.vectorstore is None:
        st.warning("Upload and process your PDFs first.")
        st.stop()

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Searching your study materials..."):
                answer, sources, retrieved_docs = answer_question(
                    st.session_state.vectorstore,
                    question
                )

            st.markdown(answer)

            with st.expander("View retrieved source passages"):
                for index, document in enumerate(
                    retrieved_docs, start=1
                ):
                    filename = document.metadata.get(
                        "source", "Unknown file"
                    )

                    page = document.metadata.get("page")
                    page_number = (
                        page + 1 if isinstance(page, int)
                        else "Unknown"
                    )

                    st.markdown(
                        f"**Passage {index}: {filename}, "
                        f"page {page_number}**"
                    )
                    st.write(document.page_content)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "sources": sources
            })

        except Exception as error:
            st.error(f"Could not answer the question: {error}")
