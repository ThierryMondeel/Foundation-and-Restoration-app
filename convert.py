import json

def parse_yaml(content):
    """Simple YAML parser for the new movement family structure"""
    lines = content.split('\n')
    result = {}
    current_movement = None
    current_subcategory = None
    current_exercise = None
    in_exercise = False
    
    for line in lines:
        stripped = line.strip()
        
        # Skip comments and empty lines
        if stripped.startswith('#') or stripped == '':
            continue
        
        # Count leading spaces to determine nesting
        indent = len(line) - len(line.lstrip())
        
        # Movement family level (0 spaces)
        if indent == 0 and stripped.endswith(':'):
            # Save previous exercise if exists
            if current_exercise and current_subcategory:
                result[current_movement][current_subcategory].append(current_exercise)
                current_exercise = None
                in_exercise = False
            
            current_movement = stripped[:-1]
            result[current_movement] = {}
            current_subcategory = None
            in_exercise = False
        
        # Subcategory level (2 spaces)
        elif indent == 2 and stripped.endswith(':'):
            # Save previous exercise if exists
            if current_exercise and current_subcategory:
                result[current_movement][current_subcategory].append(current_exercise)
                current_exercise = None
                in_exercise = False
            
            current_subcategory = stripped[:-1]
            result[current_movement][current_subcategory] = []
            in_exercise = False
        
        # Exercise start (4 spaces, -)
        elif indent == 4 and (stripped.startswith('- Name:') or stripped.startswith('- name:')):
            # Save previous exercise if exists
            if current_exercise and current_subcategory:
                result[current_movement][current_subcategory].append(current_exercise)
            
            # Handle both capitalized and lowercase
            if stripped.startswith('- Name:'):
                name = stripped[7:].strip().strip('"')
            else:
                name = stripped[7:].strip().strip('"')
            
            current_exercise = {
                'name': name,
                'notes': ''
            }
            in_exercise = True
        
        # Exercise properties (6+ spaces)
        elif in_exercise and indent >= 6:
            if stripped.startswith('Notes:') or stripped.startswith('notes:'):
                # Handle both capitalized and lowercase
                if stripped.startswith('Notes:'):
                    current_exercise['notes'] = stripped[7:].strip().strip('"')
                else:
                    current_exercise['notes'] = stripped[6:].strip().strip('"')
    
    # Don't forget the last exercise
    if current_exercise and current_subcategory:
        result[current_movement][current_subcategory].append(current_exercise)
    
    return result

def map_subcategory_to_category(subcategory):
    """Map subcategory to app category"""
    # Handle both capitalized and lowercase
    sub_lower = subcategory.lower()
    if sub_lower == 'stretch':
        return 'stretch'
    return 'foundation'  # foundation and movement both map to foundation

def generate_tags(movement, subcategory):
    """Generate tags based on movement family and subcategory"""
    # Convert movement names to match original tag format
    movement_map = {
        'Side Lying': 'Side-lying',
        'Squat': 'Squat',
        'Supine': 'Supine',
        'Prone': 'Prone',
        'Lunge': 'Lunge',
        'Standing': 'Standing',
        'Sitting': 'Sitting',
        'Quadruped': 'Quadruped',
        'Walking & Favorites': 'Walking'
    }
    
    tags = [movement_map.get(movement, movement)]
    
    # Only add Locomotion tag for movement subcategory
    sub_lower = subcategory.lower()
    if sub_lower == 'movement':
        tags.append('Locomotion')
    
    return tags

# Read YAML file
with open('./exercises.yaml', 'r') as f:
    yaml_content = f.read()

data = parse_yaml(yaml_content)

# Convert to flat array format
exercises = []

for movement, subcategories in data.items():
    for subcategory, exercise_list in subcategories.items():
        for exercise in exercise_list:
            exercises.append({
                'name': exercise['name'],
                'category': map_subcategory_to_category(subcategory),
                'enabled': True,
                'tags': generate_tags(movement, subcategory),
                'notes': exercise.get('notes', '')
            })

# Write to JSON
with open('./exercises.json', 'w') as f:
    json.dump(exercises, f, indent=2)

print(f"✓ Converted {len(exercises)} exercises from exercises.yaml to exercises.json")
