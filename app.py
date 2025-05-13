from flask import Flask, render_template, request, jsonify, send_file
import io
import base64
import os
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from SeqDiagramsLexer import SeqDiagramsLexer
from SeqDiagramsParser import SeqDiagramsParser
from antlr4.tree.Trees import Trees
from antlr4 import ParseTreeWalker
from SeqDiagramsInterpreter import SequenceDiagramInterpreter
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('flowuml')

app = Flask(__name__, static_folder='static')

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.syntax_errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Line {line}:{column} - {msg}"
        self.syntax_errors.append(error_message)

@app.route('/')
def index():
    logger.info("Serving index page")
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    logger.info("Received diagram generation request")
    start_time = time.time()
    
    dsl_text = request.json.get('dsl_text', '')
    
    if not dsl_text.strip():
        logger.warning("Empty DSL text received")
        return jsonify({
            'success': False,
            'error': "Empty DSL text. Please enter sequence diagram code."
        })
    
    img_data = io.BytesIO()
    
    try:
        input_stream = InputStream(dsl_text)
        lexer = SeqDiagramsLexer(input_stream)
        
        error_listener = SyntaxErrorListener()
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)
        
        stream = CommonTokenStream(lexer)
        parser = SeqDiagramsParser(stream)
        
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        
        tree = parser.sequenceDiagram()
        
        if error_listener.syntax_errors:
            logger.warning(f"Syntax errors detected: {error_listener.syntax_errors}")
            return jsonify({
                'success': False,
                'error': "Syntax errors detected:\n" + "\n".join(error_listener.syntax_errors)
            })
        
        logger.info("Parsing successful. Building sequence diagram...")
        walker = ParseTreeWalker()
        interpreter = SequenceDiagramInterpreter()
        walker.walk(interpreter, tree)
        
        if interpreter.semantic_errors:
            logger.warning(f"Semantic errors detected: {interpreter.semantic_errors}")
            return jsonify({
                'success': False,
                'error': "Semantic errors detected:\n" + "\n".join(interpreter.semantic_errors)
            })
        
        fig = interpreter.visualizer.fig
        fig.savefig(img_data, format='png', bbox_inches='tight', dpi=120)
        img_data.seek(0)
        
        img_base64 = base64.b64encode(img_data.getvalue()).decode('utf-8')
        
        end_time = time.time()
        processing_time = round((end_time - start_time) * 1000)
        logger.info(f"Diagram generated successfully in {processing_time}ms")
        
        return jsonify({
            'success': True,
            'image': img_base64,
            'processing_time': processing_time
        })
        
    except Exception as e:
        import traceback
        error_traceback = traceback.format_exc()
        logger.error(f"Error generating diagram: {str(e)}\n{error_traceback}")
        return jsonify({
            'success': False,
            'error': f"Error generating diagram: {str(e)}",
            'traceback': error_traceback
        })

if __name__ == '__main__':
    logger.info("Starting FlowUML application")
    app.run(debug=True) 