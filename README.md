# FlowUML - Professional Sequence Diagram Designer

FlowUML is a modern web-based tool for creating sequence diagrams using a domain-specific language. It offers an intuitive interface with real-time diagram generation.

![FlowUML Screenshot](https://i.imgur.com/MXz9s9h.png)

## Features

- **Professional Editor**: Line numbers, syntax highlighting, and clear error messages
- **Real-time Visualization**: Generate diagrams instantly with a single click
- **Modern UI**: Clean, responsive design that adapts to different screen sizes
- **Error Handling**: Detailed syntax and semantic error reporting 
- **Export Capability**: Download diagrams as high-quality PNG images

## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your browser and navigate to `http://localhost:5000`

## Using the DSL

FlowUML supports a comprehensive set of sequence diagram elements:

### Participant Types
```
actor User;
object Client;
boundary UI;
control Controller;
entity Order;
database Database;
```

### Message Types
```
User -> UI : Normal_message;
UI => Controller : Asynchronous_message;
Database --> Controller : Return_message;
Controller -x> UI : Destruction_message;
Controller <-> Order : Two_way_message;
Controller -o> Database : Timeout_message;
Database |< Controller : Bulk_data_message;
```

### Control Structures
```
for (condition) {
    messages
}

alt {
    case (condition1) {
        messages
    }
    case (condition2) {
        messages
    }
}

opt (condition) {
    messages
}
```

### Activation & Deactivation
```
Controller activate;
messages
Controller deactivate;
```

## Example
Click the "Example" button in the UI to see a comprehensive example that demonstrates all the DSL features. The example includes different participant types, message types, control structures, and activation/deactivation.

## Implementation Details

FlowUML is built with:
- Python and Flask for the backend
- ANTLR4 for the DSL parser
- Matplotlib for diagram generation
- Modern HTML, CSS, and JavaScript for the frontend

## Notes
- Messages must use underscores instead of spaces (e.g., "Submit_form" not "Submit form")
- Each statement must end with a semicolon (;)
- Participants must be declared before they are used