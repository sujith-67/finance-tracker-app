import streamlit as st
from datetime import date

from database import create_table, insert_transaction, delete_transaction
from analysis import load_data
from utils import CATEGORIES, INCOME_CATEGORIES
from charts import plot_category, plot_monthly, plot_income_vs_expense

# =========================
# INIT
# =========================
create_table()

st.title("💰 Personal Finance Tracker")

# =========================
# ➕ ADD TRANSACTION
# =========================
st.header("➕ Add Transaction")

col1, col2 = st.columns(2)

with col1:
    type_ = st.selectbox("Type", ["Income", "Expense"])
    amount = st.number_input(
    "Amount",
    min_value=0.0,
    step=500.0
)

with col2:
    if type_ == "Expense":
        main_category = st.selectbox("Main Category", list(CATEGORIES.keys()))
        sub_category = st.selectbox("Sub Category", CATEGORIES[main_category])
    else:
       sub_category = st.selectbox("Income Category", INCOME_CATEGORIES)

tags = st.text_input("Tags (optional)")
date_input = st.date_input("Date", value=date.today())

if st.button("Add Transaction"):
    if amount > 0:
        insert_transaction(type_, amount, sub_category, tags, str(date_input))
        st.success("Transaction Added ✅")
        st.rerun()
    else:
        st.error("Amount must be greater than 0")

# =========================
# 📊 LOAD DATA
# =========================
df = load_data()

if df.empty:
    st.info("No transactions yet. Add some data 👆")
    st.stop()
# =========================
# 🔍 FILTERS
# =========================
st.header("🔍 Filters")

col1, col2 = st.columns(2)

with col1:
    selected_type = st.selectbox("Type", ["All", "Income", "Expense"])

with col2:
    selected_category = st.selectbox(
        "Category",
        ["All"] + list(df["category"].unique())
    )

filtered_df = df.copy()

if selected_type != "All":
    filtered_df = filtered_df[filtered_df["type"] == selected_type]

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["category"] == selected_category]

# =========================
# 📈 SUMMARY
# =========================
st.header("📈 Summary")

income = filtered_df[filtered_df["type"] == "Income"]["amount"].sum()
expense = filtered_df[filtered_df["type"] == "Expense"]["amount"].sum()
balance = income - expense

c1, c2, c3 = st.columns(3)
c1.metric("Income", income)
c2.metric("Expense", expense)
c3.metric("Balance", balance)

# =========================
# 📋 TRANSACTIONS TABLE
# =========================
st.header("📋 Transactions")

st.dataframe(filtered_df, use_container_width=True)

# =========================
# ❌ DELETE
# =========================
st.subheader("Delete Transaction")

txn_id = st.number_input("Enter ID to delete", step=1)

if st.button("Delete"):
    delete_transaction(txn_id)
    st.success("Deleted ✅")
    st.rerun()

# =========================
# 📊 CHARTS (EXPENSE ONLY)
# =========================
# =========================
# 📊 CHARTS
# =========================
st.header("📊 Charts")

# 🔥 Income vs Expense (BAR)
st.subheader("💰 Income vs Expense")

st.pyplot(plot_income_vs_expense(filtered_df))


# 🔹 Expense Charts (existing ones)
expense_df = filtered_df[filtered_df["type"] == "Expense"]

if not expense_df.empty:
    col1, col2 = st.columns(2)

    with col1:
        st.pyplot(plot_category(expense_df))

    with col2:
        st.pyplot(plot_monthly(expense_df))
else:
    st.info("No expense data to display charts")