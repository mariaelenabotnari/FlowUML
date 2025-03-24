grammar SeqDiagrams;

// Parser rules
sequenceDiagram: SEQUENCE STRING LBRACE lifeline* interaction* RBRACE;

lifeline: participant SEMI;

participant: actor | object | boundary | control | entity | database | diagramName;
diagramName: STRING;
actor: ACTOR STRING;
object: OBJECT objectName;
boundary: BOUNDARY STRING;
control: CONTROL STRING;
entity: ENTITY STRING;
database: DATABASE STRING;

objectName: objectOnly | objectClass | classOnly | classPackage | objectClassPackage;
objectOnly: STRING COLON?;
objectClass: STRING COLON STRING;
classOnly: COLON STRING;
classPackage: COLON STRING DOUBLE_COLON STRING;
objectClassPackage: STRING COLON STRING DOUBLE_COLON STRING;

interaction: message | loop | conditional | optional | parallel | activation | deactivation;

message: synchronous | asynchronous | returnMessage | xsynchronous | twoWayAsync | timeout | bulking;

synchronous: STRING ARROW STRING COLON STRING synchronousStereo? returnMessage? SEMI;
asynchronous: STRING ASYNC STRING COLON STRING returnMessage? SEMI;
returnMessage: STRING RETURN STRING COLON STRING returnStereo? SEMI;
xsynchronous: STRING XSYNC STRING COLON STRING xsynchronousStereo? SEMI;
twoWayAsync: STRING TWO_WAY_ASYNC STRING COLON STRING twoWayAsyncStereo? SEMI;
timeout: STRING TIMEOUT STRING COLON STRING timeoutStereo? SEMI;
bulking: STRING BULKING STRING COLON STRING bulkingStereo? SEMI;

loop: FOR LPAREN STRING RPAREN LBRACE interaction* RBRACE | WHILE LPAREN STRING RPAREN LBRACE interaction* RBRACE;
conditional: ALT LBRACE altCase+ RBRACE;
altCase: CASE LPAREN STRING RPAREN LBRACE interaction* RBRACE;
optional: OPT LPAREN STRING RPAREN LBRACE interaction* RBRACE;
parallel: PAR LBRACE interaction* RBRACE;

lifecycle: newObject | deleteObject;
newObject: STRING NEW SEMI;
deleteObject: STRING DELETE SEMI;
activation: STRING ACTIVATE SEMI;
deactivation: STRING DEACTIVATE SEMI;

note: NOTE LPAREN STRING RPAREN COLON STRING SEMI;
stereotype: STEREOTYPE;

synchronousStereo: STEREOTYPE;
returnStereo: STEREOTYPE;
xsynchronousStereo: STEREOTYPE;
twoWayAsyncStereo: STEREOTYPE;
timeoutStereo: STEREOTYPE;
bulkingStereo: STEREOTYPE;
asynchronousStereo: STEREOTYPE;

// Lexer rules
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

STRING: [a-zA-Z_][a-zA-Z_0-9]*;

WS: [ \t\n\r]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;