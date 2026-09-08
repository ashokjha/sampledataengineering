import streamlit as st


class Loader:
    @staticmethod
    def show_top_loader():
        st.markdown(
            """
            <style>
            /* fit the spinner*/
            div[data-testid="stSpinner"] {
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                z-index: 999999;
                background-color: rgba(255, 255, 255, 0.9);
                padding: 20px 40px;
                border-radius: 10px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                width: fit-content;
                text-align: center;
            }
            /* For Dark Mode */
            @media (prefers-color-scheme: dark) {
                div[data-testid="stSpinner"] {
                    background-color: rgba(14, 18, 36, 0.9);
                    color: white;
                }
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
