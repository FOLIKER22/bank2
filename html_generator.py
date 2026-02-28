def generate_html(user, user_accounts):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Кабінет користувача</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f4f4f4;
                padding: 40px;
            }}
            .card {{
                background: white;
                padding: 20px;
                margin: 10px 0;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
        </style>
    </head>
    <body>
        <h1>Вітаємо, {user.username} 👋</h1>
        <h2>Ваші рахунки:</h2>
    """

    for acc in user_accounts:
        html_content += f"""
        <div class="card">
            <h3>Тип: {acc.__class__.__name__}</h3>
            <p>Баланс: {acc.get_balance()} грн</p>
            <p>Відсотки: {acc.calculate_interest()} грн</p>
        </div>
        """

    html_content += """
    </body>
    </html>
    """

    with open("dashboard.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ dashboard.html створено!")
