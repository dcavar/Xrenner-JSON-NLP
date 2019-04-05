from xrennerjsonnlp import XrennerPipeline
from pyjsonnlp.microservices.flask_server import FlaskMicroservice

app = FlaskMicroservice(__name__, XrennerPipeline(), base_route='/')
app.with_constituents = False
app.with_coreferences = True
app.with_dependencies = True
app.with_expressions = True

if __name__ == "__main__":
    app.run(debug=True)