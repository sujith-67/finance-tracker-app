import matplotlib.pyplot as plt


# =========================
# 📊 CATEGORY SPENDING (BAR)
# =========================
def plot_category(df):
    data = df.groupby("category")["amount"].sum()

    fig, ax = plt.subplots(figsize=(6, 4))

    data.plot(
        kind="bar",
        ax=ax,
        color="skyblue",
        edgecolor="black"
    )

    ax.set_title("💸 Spending by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount")

    ax.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(rotation=30)

    plt.tight_layout()
    return fig


# =========================
# 📈 MONTHLY SPENDING TREND
# =========================
def plot_monthly(df):
    data = df.groupby(df["date"].dt.month)["amount"].sum()

    fig, ax = plt.subplots(figsize=(6, 4))

    data.plot(
        kind="line",
        marker="o",
        ax=ax
    )

    ax.set_title("📅 Monthly Spending Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount")

    ax.set_xticks(range(1, 13))  # clean month axis
    ax.grid(True, linestyle="--", alpha=0.7)

    plt.tight_layout()
    return fig


# =========================
# 💰 INCOME vs EXPENSE (BAR)
# =========================
def plot_income_vs_expense(df):
    summary = df.groupby("type")["amount"].sum()

    fig, ax = plt.subplots(figsize=(5, 4))

    summary.plot(
        kind="bar",
        ax=ax,
        color=["green", "red"]
    )

    ax.set_title("💰 Income vs Expense")
    ax.set_ylabel("Amount")

    plt.tight_layout()
    return fig


# =========================
# 🥧 INCOME vs EXPENSE (PIE)
# =========================
def plot_income_expense_pie(df):
    summary = df.groupby("type")["amount"].sum()

    fig, ax = plt.subplots()

    ax.pie(
        summary,
        labels=summary.index,
        autopct="%1.1f%%",
        colors=["green", "red"]
    )

    ax.set_title("Income vs Expense Ratio")

    return fig


# =========================
# 📊 MONTHLY INCOME vs EXPENSE
# =========================
def plot_monthly_income_expense(df):
    df["month"] = df["date"].dt.month

    summary = df.groupby(["month", "type"])["amount"].sum().unstack()

    fig, ax = plt.subplots(figsize=(6, 4))

    summary.plot(ax=ax, marker="o")

    ax.set_title("📈 Monthly Income vs Expense")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount")

    ax.set_xticks(range(1, 13))
    ax.grid(True, linestyle="--", alpha=0.7)

    plt.tight_layout()
    return fig