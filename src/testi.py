
            from sqlalchemy import create_engine
            from sqlalchemy.exc import SQLAlchemyError
            engine = create_engine("mysql+mysqldb://userid:password@localhost/login_information")