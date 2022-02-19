from config import app
from layout import make_layout

if __name__ == "__main__":
    app.layout = make_layout()
    app.run_server(debug=True)
