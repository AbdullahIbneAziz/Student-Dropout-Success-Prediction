from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Student Dropout Success Prediction Workflow')
dot.attr(rankdir='TB', size='11,8', dpi='300')

# Add nodes with custom styling
dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue', fontname='Arial')
dot.attr('edge', fontname='Arial')

# Data Collection and Preprocessing
dot.node('A', 'Data Collection\n(students_dropout_academic_success.csv)')
dot.node('B', 'Data Preprocessing\n- Handling missing values\n- Feature engineering\n- Data cleaning')
dot.edge('A', 'B')

# Exploratory Data Analysis
dot.node('C', 'Exploratory Data Analysis\n- Statistical analysis\n- Visualization\n- Feature correlation')
dot.edge('B', 'C')

# Model Development
dot.node('D', 'Model Development\n- Feature selection\n- Train-test split\n- Model training')
dot.edge('C', 'D')

# Model Evaluation
dot.node('E', 'Model Evaluation\n- Performance metrics\n- Cross-validation\n- Model comparison')
dot.edge('D', 'E')

# Results and Insights
dot.node('F', 'Results and Insights\n- Prediction analysis\n- Key findings\n- Recommendations')
dot.edge('E', 'F')

# Save the diagram
dot.render('workflow_diagram', format='png', cleanup=True) 