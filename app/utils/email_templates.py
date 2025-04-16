def password_reset_html(name: str) -> str:
    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
      <head>
        <meta charset="UTF-8" />
        <title>Orçana - Redefinição de Senha</title>
        <style>
          body {{
            font-family: 'Segoe UI', sans-serif;
            background-color: #f6f8fa;
            padding: 40px 20px;
            color: #2c3e50;
          }}
          .container {{
            max-width: 500px;
            margin: 0 auto;
            background-color: white;
            border-radius: 8px;
            padding: 32px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
          }}
          .logo {{
            font-weight: bold;
            font-size: 24px;
            color: #2980b9;
            margin-bottom: 24px;
          }}
          .title {{
            font-size: 20px;
            margin-bottom: 12px;
          }}
          .text {{
            font-size: 16px;
            line-height: 1.6;
            margin-bottom: 24px;
          }}
          .footer {{
            font-size: 12px;
            color: #7f8c8d;
            margin-top: 32px;
            text-align: center;
          }}
        </style>
      </head>
      <body>
        <div class="container">
          <div class="logo">Orçana</div>
          <div class="title">Senha redefinida com sucesso!</div>

          <div class="text">
            Olá, <strong>{name}</strong>! Sua senha foi atualizada com sucesso em nossa plataforma.<br />
            Se você não realizou essa alteração, entre em contato imediatamente com nosso suporte.
          </div>

          <div class="text">
            Caso tenha sido você, pode ignorar este e-mail e continuar usando o sistema normalmente.
          </div>

          <div class="footer">
            Este é um e-mail automático da Orçana. Por favor, não responda.
          </div>
        </div>
      </body>
    </html>
    """
