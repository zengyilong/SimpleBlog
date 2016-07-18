from app import create_app


app = create_app()

if __name__ == '__main__':
    from app.models import init_db
    init_db()
    app.run()
