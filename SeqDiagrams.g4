grammar SeqDiagrams;

sequenceDiagram: SEQUENCE IDENTIFIER LBRACE lifeline* interaction* RBRACE;

lifeline: participant SEMI;

participant: actor | object | boundary | control | entity | database | diagramName;
diagramName: IDENTIFIER;
actor: ACTOR IDENTIFIER;
object: OBJECT objectName;
boundary: BOUNDARY IDENTIFIER;
control: CONTROL IDENTIFIER;
entity: ENTITY IDENTIFIER;
database: DATABASE IDENTIFIER;

objectName: objectOnly | objectClass | classOnly | classPackage | objectClassPackage;
objectOnly: IDENTIFIER COLON?;
objectClass: IDENTIFIER COLON IDENTIFIER;
classOnly: COLON IDENTIFIER;
classPackage: COLON IDENTIFIER DOUBLE_COLON IDENTIFIER;
objectClassPackage: IDENTIFIER COLON IDENTIFIER DOUBLE_COLON IDENTIFIER;

interaction: message | loop | conditional | optional | parallel | activation | deactivation;

message: synchronous | asynchronous | returnMessage | xsynchronous | twoWayAsync | timeout | bulking;

synchronous: IDENTIFIER ARROW IDENTIFIER COLON IDENTIFIER synchronousStereo? returnMessage? SEMI;
asynchronous: IDENTIFIER ASYNC IDENTIFIER COLON IDENTIFIER returnMessage? SEMI;
returnMessage: IDENTIFIER RETURN IDENTIFIER COLON IDENTIFIER returnStereo? SEMI;
xsynchronous: IDENTIFIER XSYNC IDENTIFIER COLON IDENTIFIER xsynchronousStereo? SEMI;
twoWayAsync: IDENTIFIER TWO_WAY_ASYNC IDENTIFIER COLON IDENTIFIER twoWayAsyncStereo? SEMI;
timeout: IDENTIFIER TIMEOUT IDENTIFIER COLON IDENTIFIER timeoutStereo? SEMI;
bulking: IDENTIFIER BULKING IDENTIFIER COLON IDENTIFIER bulkingStereo? SEMI;

loop: FOR LPAREN IDENTIFIER RPAREN LBRACE interaction* RBRACE | WHILE LPAREN IDENTIFIER RPAREN LBRACE interaction* RBRACE;
conditional: ALT LBRACE altCase+ RBRACE;
altCase: CASE LPAREN IDENTIFIER RPAREN LBRACE interaction* RBRACE;
optional: OPT LPAREN IDENTIFIER RPAREN LBRACE interaction* RBRACE;
parallel: PAR LBRACE interaction* RBRACE;

lifecycle: newObject | deleteObject;
newObject: IDENTIFIER NEW SEMI;
deleteObject: IDENTIFIER DELETE SEMI;
activation: IDENTIFIER ACTIVATE SEMI;
deactivation: IDENTIFIER DEACTIVATE SEMI;

note: NOTE LPAREN IDENTIFIER RPAREN COLON IDENTIFIER SEMI;
stereotype: STEREOTYPE;

synchronousStereo: STEREOTYPE;
returnStereo: STEREOTYPE;
xsynchronousStereo: STEREOTYPE;
twoWayAsyncStereo: STEREOTYPE;
timeoutStereo: STEREOTYPE;
bulkingStereo: STEREOTYPE;
asynchronousStereo: STEREOTYPE;

SEQUENCE: 'sequence';
ACTOR: 'actor';
OBJECT: 'object';
BOUNDARY: 'boundary';
CONTROL: 'control';
ENTITY: 'entity';
DATABASE: 'database';
FOR: 'for';
WHILE: 'while';
ALT: 'alt';
CASE: 'case';
OPT: 'opt';
PAR: 'par';
NEW: 'new';
DELETE: 'delete';
NOTE: 'note';
ACTIVATE: 'activate';
DEACTIVATE: 'deactivate';

ARROW: '->';
ASYNC: '=>';
RETURN: '-->';
XSYNC: '-x>';
TWO_WAY_ASYNC: '<->';
TIMEOUT: '-o>';
BULKING: '|<';

STEREOTYPE: '<<' ('call' | 'send' | 'create' | 'destroy' | 'return') '>>';

LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
COLON: ':';
SEMI: ';';
DOUBLE_COLON: '::';

IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;

WS: [ \t\n\r]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;