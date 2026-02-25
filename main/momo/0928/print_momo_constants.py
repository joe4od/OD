import ast
import json
from pathlib import Path

p = Path(__file__).with_name('momo_ac.py')
src = p.read_text()
module = ast.parse(src)

values = {}
for node in module.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in ('url', 'COOKIE', 'headers', 'data'):
                try:
                    # Safely evaluate literal values
                    val = ast.literal_eval(node.value)
                except Exception:
                    # Fallback: get source segment and try eval in restricted namespace
                    seg = ast.get_source_segment(src, node.value)
                    try:
                        val = eval(seg, {})
                    except Exception:
                        val = seg
                values[target.id] = val

print(json.dumps(values, ensure_ascii=False, indent=2))

