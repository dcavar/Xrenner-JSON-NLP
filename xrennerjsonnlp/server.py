from xrennerjsonnlp import XrennerPipeline
from pyjsonnlp.microservices.flask_server import FlaskMicroservice


class XrennerMicroservice(FlaskMicroservice):
    def __init__(self, import_name, pipeline: XrennerPipeline, base_route='/'):
        super().__init__(import_name, pipeline, base_route)
        self.add_url_rule(base_route + 'process_conll', view_func=self.run_process_conll, methods=['GET', 'POST'])
        self.pipeline: XrennerPipeline = pipeline

    def run_process_conll(self):
        return self.custom_process(self.pipeline.process_conll)


app = XrennerMicroservice(__name__, XrennerPipeline(), base_route='/')
app.with_constituents = False
app.with_coreferences = True
app.with_dependencies = True
app.with_expressions = True

if __name__ == "__main__":
    app.run(debug=True)
