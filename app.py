# app.py
import web
import redis

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

class Index:
    def GET(self):
        return """
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Calculadora</title>
            </head>
            <body>
                <h2>Calculadora</h2>
                <form action="/" method="post">
                    <label for="num1">Número 1:</label>
                    <input type="number" id="num1" name="num1" required><br>
                    <label for="num2">Número 2:</label>
                    <input type="number" id="num2" name="num2" required><br>
                    <input type="submit" value="Sumar">
                </form>
            </body>
            </html>
        """

    def POST(self):
        data = web.input()
        num1 = int(data.num1)
        num2 = int(data.num2)
        suma = num1 + num2
        return f"La suma de {num1} y {num2} es: {suma}"

if __name__ == "__main__":
    app.run()