"""
Sequence Diagram Visualizer (Bottom-to-Top Layout)
This visualizer creates sequence diagrams with the following characteristics:
- Participants are positioned at the bottom of the diagram
- Lifelines run vertically up the diagram
- Messages are drawn horizontally between lifelines
- A timeline is shown on the left side to indicate progression upward
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import numpy as np
from matplotlib.colors import to_rgba

class SequenceDiagramVisualizer:
    def __init__(self):
        plt.style.use('ggplot')  # Use a nicer style
        self.fig, self.ax = plt.subplots(figsize=(10, 8), facecolor='#FAFAFA')  # Reduce height from 14 to 8
        self.participants = {}  # name -> x_position
        self.messages = []      # (source, target, message, msg_type, y)
        self.activations = {}   # name -> list of (start_y, end_y)
        self.title = ""
        self.control_blocks = [] # (type, label, start_y, end_y, x1, x2)
        
        # Bottom-to-top layout metrics
        self.diagram_height = 8  # Reduce total height from 15 to 8
        self.current_y = self.diagram_height - 2  # Adjust starting position
        self.y_step = -0.8      # Reduce y-step from -2.0 to -0.8 for more compact spacing
        self.x_padding = 3      # Horizontal spacing between participants
        self.notes = []         # (text, y)
        self.participant_types = {}  # name -> type
        
        # Define colors for different types
        self.participant_colors = {
            "actor": "#E1F5FE",      # Light blue
            "boundary": "#E8F5E9",   # Light green
            "control": "#F3E5F5",    # Light purple
            "entity": "#FFF3E0",     # Light orange
            "database": "#E0F2F1",   # Light teal
            "object": "#F5F5F5",     # Light grey
            "participant": "#E0F7FA" # Light cyan
        }

    def add_participant(self, name, type_="participant"):
        """Add a participant to the diagram"""
        if name not in self.participants:
            x_pos = len(self.participants) * self.x_padding + 3  # Start more to the right
            self.participants[name] = x_pos
            self.participant_types[name] = type_
            # Store the type for coloring
            self.participant_colors.setdefault(name, 
                self.participant_colors.get(type_, self.participant_colors["participant"]))

    def add_message(self, source, target, message, msg_type="->"):
        """Add a message between participants"""
        if source not in self.participants or target not in self.participants:
            return
        self.current_y += self.y_step  # Move upward
        self.messages.append((source, target, message, msg_type, self.current_y))
        
        # Automatically add activation for synchronous messages
        if msg_type == "->":
            self.add_activation(target)

    def add_activation(self, participant, start_y=None):
        """Add an activation bar for a participant"""
        if participant not in self.participants:
            return
        if start_y is None:
            start_y = self.current_y
        if participant not in self.activations:
            self.activations[participant] = []
        self.activations[participant].append([start_y, None])

    def end_activation(self, participant):
        """End the latest activation for a participant"""
        if participant in self.activations and self.activations[participant]:
            start_y, _ = self.activations[participant][-1]
            self.activations[participant][-1][1] = self.current_y

    def add_note(self, text):
        """Add a note to the diagram"""
        self.current_y += self.y_step / 2  # Reduce spacing before notes
        self.notes.append((text, self.current_y))
        self.current_y += self.y_step / 8  # Reduce additional movement

    def set_title(self, title):
        """Set the diagram title"""
        self.title = title

    def draw(self):
        """Draw the sequence diagram"""
        plt.close('all')  # Close any previous figures
        self.fig, self.ax = plt.subplots(figsize=(10, 8), facecolor='#FAFAFA')
        n = len(self.participants)
        if n == 0:
            return self.fig
        
        # Find the minimum y-coordinate for lifelines (highest point)
        lifeline_top = min(self.current_y - 2, 1)
        
        # Draw participant boxes at the bottom of the diagram
        participants_y = self.diagram_height - 1  # Position at bottom
        
        for name, x in self.participants.items():
            participant_type = self.participant_types.get(name, "participant")
            
            # Draw shadow for 3D effect
            shadow = patches.FancyBboxPatch((x-1.2, participants_y-0.1), 2.4, 1.2, 
                                         boxstyle="round,pad=0.2", 
                                         facecolor='#CCCCCC', 
                                         alpha=0.5, 
                                         zorder=1)
            self.ax.add_patch(shadow)
            
            # Draw main box
            box = patches.FancyBboxPatch((x-1, participants_y), 2, 1, 
                                      boxstyle="round,pad=0.2", 
                                      facecolor=self.participant_colors.get(name, '#E0F7FA'),
                                      edgecolor='#555555',
                                      linewidth=1.5,
                                      zorder=2)
            self.ax.add_patch(box)
            
            # Add participant icons based on type
            if participant_type == "actor":
                # Draw stick figure for actor
                # Head
                circle = patches.Circle((x, participants_y+0.7), radius=0.15, 
                                     facecolor='white', edgecolor='black', 
                                     linewidth=1.2, zorder=3)
                self.ax.add_patch(circle)
                # Body
                self.ax.plot([x, x], [participants_y+0.55, participants_y+0.2], 'k-', linewidth=1.2, zorder=3)
                # Arms
                self.ax.plot([x-0.2, x+0.2], [participants_y+0.4, participants_y+0.4], 'k-', linewidth=1.2, zorder=3)
                # Legs
                self.ax.plot([x-0.2, x], [participants_y+0.1, participants_y+0.2], 'k-', linewidth=1.2, zorder=3)
                self.ax.plot([x, x+0.2], [participants_y+0.2, participants_y+0.1], 'k-', linewidth=1.2, zorder=3)
                # Add name below
                self.ax.text(x, participants_y+0.1, name, ha='center', va='top', fontsize=9, fontweight='bold')
            
            elif participant_type == "database":
                # Draw database cylinder
                cylinder_top = patches.Ellipse((x, participants_y+0.75), 
                                          width=1.5, height=0.3, 
                                          facecolor='white', edgecolor='black', 
                                          linewidth=1.2, zorder=3)
                self.ax.add_patch(cylinder_top)
                
                # Draw sides
                self.ax.plot([x-0.75, x-0.75], [participants_y+0.75, participants_y+0.25], 
                          'k-', linewidth=1.2, zorder=3)
                self.ax.plot([x+0.75, x+0.75], [participants_y+0.75, participants_y+0.25], 
                          'k-', linewidth=1.2, zorder=3)
                
                # Draw bottom
                cylinder_bottom = patches.Ellipse((x, participants_y+0.25), 
                                             width=1.5, height=0.3, 
                                             facecolor='white', edgecolor='black', 
                                             linewidth=1.2, zorder=3)
                self.ax.add_patch(cylinder_bottom)
                
                # Add name inside
                self.ax.text(x, participants_y+0.5, name, ha='center', va='center', 
                          fontsize=9, fontweight='bold')
                
            else:
                # Default text for other types
                self.ax.text(x, participants_y+0.5, name, ha='center', va='center', 
                          fontsize=10, fontweight='bold')
        
        # Add a horizontal separator line above participants to emphasize bottom-to-top flow
        self.ax.plot([0, n * self.x_padding + 6], [participants_y-0.2, participants_y-0.2], 
                  color='#AAAAAA', 
                  linestyle='-', 
                  linewidth=0.5, 
                  alpha=0.5,
                  zorder=1)
            
        # Draw lifelines vertically from participants (going up)
        for x in self.participants.values():
            # Draw dashed line with gradient alpha
            for i in range(100):
                y_start = participants_y - 1 - i * (participants_y - lifeline_top - 1) / 100
                y_end = participants_y - 1 - (i + 1) * (participants_y - lifeline_top - 1) / 100
                alpha = 0.6 - (i / 100) * 0.3  # Gradually reduce alpha
                self.ax.plot([x, x], [y_start, y_end], 'k--', alpha=alpha, linewidth=1.2, zorder=1)
            
        # Draw activations along lifelines
        for participant, acts in self.activations.items():
            x = self.participants[participant]
            for start_y, end_y in acts:
                if end_y is not None:
                    width = 0.4
                    # For bottom-to-top, the end_y is smaller than start_y
                    if end_y > start_y:  # Swap if needed
                        start_y, end_y = end_y, start_y
                    height = abs(end_y - start_y)
                    # Skip very short activations
                    if height < 0.2:
                        height = 0.2
                        
                    # Draw shadow
                    shadow = patches.Rectangle((x - width/2 + 0.05, end_y + 0.05), 
                                            width, 
                                            height,
                                            facecolor='#AAAAAA', 
                                            alpha=0.5, 
                                            zorder=2)
                    self.ax.add_patch(shadow)
                    
                    # Draw activation
                    activation = patches.Rectangle((x - width/2, end_y), 
                                               width, 
                                               height,
                                               facecolor='#A5D6A7', 
                                               edgecolor='#388E3C',
                                               linewidth=1.2,
                                               alpha=0.9, 
                                               zorder=3)
                    self.ax.add_patch(activation)
                    
        # Draw messages
        for source, target, message, msg_type, y in self.messages:
            x1 = self.participants[source]
            x2 = self.participants[target]
            
            # Style based on message type
            if msg_type == '->':
                style = dict(arrowstyle='->', color='#333333', lw=1.5, zorder=4)
            elif msg_type == '-->':
                style = dict(arrowstyle='->', color='#333333', lw=1.5, zorder=4, linestyle='dashed')
            elif msg_type == '->>':
                style = dict(arrowstyle='->', color='#0D47A1', lw=1.8, zorder=4)
                # For create messages, add a special marker
                if x1 != x2:  # Only if not self-message
                    self.ax.text(x2, y+0.3, "«create»", 
                             ha='center', va='bottom', 
                             fontsize=8, 
                             color='#0D47A1',
                             fontstyle='italic')
            elif msg_type == '-x>':
                style = dict(arrowstyle='->', color='#E53935', lw=1.5, zorder=4)
                # Add 'X' marker for destruction messages
                self.ax.plot([x2-0.2, x2+0.2], [y-0.2, y+0.2], color='#E53935', lw=1.5, zorder=5)
                self.ax.plot([x2-0.2, x2+0.2], [y+0.2, y-0.2], color='#E53935', lw=1.5, zorder=5)
            elif msg_type == '<->':
                # Two-way arrow - draw special bidirectional arrow
                style = dict(arrowstyle='<->', color='#9C27B0', lw=1.5, zorder=4)
            elif msg_type == '-o>':
                # Timeout arrow
                style = dict(arrowstyle='->', color='#FF9800', lw=1.5, zorder=4)
                # Add a small circle to indicate timeout
                circle = patches.Circle((x1 + 0.8 * (x2 - x1), y), radius=0.15, 
                                    facecolor='#FFF3E0', edgecolor='#FF9800', 
                                    linewidth=1.5, zorder=5)
                self.ax.add_patch(circle)
            elif msg_type == '|<':
                # Bulking arrow (data transfer)
                style = dict(arrowstyle='<-', color='#2E7D32', lw=1.5, zorder=4)
                # Add vertical line for bulk data
                self.ax.plot([x2-0.2, x2-0.2], [y-0.3, y+0.3], color='#2E7D32', lw=2.5, zorder=5)
            
            # Handle self-messages with curved arrows
            if x1 == x2:
                # Create curved arrow for self messages
                path = [
                    (x1, y),              # Start
                    (x1 + 0.8, y),        # Control point out
                    (x1 + 0.8, y - 0.5),  # Control point up (direction reversed)
                    (x1, y - 0.5)         # End
                ]
                
                verts = path
                codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
                
                path = Path(verts, codes)
                patch = patches.PathPatch(path, facecolor='none', edgecolor='black', lw=1.5, zorder=4)
                self.ax.add_patch(patch)
                
                # Add arrow head 
                self.ax.annotate('', xy=(x1, y-0.5), xytext=(x1+0.1, y-0.5),
                             arrowprops=dict(arrowstyle='->', lw=1.5, color='black'), zorder=5)
                             
                # Position self-message text
                self.ax.text(x1 + 1.2, y - 0.25, message, 
                          ha='center', va='center', 
                          fontsize=9, 
                          color='#333333',
                          bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.2', edgecolor='none'))
            else:
                # Draw regular message arrow
                self.ax.annotate('', xy=(x2, y), xytext=(x1, y), arrowprops=style)
                
                # Draw message label
                self.ax.text((x1 + x2) / 2, y + 0.3, message, 
                          ha='center', va='center', 
                          fontsize=9,
                          color='#333333',
                          bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.2', edgecolor='none'))
            
        # Draw notes on the right side
        # Define a placeholder for timeline_x (previous code removed it)
        timeline_x = 0.5
        
        for text, y in self.notes:
            note_width = 4
            note_height = 1
            note_x = n * self.x_padding + 2
            
            # Draw shadow
            shadow = patches.FancyBboxPatch((note_x+0.1, y-note_height/2+0.1), 
                                         note_width, note_height, 
                                         boxstyle="round,pad=0.3", 
                                         facecolor='#BBBBBB', 
                                         alpha=0.5, 
                                         zorder=1)
            self.ax.add_patch(shadow)
            
            # Draw note
            note_box = patches.FancyBboxPatch((note_x, y-note_height/2), 
                                           note_width, note_height, 
                                           boxstyle="round,pad=0.3", 
                                           facecolor='#FFF9C4', 
                                           edgecolor='#FBC02D',
                                           linewidth=1.2,
                                           zorder=2)
            self.ax.add_patch(note_box)
            
            # Add folded corner effect
            corner_x = note_x + note_width - 0.3
            corner_y = y - note_height/2
            self.ax.plot([corner_x, corner_x], [corner_y, corner_y+0.3], 
                      color='#FBC02D', linewidth=1, zorder=3)
            self.ax.plot([corner_x-0.3, corner_x], [corner_y+0.3, corner_y+0.3], 
                      color='#FBC02D', linewidth=1, zorder=3)
            
            # Draw note text
            self.ax.text(note_x + note_width/2, y, text, 
                      ha='center', va='center', 
                      fontsize=9, 
                      color='#333333')
            
            # Draw a line to the note (no longer from timeline)
            self.ax.plot([1, note_x], [y, y], 
                      ':', color='#AAAAAA', linewidth=1, alpha=0.5, zorder=1)
            
        # Draw control blocks (alt, loop, opt) 
        for block_type, label, start_y, end_y, x_min, x_max in self.control_blocks:
            if end_y is None:  # Skip incomplete blocks
                continue
                
            # Draw the box
            if block_type == "alt":
                # Alt block in PlantUML style with angles at top corners
                color = "#FFD966"  # Light gold
                edge_color = "#E6B800"  # Darker gold
                alpha = 0.2
                
                # Draw box
                box = patches.Rectangle((x_min, end_y), 
                                    x_max - x_min, start_y - end_y,
                                    facecolor=color, 
                                    edgecolor=edge_color,
                                    linewidth=1.5,
                                    alpha=alpha,
                                    zorder=0)
                self.ax.add_patch(box)
                
                # Add label at top
                header_box = patches.Rectangle((x_min, start_y - 0.5), 
                                          2.5, 0.5,
                                          facecolor=color, 
                                          edgecolor=edge_color,
                                          linewidth=1.5,
                                          alpha=alpha+0.1,
                                          zorder=1)
                self.ax.add_patch(header_box)
                
                self.ax.text(x_min + 1.25, start_y - 0.25, f"alt {label}", 
                         ha='center', va='center', 
                         fontsize=9, 
                         fontweight='bold',
                         color='#333333')
                
            elif block_type == "loop":
                # Loop block
                color = "#C6E2FF"  # Light blue
                edge_color = "#9ACDFF"  # Blue
                alpha = 0.2
                
                # Draw box
                box = patches.Rectangle((x_min, end_y), 
                                    x_max - x_min, start_y - end_y,
                                    facecolor=color, 
                                    edgecolor=edge_color,
                                    linewidth=1.5,
                                    alpha=alpha,
                                    zorder=0)
                self.ax.add_patch(box)
                
                # Add label at top
                header_box = patches.Rectangle((x_min, start_y - 0.5), 
                                          2.5, 0.5,
                                          facecolor=color, 
                                          edgecolor=edge_color,
                                          linewidth=1.5,
                                          alpha=alpha+0.1,
                                          zorder=1)
                self.ax.add_patch(header_box)
                
                self.ax.text(x_min + 1.25, start_y - 0.25, f"loop {label}", 
                         ha='center', va='center', 
                         fontsize=9, 
                         fontweight='bold',
                         color='#333333')
                
            elif block_type == "opt":
                # Optional block
                color = "#E0E0E0"  # Light gray
                edge_color = "#AAAAAA"  # Gray
                alpha = 0.2
                
                # Draw box
                box = patches.Rectangle((x_min, end_y), 
                                    x_max - x_min, start_y - end_y,
                                    facecolor=color, 
                                    edgecolor=edge_color,
                                    linewidth=1.5,
                                    alpha=alpha,
                                    zorder=0)
                self.ax.add_patch(box)
                
                # Add label at top
                header_box = patches.Rectangle((x_min, start_y - 0.5), 
                                          2.5, 0.5,
                                          facecolor=color, 
                                          edgecolor=edge_color,
                                          linewidth=1.5,
                                          alpha=alpha+0.1,
                                          zorder=1)
                self.ax.add_patch(header_box)
                
                self.ax.text(x_min + 1.25, start_y - 0.25, f"opt {label}", 
                         ha='center', va='center', 
                         fontsize=9, 
                         fontweight='bold',
                         color='#333333')
        
        # Title at the top of the diagram
        #if self.title:
        #    title_width = n * self.x_padding + 6
        #    title_patch = patches.FancyBboxPatch((0, 0), 
        #                                      title_width, 0.7, 
        #                                      boxstyle="round,pad=0.3", 
        #                                      facecolor='#BBDEFB', 
        #                                      edgecolor='#1976D2',
        #                                      linewidth=1.2,
        #                                      alpha=0.7,
        #                                      zorder=1)
        #    self.ax.add_patch(title_patch)
        #    self.ax.text(title_width/2, 0.35, self.title, 
        #              ha='center', va='center', 
        #              fontsize=14, 
        #              fontweight='bold', 
        #              color='#0D47A1')
        
        # Add a clear "Bottom-to-Top Flow" indicator
        #flow_indicator = patches.FancyBboxPatch((n * self.x_padding + 2, participants_y-0.9), 
        #                                    3, 1.2, 
        #                                    boxstyle="round,pad=0.2", 
        #                                    facecolor='#E8F5E9', 
        #                                    edgecolor='#66BB6A',
        #                                    linewidth=1,
        #                                    alpha=0.8,
        #                                    zorder=5)
        #self.ax.add_patch(flow_indicator)
        #self.ax.text(n * self.x_padding + 3.5, participants_y-0.6, "Bottom-to-Top", 
        #          ha='center', va='center', 
        #          fontsize=9, 
        #          fontweight='bold',
        #          color='#333333')
        #self.ax.text(n * self.x_padding + 3.5, participants_y-0.1, "↑", 
        #          ha='center', va='center', 
        #          fontsize=14, 
        #          fontweight='bold',
        #          color='#2E7D32')
        
        # Set plot limits and remove axes
        self.ax.set_xlim(-0.5, n * self.x_padding + 7)
        self.ax.set_ylim(lifeline_top - 0.5, self.diagram_height + 0.5)
        self.ax.axis('off')
        plt.tight_layout()
        return self.fig

    def save(self, filename):
        """Save the diagram to a file"""
        self.draw()
        plt.savefig(filename, bbox_inches='tight', dpi=300, facecolor=self.fig.get_facecolor())
        print(f"Diagram saved to: {filename}")
        plt.close()

    def start_alt(self, condition=""):
        """Start an alt block"""
        self.current_y += self.y_step  # Move upward
        # Store starting position and condition
        self.control_blocks.append(("alt", condition, self.current_y, None, None, None))
        
    def add_alt_branch(self, condition=""):
        """Add a branch to an alt block"""
        if self.control_blocks and self.control_blocks[-1][0] == "alt":
            block_type, _, start_y, _, _, _ = self.control_blocks[-1]
            self.current_y += self.y_step / 2  # Small movement
            # Add a note to show the branch condition
            self.add_note(f"[{condition}]")
    
    def end_alt(self):
        """End an alt block"""
        if self.control_blocks and self.control_blocks[-1][0] == "alt":
            block_type, label, start_y, _, _, _ = self.control_blocks.pop()
            x_min = min(self.participants.values()) - 1.5
            x_max = max(self.participants.values()) + 1.5
            # Update with end position and x-coordinates
            self.control_blocks.append((block_type, label, start_y, self.current_y, x_min, x_max))
    
    def start_loop(self, condition=""):
        """Start a loop block"""
        self.current_y += self.y_step  # Move upward
        # Store starting position and condition
        self.control_blocks.append(("loop", condition, self.current_y, None, None, None))
        
    def end_loop(self):
        """End a loop block"""
        if self.control_blocks and self.control_blocks[-1][0] == "loop":
            block_type, label, start_y, _, _, _ = self.control_blocks.pop()
            x_min = min(self.participants.values()) - 1.5
            x_max = max(self.participants.values()) + 1.5
            # Update with end position and x-coordinates
            self.control_blocks.append((block_type, label, start_y, self.current_y, x_min, x_max))
    
    def start_opt(self, condition=""):
        """Start an optional block"""
        self.current_y += self.y_step  # Move upward
        # Store starting position and condition
        self.control_blocks.append(("opt", condition, self.current_y, None, None, None))
        
    def end_opt(self):
        """End an optional block"""
        if self.control_blocks and self.control_blocks[-1][0] == "opt":
            block_type, label, start_y, _, _, _ = self.control_blocks.pop()
            x_min = min(self.participants.values()) - 1.5
            x_max = max(self.participants.values()) + 1.5
            # Update with end position and x-coordinates
            self.control_blocks.append((block_type, label, start_y, self.current_y, x_min, x_max)) 